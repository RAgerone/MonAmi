# Generated by Django 2.0.1 on 2018-01-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistants', '0002_auto_20180104_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='image_url',
            field=models.CharField(default='https://i.imgur.com/yILM61G.jpg', max_length=100),
        ),
    ]
