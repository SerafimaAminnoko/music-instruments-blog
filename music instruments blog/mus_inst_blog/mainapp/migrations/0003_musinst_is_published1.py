# Generated by Django 4.2 on 2023-04-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_mainpage_rename_text_musinst_text1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musinst',
            name='is_published1',
            field=models.BooleanField(default=True),
        ),
    ]
