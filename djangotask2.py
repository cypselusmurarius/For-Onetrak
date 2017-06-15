# Запросы с помощью django ORM

from django.db import models

class Faculty(models.Model):
    title = models.CharField(max_length=255, verbose_name='Faculty name')
    description = models.TextField(
        verbose_name='Faculty description', default=’’, blank=True)

class Student(models.Model):
   first_name = models.CharField(max_length=255, verbose_name='First name')
   last_name = models.CharField(max_length=255, verbose_name='Last name')
   birthday = models.DateField(verbose_name='User birthday')
   faculty = models.ForeignKey(Faculty, verbose_name='Faculty')

# Общее кол-во студентов

Student.objects.count()

# Кол-во студентов, которые обучаются на факультете "faculty1"

f = Faculty.objects.get(title='faculty1')
Student.objects.get(faculty_id = f.id).count()

# Список словарей со значениями: имя студента, фамилия студента, наименование факультета, на котором он учится.

Student.objects.values('first_name', 'last_name', 'faculty')

# Подсчет кол-ва студентов на каждом факультете

s = Student.objects.values('first_name', 'last_name', 'faculty')
for s in a:
    Student.objects.get(faculty_id=s['faculty']).count()
