# Generated by Django 3.2.9 on 2021-11-29 18:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211129_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='pp',
            field=django_resized.forms.ResizedImageField(crop=None, default='static_imgs/default_pp.jpeg', force_format='JPEG', keep_meta=True, quality=90, size=[1000, 1000], upload_to='profile_pics'),
        ),
    ]