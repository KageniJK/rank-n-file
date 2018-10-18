from django import forms
from .models import Project, Rating


class PostProjectForm(forms.ModelForm):
    """
    Enables the user to upload their projects
    """
    class Meta:
        model = Project
        exclude = ['user','date_posted']


class VoteForm(forms.ModelForm):
    """
    Enables the users to vote on projects
    """
    class Meta:
        model = Rating
        exclude = ['user', 'project']
