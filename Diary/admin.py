from django.contrib import admin
from .models import aboutModel, aboutQGModel, Advertising, BlogModel6

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(BlogModel6, BlogAdmin)
admin.site.register(aboutModel, BlogAdmin)
admin.site.register(aboutQGModel, BlogAdmin)
admin.site.register(Advertising, BlogAdmin)