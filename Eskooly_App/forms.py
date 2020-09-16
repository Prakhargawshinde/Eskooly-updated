from django import forms
from Eskooly_App.models import Classes

class Classes_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "" 
    class Meta:
        model = Classes
        fields = "__all__"
        labels = {
        'Name_of_class': " ",
        'Monthly_fees':" ",
    }
        widgets = {
            'Name_of_class': forms.TextInput(attrs={'placeholder': 'Name Of Class'}),
            'Monthly_fees': forms.TextInput(attrs={'placeholder': 'Monthly Fees'}),
        }
