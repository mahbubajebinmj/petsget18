<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User 

=======

from django.db import models
from django.contrib.auth.models import User 

>>>>>>> 1baf8065ac4f3616ce0644d08045d47b515619ff

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
<<<<<<< HEAD
    is_verified = models.BooleanField( default=False)
=======
    #is_verified = models.BooleanField( Default-False)
>>>>>>> 1baf8065ac4f3616ce0644d08045d47b515619ff
