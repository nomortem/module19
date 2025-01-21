from django.contrib import admin
from .models import Game, Buyer

# Класс для администрирования модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_per_page = 20

# Класс для администрирования модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)