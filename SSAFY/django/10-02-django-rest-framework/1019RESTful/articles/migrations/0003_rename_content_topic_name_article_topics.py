# Generated by Django 4.2.6 on 2023-10-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='content',
            new_name='name',
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(blank=True, null=True, to='articles.topic'),
        ),
    ]
