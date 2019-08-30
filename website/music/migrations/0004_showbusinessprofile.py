# Generated by Django 2.2.4 on 2019-08-23 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_businessprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowBusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.BusinessProfile')),
            ],
        ),
    ]
