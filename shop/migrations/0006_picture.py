# Generated by Django 3.2.16 on 2023-01-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20221229_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('pic_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
