# Generated by Django 2.0.6 on 2018-07-02 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logcase',
            name='status',
            field=models.CharField(choices=[('No_test', 'Не тесировался'), ('Fail', 'Провал'), ('Done', 'Прошел'), ('Error', 'Ошибка')], default='Не тесировался', max_length=15),
        ),
        migrations.AlterField(
            model_name='logcase',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcase.TestCase'),
        ),
        migrations.AlterField(
            model_name='logcase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='results',
            field=models.CharField(max_length=1000, verbose_name='результат'),
        ),
    ]
