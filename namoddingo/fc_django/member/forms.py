from django import forms
from .models import Member
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleand_data = super().clean()
        email = cleand_data.get('email')
        password = cleand_data.get('password')
        re_password = cleand_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else :
                member = Member(
                    email = email,
                    password = make_password(password)
                )
                member.save()



class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleand_data = super().clean()
        email = cleand_data.get('email')
        password = cleand_data.get('password')

        if email and password:
            try:
                member = Member.objects.get(email=email)
            except Member.DoesNotExist:
                self.add_error('email','아이디가 없습니다.')
                return

            if not check_password(password, member.password):
                self.add_error('password','비밀번호를 틀렸습니다.')
            else:
                self.email = member.email
