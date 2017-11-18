from django import  forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class formdangki(forms.Form):
    tentk=forms.CharField(label='taikhoan',max_length=30)
    matkhau1 = forms.CharField(label='Matkhau', widget=forms.PasswordInput())
    matkhau2 = forms.CharField(label='Nhaplaimatkhau', widget=forms.PasswordInput())

    def kiemtramatkhau(self):
        if 'matkhau1' in self.cleaned_data:
            matkhau1 = self.cleaned_data['matkhau1']
            matkhau2 = self.cleaned_data['matkhau2']
            if matkhau1 == matkhau2:
                return matkhau2
        raise forms.ValidationError('Nhập lại mật khẩu')

    def kiemtratk(self):
        tentk = self.cleaned_data['tentk']
        if not re.search(r'^\w+$', tentk):
            raise forms.ValidationError('Tên tài khoản khong hợp lệ')
        try:
            User.objects.get(username=tentk)
        except ObjectDoesNotExist:
            return tentk
        raise forms.ValidationError('Tài khoản đã tồn tại')