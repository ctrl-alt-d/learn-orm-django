from django.contrib import admin


from .models import Categoria, SubCategoria, Producte

@admin.register(Producte)
class ProducteAdmin(admin.ModelAdmin):
    search_fields = ('nom', 'flags__nom')
    list_filter = ('sub_categoria__categoria',)

class ChoiceInline(admin.StackedInline):
    model = SubCategoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(SubCategoria)

