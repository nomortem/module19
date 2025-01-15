from django.db import models
from decimal import Decimal

# Модель покупателя
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс покупателя
    age = models.IntegerField()  # Возраст покупателя

    def __str__(self):
        return self.namegi

# Модель игры
class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена игры
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер игры
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # Ограничение по возрасту (18+)
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели, которые обладают этой игрой

    def __str__(self):
        return self.title
