"""Erzeugt index.html (installierbare PWA) aus app.html. Aufruf: python3 build.py"""
import re, pathlib
here = pathlib.Path(__file__).parent
body = (here / 'app.html').read_text()
head = '''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2A1640">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Zoes Gym">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" href="icons/icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}img{max-width:100%}</style>
</head>
<body>
'''
tail = '''
<script>
if('serviceWorker' in navigator){window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))}
if(navigator.storage&&navigator.storage.persist){navigator.storage.persist().catch(()=>{})}
</script>
</body>
</html>
'''
(here / 'index.html').write_text(head + body + tail)
# Cache-Version hochzählen, damit installierte Apps das Update laden
sw = here / 'sw.js'
t = sw.read_text()
m = re.search(r"zoes-gym-v(\d+)", t)
t = t.replace(m.group(0), f"zoes-gym-v{int(m.group(1)) + 1}")
sw.write_text(t)
print('index.html gebaut, Cache', f"v{int(m.group(1)) + 1}")
