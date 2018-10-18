from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the basic Django user model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)


class Project(models.Model):
    """
    class that defines the projects
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    link = models.URLField()
    description = models.CharField(max_length=250)
    screenshot = models.ImageField(upload_to='screengrabs/')
    date_posted = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_recent(cls):
        all = cls.objects.all()
        return all

    @classmethod
    def get_by_id(cls,id):
        return cls.objects.get(id=id)


class Rating(models.Model):
    """
    class that defines the votes
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)

