from django import forms  # Correctly import forms from django
from django.forms import ModelForm
from .models import Projects, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        # fields = '__all__'
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):  # Move __init__ outside Meta class
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        # self.fields['title'].widget.attrs.update({'class': 'input','placeholder':'Add title'})

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment to your vote'
        }
    def __init__(self, *args, **kwargs):  # Move __init__ outside Meta class
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        # self.fields['title'].widget.attrs.update({'class': 'input','placeholder':'Add title'})

