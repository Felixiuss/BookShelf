from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


GENDER = (
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    )

CITY = (
    ('kyiv', 'Киев'),
    ('harkov', 'Харьков'),
    ('lvov', 'Львов'),
    ('dnepr', 'Днепропетровск'),
    ('osessa', 'Одесса'),
    ('herson', 'Херсон'),
    ('vyshgorod', 'Вышгород'),
    ('kovel', 'Ковель'),
)


class Profile(models.Model):  # TODO добавить avatar
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    city = models.CharField(max_length=30, choices=CITY, default='kyiv')
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ сигнал создания модели Profile после создания модели User """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ сигнал сохранения модели Profile после создания модели User """
    instance.profile.save()
