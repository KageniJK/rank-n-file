from django import forms
from .models import Project


class PostProjectForm(forms.ModelForm):
    """
    Enables the user to upload their projects
    """
    class Meta:
        model = Project
        exclude = ['user','date_posted']