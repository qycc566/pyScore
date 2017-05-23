# coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
# 学校
class School(models.Model):
    name = models.CharField('学校', max_length=255)

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'

    def __unicode__(self):
        return self.name


# 年级
class Grade(models.Model):
    name = models.CharField('年级', max_length=255)
    class Meta:
        verbose_name = '年级'
        verbose_name_plural = '年级'

    def __unicode__(self):
        return self.name



# 班级
class Class(models.Model):
    school = models.ForeignKey(School)
    grade = models.ForeignKey(Grade)
    name = models.CharField('班级', max_length=255)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __unicode__(self):
        return self.name


# 考试
class Exam(models.Model):
    school = models.ForeignKey(School)
    grade = models.ForeignKey(Grade)
    name = models.CharField('考试名称', max_length=512)

    class Meta:
        verbose_name = '考试'
        verbose_name_plural = '考试'

    def __unicode__(self):
        return self.name



# 原始分数
class RawScore(models.Model):
    # 班级
    cls = models.ForeignKey(Class, null=False)
    # 考试
    exam = models.ForeignKey(Exam, null=False)
    # 导入日期
    imp_datetime = models.DateField('导入日时间', default=timezone.now())
    # 学号
    student_id = models.CharField('考号', max_length=32)
    # 姓名
    student_name = models.CharField('姓名', max_length=32)
    # 语文
    chinese = models.DecimalField('语文成绩', max_digits=8, decimal_places=2, default=0.0)
    # 数学
    mathematics = models.DecimalField('数学成绩', max_digits=8, decimal_places=2, default=0.0)
    # 英语
    english = models.DecimalField('英语成绩', max_digits=8, decimal_places=2, default=0.0)
    # 物理
    physics = models.DecimalField('物理成绩', max_digits=8, decimal_places=2, default=0.0)
    # 化学
    chemistry = models.DecimalField('化学成绩', max_digits=8, decimal_places=2, default=0.0)
    # 生物
    biology = models.DecimalField('生物成绩', max_digits=8, decimal_places=2, default=0.0)
    # 政治
    politics = models.DecimalField('政治成绩', max_digits=8, decimal_places=2, default=0.0)
    # 历史
    history = models.DecimalField('历史成绩', max_digits=8, decimal_places=2, default=0.0)
    # 地理
    geography = models.DecimalField('地理成绩', max_digits=8, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = '原始成绩'
        verbose_name_plural = '原始成绩'

    def __unicode__(self):
        return self.student_name + '的成绩'