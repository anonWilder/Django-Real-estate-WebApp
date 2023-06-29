# Generated by Django 4.2.2 on 2023-06-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0006_remove_download_link_remove_download_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='download',
            old_name='imgname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='download',
            name='imglink',
        ),
        migrations.RemoveField(
            model_name='download',
            name='pdflink',
        ),
        migrations.RemoveField(
            model_name='download',
            name='pdfname',
        ),
        migrations.AddField(
            model_name='download',
            name='link',
            field=models.URLField(default=''),
        ),
    ]