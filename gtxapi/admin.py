from django.contrib import admin
from django.contrib.admin import autodiscover, site, AdminSite, ModelAdmin, StackedInline, TabularInline, HORIZONTAL, VERTICAL
from gtxapi.models import Task, Status, Tag


class tagInline(admin.TabularInline):

    model = Task.tags.through
    verbose_name = u"Tag"
    verbose_name_plural = u"Tags"


class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at', 'owner', 'created_by')
    exclude = ("status", "tags" )
    inlines = (tagInline,)



# Register your models here.
admin.site.register(Tag)
admin.site.register(Status)
admin.site.register(Task, TaskAdmin)




