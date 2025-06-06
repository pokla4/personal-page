from pathlib import Path

BLOG_PATH = 'blog/'

def _response(res: str) -> str:
    with open('template.html') as f:
        template = f.read().strip()
    return template + res + '</div>'

def index_page():
    res = ""
    for x in Path(BLOG_PATH).iterdir():
        if x.name.endswith('.md'):
            name = x.name.removesuffix('.md')
            res += f'<a href="{name}">{name}</a>' + '<br />'
    return _response(res)


import mistune
def md_page(pagename: str):
    try:
        with open(BLOG_PATH + pagename + '.md') as f:
            html = mistune.html(f.read())
            assert type(html) == str
            return _response(html)
    except FileNotFoundError:
        return 0




