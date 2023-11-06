from pathlib import PurePath
from playscript.conv import fountain, pdf

with open(PurePath('.', 'script', 'yuki.fountain'), encoding='utf-8-sig') as f:
    script = fountain.psc_from_fountain(f.read())

pdf_stream = pdf.psc_to_pdf(script)

with open('out.pdf', 'wb') as f:
    f.write(pdf_stream.read())