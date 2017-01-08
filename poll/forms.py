from django import forms
from .models import Question,Choice

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('author','question_text')

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields= ('choice_text','votes')
