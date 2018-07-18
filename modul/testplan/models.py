from django.db import models

from django.contrib.auth.models import User

from modul.tag.models import Tag


class TestPlan(models.Model):

    STATUS_CHOICES = (('No_test', 'Не тесировался'),
                      ('Fail', 'Провал'),
                      ('Done', 'Прошел'),
                      ('Error', 'Ошибка'))

    name = models.CharField('Название тест плана', max_length=60)
    description = models.CharField('Описание тест плана', max_length=300)
    precondition = models.CharField('предварительное условие', max_length=1000)
    create = models.DateTimeField('дата создания', auto_now_add=True)
    change = models.DateTimeField('последнее изменение', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='No_test', verbose_name='статус')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='тег')
    test_case = models.ManyToManyField('testcase.TestCase', through='testplan.PlanCase')

    class Meta:
            verbose_name = 'Тест План'
            verbose_name_plural = 'Тест План'

    def __str__(self):
        return self.name


class PlanCase(models.Model):
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    test_case = models.ForeignKey('testcase.TestCase', on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Связь'
            verbose_name_plural = 'Связи'

 #   def __str__(self):
  #      return str(self.id)

    def __str__(self):
        return 'PlanCase: {}'.format(self.id)


class LogPlan(models.Model):
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, verbose_name='описание')
    create = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')

    class Meta:
            verbose_name = 'Лог плана'
            verbose_name_plural = 'Логи планов'

    def __str__(self):
        return self.create


# Create your models here.
