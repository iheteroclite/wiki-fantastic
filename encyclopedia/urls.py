from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('wiki/str:<title>', views.entry, name='entry')
]


handler404 = 'encyclopedia.views.error_404'