from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Image)
admin.site.register(Testimonial)
admin.site.register(Brands)
admin.site.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile number','message')