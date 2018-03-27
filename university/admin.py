from django.contrib import admin
from .models import *

admin.site.register(Lecturer)
admin.site.register(Disciplines)
admin.site.register(Publications)
admin.site.register(Department)
admin.site.register(Specialty)
admin.site.register(Science_interest)

# Register your models here.
