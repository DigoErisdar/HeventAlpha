from django.contrib import admin

from apps.guilds.admin import hevent
from apps.help.models import FeedBack
from helper.admin import DontLog, PublicFullHide


@admin.register(FeedBack, site=hevent)
class AdminFeedBack(DontLog, PublicFullHide, admin.ModelAdmin):
    list_display = ['message', 'date_created']
    date_hierarchy = 'date_created'
