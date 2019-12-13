# Generated by Django 2.2.1 on 2019-12-04 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('example', '0002_auto_20191016_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product_id',
            field=models.ForeignKey(on_delete=models.SET(-1), to='example.Product'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product_id',
            field=models.ForeignKey(on_delete=models.SET(-1), to='example.Product'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='user_id',
            field=models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='inventory_id',
            field=models.ForeignKey(on_delete=models.SET(-1), to='example.Inventory'),
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('sale_id', models.ForeignKey(on_delete=models.SET(-1), to='example.Sale')),
                ('user_id', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notificaciones',
            },
        ),
    ]
