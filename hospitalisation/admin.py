from django.contrib import admin
from .models import *

admin.site.register(Date_travail)
admin.site.register(Patient)
admin.site.register(Ressource_Materiel)
admin.site.register(Assistant)
admin.site.register(Médcin)
admin.site.register(Salle)
admin.site.register(Hospitalisation)

# Register your models here.
