# Generated by Django 3.0.5 on 2020-05-22 02:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20200502_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoteName', models.CharField(max_length=150)),
                ('AreaContent', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
