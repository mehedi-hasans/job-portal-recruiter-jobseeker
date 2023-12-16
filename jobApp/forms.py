from django import forms

class JobCreateForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label='Company Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    job_image = forms.ImageField(label='Job Cover Image', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
