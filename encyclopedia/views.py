from django.http import HttpRequest
from markdown2 import markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # TODO: make new function in utils called check_title
    matches = util.check_title(title)
    if matches:
        text = markdown(util.get_entry(matches[0]))
        # test if more than one match
        if len(matches) > 1:
            text = f'<h1>Multiple entries for {title}</h1>'
            for match in matches:
                # TODO format this div style to a max size (like 1/3 of page + title height or something)
                # TODO: this div is a link to that entry
                text += f'<div>{markdown(util.get_entry(match))}</div>'

        return render(request, 'encyclopedia/entry.html', {
            'title': matches[0],
            'text': text
        })
    # TODO: redirect to the correct page if user misses the /wiki/ bit
    return render(request, 'encyclopedia/404.html', {
        'path_title': title
    })

def error_404(request, exception):
    # check whether there is a match before returning a suggestion
    # get the last piece of the path to suggest alternative
    path_end = request.path.split('/')[-1]
    try:
        match = util.check_title(path_end)[0]
    except:
        match = ''

    return render(request,'encyclopedia/404.html', {
        'path_title': match,
        'title' : path_end  })
