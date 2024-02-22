import sys
import re

html = """
<html>
    <head>
        <title>HTML Page</title>
        <meta charset="utf-8">
    </head>
    <body>

"""

md = open(sys.argv[1], "r").read()

# CABEÇALHOS
md = re.sub(r"^#(\s.*)$", r"<h1>\1</h1>", md, flags=re.MULTILINE)   # H1
md = re.sub(r"^##(\s.*)$", r"<h2>\1</h2>", md, flags=re.MULTILINE)  ## H2
md = re.sub(r"^###(\s.*)$", r"<h3>\1</h3>", md, flags=re.MULTILINE) ### H3

# BOLD
md = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", md)

# ITÁLICO
md = re.sub(r"\*(.*?)\*", r"<i>\1</i>", md)

# BLOCKQUOTE
md = re.sub(r"^\s>\s*(.+)$", r"<blockquote>\1</blockquote>", md, flags=re.MULTILINE)

# LISTA NUMERADA
md = re.sub(r"^\s*\d+\.\s+(.+)$", r"<li>\1</li>", md, flags=re.MULTILINE)
md = re.sub(r"((<li>.*</li>\n)+)", r"<ol>\n\1</ol>\n", md, flags=re.MULTILINE)

# LISTA NÃO NUMERADA
md = re.sub(r'^\s*-\s+(.+)$', r'<lo>\1</lo>', md, flags=re.MULTILINE)
md = re.sub(r'((<lo>.*</lo>\n)+)', r'<ul>\n\1</ul>\n', md, flags=re.MULTILINE)
md = re.sub(r'<lo>', r'<li>', md)
md = re.sub(r'</lo>', r'</li>', md)

# CODE
md = re.sub(r'`(.*)`', r'<code>\1</code>', md)

# HORIZONTAL RULE
md = re.sub(r'^\s*---\s*$', r'<hr>', md, flags=re.MULTILINE)

# IMAGEM
md = re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)', r'<img src="\2" alt="\1"/>', md)

# LINK
md = re.sub(r'\[([^\]]*)\]\(([^\)]*)\)', r'<a href="\2">\1</a>', md)

html += md

html += """

    </body>
</html>"""

html_page = open("page.html", "w", encoding="utf-8")
html_page.write(html)
html_page.close()