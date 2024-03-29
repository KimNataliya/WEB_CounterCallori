from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Food, Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('food_selected', 'quantity',)

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.filter(person_of=user)


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'quantity', 'calorie', 'proteins', 'fats', 'carbs')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('calorie_goal', 'proteins_goal', 'fats_goal', 'carbs_goal')
