# Generated by Django 2.2.1 on 2019-12-09 20:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('example', '0004_auto_20191209_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sesiones',
            },
        ),
    ]