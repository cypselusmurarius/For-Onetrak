# Необходимо продумать и описать модели django для сущностей Устройство-Пользователь.
# Одно устройство может быть привязано только к одному пользователю. Пользователь может иметь несколько устройств одновременно.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)  # имя пользователя
    email = models.CharField(max_length=200) # email
    phone = models.CharField(max_length=200) # телефон пользователя

    def __str__(self):
        return "%s %s %s" % (self.name, self.email, self.phone)

class Gadget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # связь моделей устройство-пользователь
    name = models.CharField(max_length=200) 

    def __str__(self):
        return "%s" % (self.name)
