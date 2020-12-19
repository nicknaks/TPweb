from django.contrib.auth.models import User
from django.db import models

class s(models.Model):
    user = models.OneToOne