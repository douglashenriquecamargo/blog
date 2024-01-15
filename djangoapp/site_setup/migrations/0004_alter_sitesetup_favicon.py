# Generated by Django 4.2.9 on 2024-01-15 12:04

from django.db import migrations, models
import utils.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validators.validate_png]),
        ),
    ]
