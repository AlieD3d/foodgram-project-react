from django.contrib.admin import ModelAdmin, TabularInline, register, site
from django.utils.safestring import mark_safe

from .models import AmountIngredient, Ingredient, Recipe, Tag

site.site_header = 'Администрирование Foodgram'
EMPTY_VALUE_DISPLAY = 'Пусто'


class IngredientInLine(TabularInline):
    model = AmountIngredient
    extra = 2


@register(AmountIngredient)
class LinkedAdmin(ModelAdmin):
    pass


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'name', 'author', 'get_image',
    )
    fields = (
        ('name', 'cooking_time'),
        ('author', 'tags'),
        ('text',),
        ('image',),
    )
    row_id_fields = ('author',)
    search_fields = (
        'name', 'author',
    )
    list_filter = (
        'name', 'author__username',
    )
    inlines = (IngredientInLine,)
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="30"')

    get_image.short_description = 'Изображение'


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'name', 'color', 'slug',
    )
    search_fields = (
        'name', 'color',
    )
    save_on_top = True
    empty_value_display = EMPTY_VALUE_DISPLAY
    prepopulated_fields = {'slug': ('name',)}
