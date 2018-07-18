from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields


class TagItem(models.Model):

    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Тегер'
        verbose_name_plural = 'Тегеры'

    def __str__(self):
        return self.tag


class Tag(models.Model):
    name = models.CharField('имя тега', max_length=60, default='python')
    tags = fields.GenericRelation(TagItem, content_type_field='content_type_fk', object_id_field='object_primary_key')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


# Create your models here.
