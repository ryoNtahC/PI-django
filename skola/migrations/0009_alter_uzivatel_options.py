# Generated by Django 4.2.7 on 2024-04-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0008_uzivatel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uzivatel',
            options={'ordering': ['priezvisko', 'meno'], 'verbose_name': 'Uživateľ', 'verbose_name_plural': 'Užívatelia'},
        ),
    ]