from django.contrib import admin
from listing.models import Band, Goodies


# Register your models here.

class BandAdmin(admin.ModelAdmin):  # Diplay pour affichage dans l'interface admin de Django
    list_display = ('name', 'year_formed',
                    'genre')  # les paramètres de 'list_display' correspondent aux éléments que nous voulons afficher


class GoodiesAdmin(admin.ModelAdmin):
    list_display = ('label', 'year', 'type')


admin.site.register(Band, BandAdmin)  # ici on appel le Model Band ainsi que le 'diplay' créé juste au dessus

admin.site.register(Goodies, GoodiesAdmin)  # ici on appel le Model Goodies ainsi que le 'diplay' créé juste au dessus
