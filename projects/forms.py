from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model  = Project   #指定哪一個class
        fields = ['title','description','demo_link','source_link','tags'] #form裡面 建造哪些 attribute
