from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MODEL-Topic: Stars, Planets, Animals.
class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

# MODEL-Entry: Sun is our.., Mercury is the.., Lion is a..
class Entry(models.Model):
    """Запись по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели"""
        return f"{self.text[:10]}..."