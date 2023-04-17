# accounts/forms.py


# 회원가입 폼 CustomUserCreationForm
# 폼 이름 : CustomUserCreationForm
# 클래스 상속 : UserCreationForm
# 필드
# username
# email
# first_name
# last_name
# password1
# password2

# 회원 정보 수정 폼 CustomUserChangeForm
# 폼 이름 : CustomUserChangeForm
# 클래스 상속 : UserChangeForm
# 필드
# email
# first_name
# last_name
from django import forms  # 추가
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User


class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(label='생년월일', required=False, widget=forms.DateInput(
        attrs={'type': 'date'}))  # 추가

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'birthday', 'email', 'first_name',
                  'last_name', 'password1', 'password2',)

# class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = get_user_model()
#        fields = ('username', 'email', 'first_name', 'last_name')

        # fields = ('username', 'email', 'first_name', 'last_name','birthday', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    birthday = forms.DateField(label='생년월일', required=False, widget=forms.DateInput(
        attrs={'type': 'date'}))  # 추가

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('birthday', 'email', 'first_name', 'last_name',)
        # fields = ('username','email', 'first_name', 'last_name','birthday','password1','password2',)
