# Generated by Django 4.1.3 on 2022-11-21 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='favicon',
            field=models.FileField(blank=True, help_text='(.ico|.png|.gif - 16x16|32x32 px)', upload_to='static/favicon/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'ico', 'jpg', 'jpeg', 'png', 'svg'])], verbose_name='favicon'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo',
            field=models.FileField(blank=True, help_text='Leave blank to use the default Django logo', upload_to='static/logo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'jpg', 'jpeg', 'png', 'svg'])], verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='phone_number',
            field=models.CharField(default='+91 6361662946', max_length=200, verbose_name='Phone Number'),
        ),
    ]
