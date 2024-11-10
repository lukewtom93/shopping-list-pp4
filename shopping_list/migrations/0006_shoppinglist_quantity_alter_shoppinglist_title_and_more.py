# Generated by Django 4.2.16 on 2024-11-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0005_alter_item_shopping_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='title',
            field=models.CharField(default='Shopping list', max_length=100),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]