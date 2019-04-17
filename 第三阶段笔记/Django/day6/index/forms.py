from django import forms
from .models import *

#为topic下拉列表初始化一组数据 - 元组
#('level1','好评')等同于<option value='level1'>好评</option>
TOPIC_CHOICE=(
    ('level1','好评'),
    ('level2','中评'),
    ('level3','差评'),
    )

class RemarkForm(forms.Form):
    #创建subject属性，表示评论的标题，显示成文本框
    #labe 生成的控件其那面的提示文本
    #initial表示初始化的数据，等同于空间的value
    subject=forms.CharField(label='标题',initial='初始数据')
    #创建一个email属性,表示邮箱，显示成email控件
    #label表示控件前面的文本
    email=forms.EmailField(label='邮箱')
    #创建一个message属性，表示评论内容，显示成多行文本域
    #label表示空间前面的文本
    #让当前控件变成一个多行文本域
    message=forms.CharField(label='内容',widget=forms.Textarea)
    #创建topic属性，表示评论级别，显示成一个下拉列表
    #choices:指定下拉列表选项的数据们
    topic=forms.ChoiceField(label='评价',choices=TOPIC_CHOICE)
    #创建isSave属性，表示是否保存，显示成一个复选框
    isSave=forms.BooleanField(label='是否保存')

class RegisterForm(forms.Form):
    uname=forms.CharField(label='用户名字',widget=forms.TextInput(
            attrs={
                'placeholder':'请输入用户名',
                'class':'form-control'
            }
        ))
    upwd=forms.CharField(label='用户密码',widget=forms.PasswordInput(
            attrs={
                'placeholder':'请输入密码',
                'class':'form-control',
            }
        ))
    uemail=forms.CharField(label="电子邮箱",widget=forms.EmailInput)
    uage=forms.CharField(label="用户年龄",widget=forms.NumberInput)

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields="__all__"
#         labels={
#             'uname':'用户名称',
#             'upwd':'用户密码',
#             'uemail':'用户邮箱',
#             'uage':'用户年龄',
#         }

class LoginForm(forms.ModelForm):
    #创建内部类Meta
    class Meta:
        #关联的Models
        model=User
        #定义要生成的属性们
        # fields="__all__"
        fields=['uname','upwd']
        #每个控件对应的label
        labels={
            'uname':'用户名称',
            'upwd':'用户密码',
        }
        widgets={
        'uname':forms.TextInput(
            attrs={
            'placeholder':'用户名称',
            'class':'form-control',
            }
        ),
        'upwd':forms.PasswordInput(
            attrs={
            'placeholder':'用户密码',
            'class':'form-control'
            }
        )

        }
