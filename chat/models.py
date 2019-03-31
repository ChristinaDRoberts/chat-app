from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.humanize.templatetags.humanize import naturaltime




#get_user_model is a built in contrib "auth" app
User = get_user_model()



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created = models.DateTimeField()

    def __str__(self):
        return self.user.username
