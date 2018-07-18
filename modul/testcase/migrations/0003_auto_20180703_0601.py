# Generated by Django 2.0.6 on 2018-07-03 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0002_auto_20180702_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=1000, verbose_name='Действие')),
                ('expected_result', models.CharField(max_length=1000, verbose_name='ожидаемый результа')),
                ('test_result', models.CharField(max_length=1000, verbose_name='результат тестирования')),
            ],
            options={
                'verbose_name': 'Тест кейс',
                'verbose_name_plural': 'Тест кейсы',
            },
        ),
        migrations.AlterField(
            model_name='logcase',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='description',
            field=models.TextField(max_length=300, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='precondition',
            field=models.TextField(max_length=1000, verbose_name='предварительное условие'),
        ),
        migrations.AddField(
            model_name='step',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcase.TestCase'),
        ),
    ]