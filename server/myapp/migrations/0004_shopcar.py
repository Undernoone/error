# Generated by Django 3.2.11 on 2024-05-09 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_shopcar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('thing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thing_shopcar', to='myapp.thing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_shopcar', to='myapp.user')),
            ],
            options={
                'db_table': 'shop_car',
            },
        ),
    ]
