from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model  = Project   #指定哪一個class
        fields = ['title','description','featured_image',
        'demo_link','source_link','tags'] #form裡面 建造哪些 attribute


        widgets = {
            'tags' : forms.CheckboxSelectMultiple()
        }
    

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'}) #讓title 裡面的class update 成unput
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
