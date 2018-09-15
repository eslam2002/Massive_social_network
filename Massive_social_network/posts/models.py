from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    # image = models.ImageField(upload_to='photos',blank=True)
    timeposted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        # return reverse('authentication:home', kwargs={'username': self.user.username,'pk':self.pk})
        return reverse('post:list')

    class Meta:
        ordering = ['-timeposted']
