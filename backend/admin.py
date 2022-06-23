from django.contrib import admin
from .models import Demande, Beneficiaire

class DemandeAdmin(admin.ModelAdmin):
    list_display=("beneficiaire", "date_demande", "appareil")


admin.site.register(Demande,DemandeAdmin)
admin.site.register(Beneficiaire)