from pathlib import Path

def index_page():
    res = ""
    for x in Path('pages/').iterdir():
        if x.name.endswith('.md'):
            name = x.name.removesuffix('.md')
            res += f'<a href="{name}">{name}</a>'
    return res


import mistune
def md_page(pagename: str):
    try:
        with open('pages/' + pagename + '.md') as f:
            return mistune.html(f.read())
    except FileNotFoundError:
        return 0




