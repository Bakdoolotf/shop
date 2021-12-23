from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории' #название модели во множественном числе
        verbose_name = 'Категория' #название модели в единственном числе

#Таблица продукта
class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    price = models.PositiveIntegerField(verbose_name="Цена оптом", )
    volume = models.CharField(max_length=15, verbose_name="Объём")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    
    class Meta:
            verbose_name_plural = 'Товары' #название модели во множественном числе
            verbose_name = 'Товар' #название модели в единственном числе

    def __str__(self):
        return self.title
#Таблица Заказа
class ListRequestdetail(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product', null=True)
    quantity = models.PositiveIntegerField(verbose_name="Количество", )
    summ = models.PositiveIntegerField(verbose_name="Сумма",blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_active = models.BooleanField(default=True, verbose_name="Активность запроса")
    is_finish = models.BooleanField(default=False, verbose_name="Запрос на обработку")
    address = models.CharField(max_length=255, verbose_name="адресс")
    phone_number = models.IntegerField( verbose_name="Номер телефона")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    
    class Meta:
            verbose_name_plural = 'Запросы товра' #название модели во множественном числе
            verbose_name = 'Запрос товара' #название модели в единственном числе

    def __str__(self):
        return f'Товар: {self.product}'
    
    # def save(self, *args, **kwargs):
    #     self.summ = self.quantity * self.price
    #     return super().save(*args, **kwargs)




