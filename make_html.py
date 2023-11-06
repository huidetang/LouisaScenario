from pathlib import PurePath
from playscript.conv import fountain, html

with open(PurePath('.', 'script', 'yuki.fountain'), encoding='utf-8-sig') as f:
    script = fountain.psc_from_fountain(f.read())

html_str = html.psc_to_html(script)
with open('out.html', 'w', encoding='utf-8') as f:
    f.write(html_str)