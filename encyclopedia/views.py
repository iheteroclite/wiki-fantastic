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
            'title': title,
            'text': util.get_entry(match[0])
        })
    # TODO: test if more than one match?

    # TODO: make a 404 page
    return render(request, 'encyclopedia/entry.html', {
        'title': title,
        'text': f'No Entry for {title}'
    })