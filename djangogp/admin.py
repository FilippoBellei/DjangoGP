from django.contrib import admin
from .models import Rider, Race, Result, Standings

admin.site.register(Rider)
admin.site.register(Race)
admin.site.register(Result)
admin.site.register(Standings)
