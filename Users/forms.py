from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Subs


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']

class SubsForm(forms.ModelForm):
    SELECTIONS_1 = (
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
    )
    SELECTIONS_4 = (
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
        ("Candidate E", "Candidate E"),
        ("Candidate F", "Candidate F"),
        ("Candidate G", "Candidate G"),
        ("Candidate 1", "Candidate 1"),
        ("Candidate 2", "Candidate 2"),
        ("Candidate 3", "Candidate 3"),
        ("Candidate 4", "Candidate 4"),
        ("Candidate 5", "Candidate 5")
    )
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    phone_number = forms.CharField(required = True)
    question_1 = forms.ChoiceField(label = "President Elect", required = True, choices = SELECTIONS_1, widget = forms.RadioSelect)
    question_2 = forms.ChoiceField(label = "Recording Secretary", required = True, choices = SELECTIONS_1, widget = forms.RadioSelect)
    question_3 = forms.ChoiceField(label = "Assistant Recording Secretary", required = True, choices = SELECTIONS_1, widget = forms.RadioSelect)
    question_4 = forms.MultipleChoiceField(label = "Public Relations Officers (Choose 7)", widget = forms.CheckboxSelectMultiple, choices = SELECTIONS_4)
    question_5 = forms.MultipleChoiceField(label = "Board of Directors (Choose 2)", widget=forms.CheckboxSelectMultiple, choices=SELECTIONS_4)
    question_6 = forms.ChoiceField(label="Corresponding Secretary", required=True, choices=SELECTIONS_1, widget = forms.RadioSelect)
    question_7 = forms.ChoiceField(label = "Assistant Corresponding Secretary", required=True, choices=SELECTIONS_1, widget = forms.RadioSelect)
    question_8 = forms.ChoiceField(label = "Treasurer", required=True, choices=SELECTIONS_1, widget = forms.RadioSelect)
    question_9 = forms.ChoiceField(label="Assistant Treasurer", required=True, choices=SELECTIONS_1, widget = forms.RadioSelect)
    question_10 = forms.ChoiceField(label = "Auditor", required=True, choices=SELECTIONS_1, widget = forms.RadioSelect)

    def verify_num(self):
        value = self.cleaned_data['question_4']
        if len(value) > 7:
            raise forms.ValidationError("You cannot select more than 7 items.")
        return value

    class Meta:
        model = Subs
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                 'question_1', 'question_2', 'question_3',
                 'question_6', 'question_7', 'question_8', 'question_9',
                 'question_10', 'question_4', 'question_5']