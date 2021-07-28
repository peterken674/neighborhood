# Generated by Django 3.2.5 on 2021-07-27 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0014_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='neighbors', to='neighborhood.neighborhood'),
            preserve_default=False,
        ),
    ]