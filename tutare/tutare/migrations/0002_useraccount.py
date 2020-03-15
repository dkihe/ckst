# Generated by Django 3.0.3 on 2020-03-15 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=25)),
                ('account_password', models.CharField(default='', max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutare.User')),
            ],
        ),
    ]
