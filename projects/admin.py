from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Review
from .models import Tag

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)