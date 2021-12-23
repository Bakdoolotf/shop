# Generated by Django 4.0 on 2021-12-16 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('price', models.PositiveIntegerField(verbose_name='Цена оптом')),
                ('volume', models.CharField(max_length=15, verbose_name='Объём')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ListRequestdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('summ', models.PositiveIntegerField(blank=True, null=True, verbose_name='Сумма')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность запроса')),
                ('is_finish', models.BooleanField(default=False, verbose_name='Запрос на обработку')),
                ('address', models.CharField(max_length=255, verbose_name='адресс')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='auth.user')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='api.products')),
            ],
            options={
                'verbose_name': 'Запрос товара',
                'verbose_name_plural': 'Запросы товра',
            },
        ),
    ]
