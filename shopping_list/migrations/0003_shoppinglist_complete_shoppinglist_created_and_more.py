# Generated by Django 4.2.16 on 2024-11-06 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_list', '0002_rename_post_shoppinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
