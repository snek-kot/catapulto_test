# Generated by Django 2.0.6 on 2018-07-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0003_auto_20180703_0601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logcase',
            options={'verbose_name': 'Лог кейса', 'verbose_name_plural': 'Логи кейсов'},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'verbose_name': 'Шаг', 'verbose_name_plural': 'Шаги'},
        ),
    ]