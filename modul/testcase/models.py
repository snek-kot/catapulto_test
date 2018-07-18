from django.db import models

from django.contrib.auth.models import User


class TestCase(models.Model):

    STATUS_CHOICES = (('No_test', 'Не тесировался'),
                      ('Fail', 'Провал'),
                      ('Done', 'Прошел'),
                      ('Error', 'Ошибка'))

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Не тесировался')
    name = models.CharField('имя', max_length=60)
    precondition = models.TextField('предварительное условие', max_length=1000)
    description = models.TextField('описание', max_length=300)
    results = models.CharField('результат', max_length=1000)
    create = models.DateTimeField('дата создания', auto_now_add=True)
    change = models.DateTimeField('последнее изменение', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')

    class Meta:
            verbose_name = 'Тест кейс'
            verbose_name_plural = 'Тест кейсы'

    def __str__(self):
        return self.name


class LogCase(models.Model):

    STATUS_CHOICES = (('No_test', 'Не тесировался'),
                      ('Fail', 'Провал'),
                      ('Done', 'Прошел'),
                      ('Error', 'Ошибка'))
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Не тесировался')
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание')
    create = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')

    class Meta:
            verbose_name = 'Лог кейса'
            verbose_name_plural = 'Логи кейсов'

    def __str__(self):
        return str(self.id)


class Step(models.Model):
    action = models.CharField('Действие', max_length=1000)
    expected_result = models.CharField('ожидаемый результа', max_length=1000)
    test_result = models.CharField('результат тестирования', max_length=1000)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    class Meta:
            verbose_name = 'Шаг'
            verbose_name_plural = 'Шаги'

    def __str__(self):
        return str(self.id)
