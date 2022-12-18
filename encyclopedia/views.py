from markdown2 import markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    match = [i for i in util.list_entries() if (i.lower() == title.lower())]
    if match:
        return render(request, 'encyclopedia/entry.html', {
            'title': match[0],
            'text': markdown(util.get_entry(match[0]))
        })
    # TODO: test if more than one match - display options
    return render(request, 'encyclopedia/404.html', {
        'title': title
    })