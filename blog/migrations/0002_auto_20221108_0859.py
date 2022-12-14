# Generated by Django 3.2.16 on 2022-11-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
