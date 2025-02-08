from django.contrib import admin

from api.models import Countries

# Register your models here.
admin.site.register([Countries])  # Registering models in the admin panel
