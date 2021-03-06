from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус',
                               related_name='statuses')
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тип',
                             related_name='types')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    project = models.ForeignKey('webapp.Project', null=True, blank=False, related_name='projects',
                                on_delete=models.PROTECT, verbose_name='Проект')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)



class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name




class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name