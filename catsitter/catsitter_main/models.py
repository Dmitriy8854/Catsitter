from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Questionnaire(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questionnaire'
    )
    def __str__(self):

        return self.text