from django.contrib import admin
from .models import Task # This imports your Task "blueprint"

admin.site.register(Task) # This tells the Admin: "Please show this list!"