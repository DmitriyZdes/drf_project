
# Register your models here.
from django.contrib import admin

# Register your models here.
from course.models import Stage, Subject

admin.site.register(Stage, Subject)
