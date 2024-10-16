# Generated by Django 5.1.1 on 2024-10-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='depth',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='path',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
