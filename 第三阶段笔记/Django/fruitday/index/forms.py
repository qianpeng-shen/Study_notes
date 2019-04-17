from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['uphone','upwd']
        labels={
            'uphone':'手机号',
            'upwd':'密码',
        }
        widgets={
            'uphone':forms.TextInput(
                    attrs={
                    'class':'form-control'
                    }
                ),
            'upwd':forms.PasswordInput(
                    attrs={
                        'placeholder':'请输入6-20位好号码',
                        'class':'form-control',
                    }
                )
        }