from __future__ import unicode_literals
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Compileinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compileinfo'


class Custominput(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    input_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custominput'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    to_user = models.CharField(max_length=48)
    from_user = models.CharField(max_length=48)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    new_mail = models.IntegerField()
    reply = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mail'


class Online(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=20)
    ua = models.CharField(max_length=255)
    refer = models.CharField(max_length=255, blank=True, null=True)
    lastmove = models.IntegerField()
    firsttime = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online'

class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    input = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    sample_input = models.TextField(blank=True, null=True)
    sample_output = models.TextField(blank=True, null=True)
    spj = models.CharField(max_length=1)
    hint = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    defunct = models.CharField(max_length=1)
    accepted = models.IntegerField(blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem'


class Reply(models.Model):
    rid = models.AutoField(primary_key=True)
    author_id = models.CharField(max_length=48)
    time = models.DateTimeField()
    content = models.TextField()
    topic_id = models.IntegerField()
    status = models.IntegerField()
    ip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reply'


class Runtimeinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtimeinfo'


class Sim(models.Model):
    s_id = models.IntegerField(primary_key=True)
    sim_s_id = models.IntegerField(blank=True, null=True)
    sim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'


class Solution(models.Model):

    SYNTAX_CHOICES = (
        (0, 'C'),
        (1, 'C++'),
        (2, 'Java'),
        (6, 'Python'),
        )

    solution_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    user_id = models.CharField(max_length=48)
    time = models.IntegerField()
    memory = models.IntegerField()
    in_date = models.DateTimeField()
    result = models.SmallIntegerField()
    language = models.IntegerField(choices=SYNTAX_CHOICES)
    ip = models.CharField(max_length=46)
    contest_id = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField()
    num = models.IntegerField()
    code_length = models.IntegerField()
    judgetime = models.DateTimeField(blank=True, null=True)
    pass_rate = models.DecimalField(max_digits=3, decimal_places=2)
    lint_error = models.IntegerField()
    judger = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'solution'


class SourceCode(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code'


class SourceCodeUser(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code_user'
