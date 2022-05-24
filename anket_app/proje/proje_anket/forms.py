from django.forms import ModelForm

from .models import Cevaplar, User

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['userName','userNo']
class CreateCevaplarForm(ModelForm):
    class Meta:
        model = Cevaplar
        fields = ['user_id','sinif','ortalama','katilim_derecesi','hitap_eden','hakim_misin','dusunur_musun','ing_duzey']


