from django.contrib import admin

from .models import Movie, Viewer

admin.site.register(Movie)
admin.site.register(Viewer)
