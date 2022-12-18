from markdown2 import markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    matches = [i for i in util.list_entries() if (i.lower() == title.lower())]
    if matches:
        text = markdown(util.get_entry(matches[0]))
        # test if more than one match
        if len(matches) > 1:
            text = f'<h1>Multiple entries for {title}</h1>'
            for match in matches:
                # TODO format this div style to a max size (like 1/3 of page + title height or something)
                text += f'<div>{markdown(util.get_entry(match))}</div>'

        return render(request, 'encyclopedia/entry.html', {
            'title': matches[0],
            'text': text
        })
    # TODO: redirect to the correct page if user misses the /wiki/ bit
    return render(request, 'encyclopedia/404.html', {
        'title': title
    })