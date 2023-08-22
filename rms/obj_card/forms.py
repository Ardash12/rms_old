from django import forms
from django.forms.widgets import Select, SelectMultiple

from mptt.forms import MoveNodeForm, TreeNodeChoiceField

from allauth.account.forms import LoginForm, SignupForm

from .models import Object, Picture, Category, Storage


class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.obj_user = kwargs.pop('obj_user', None)
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['storage'].queryset = Storage.objects.filter(object__in=self.obj_user).distinct()
        self.fields['category'].queryset = Category.objects.filter(object__in=self.obj_user).distinct()
    
    storage = forms.ModelChoiceField(
        queryset=None,
        label=u'Место хранения',
        required=False,
        widget=forms.Select(attrs={'class':'hidden'}),
        ) 

    category = TreeNodeChoiceField(
        queryset=None, 
        label="Категория",
        required=False,
        )
    

class ObjForm(forms.Form):

    name = forms.CharField(label=u'Название')
    description = forms.CharField(label=u'Описание')
    storage = forms.ModelChoiceField(
        queryset=Storage.objects.all(),
        label=u'Место хранения',
        ) 
    category = TreeNodeChoiceField(
        queryset=Category.objects.all(), 
        label="Выберите категорию",
        )
    photos = forms.ImageField(
        label=u'Фотографии', 
        widget=forms.FileInput(attrs={'multiple': 'multiple'})
        )
    

class StorageForm(forms.Form):
    name = forms.CharField(label=u'Название')


class ObjUpdateForm(forms.Form):
    name = forms.CharField(label=u'Название')
    description = forms.CharField(label=u'Описание')
    storage = forms.ModelChoiceField(
        queryset=Storage.objects.all(),
        label=u'Место хранения',
        ) 
    category = TreeNodeChoiceField(
        queryset=Category.objects.all(), 
        label="Выберите категорию",
        )
    photos = forms.ImageField(
        label=u'Фотографии', 
        required=False,
        widget=forms.FileInput(attrs={'multiple': 'multiple'})
        )


class PicForm(forms.Form):
    photos = forms.ImageField(
        label=u'Фотографии',
        widget=forms.FileInput(attrs={'multiple': 'multiple'})
        )


class NewLoginForm(LoginForm):
    error_messages = {
        "account_inactive": "Этот аккаунт заблокирован",
        "email_password_mismatch": "Неверный email или пароль",
        "username_password_mismatch": "Неверный логин или пароль",
    }

    def login(self, *args, **kwargs):
        # Add your own processing here.

        # You must return the original result.
        return super(NewLoginForm, self).login(*args, **kwargs)


class NewSignupForm(SignupForm):
    error_messages = {  
        'password2': "Два пароля не совпадают",
    }
    def clean(self):
        cleaned_data = super(NewSignupForm, self).clean()

        return cleaned_data


