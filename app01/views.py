from django.shortcuts import render

# Create your views here.

from django import forms
from django.core.validators import RegexValidator

from app01.models import UserInfo


class RegisterModelForm(forms.ModelForm):
    mobile = forms.CharField(label="手机", validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码", )

    class Meta:
        model = UserInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入{}'.format(field.label)


def register(request):
    form = RegisterModelForm()
    return render(request, "register.html", {"form": form})
