import sys, subprocess
from playwright.sync_api import sync_playwright
html, out = sys.argv[1], sys.argv[2]
times = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
FPS = 30
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + html); pg.wait_for_timeout(800)
    pg.evaluate('document.fonts.ready')
    if times:  # stills
        for t in times:
            pg.evaluate(f'render({t})'); pg.screenshot(path=f'{out}_{t}.png')
    else:
        dur = pg.evaluate('window.DUR')
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
        for i in range(int(dur * FPS)):
            pg.evaluate(f'render({i / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
        ff.stdin.close(); ff.wait()
    b.close()
