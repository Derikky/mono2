from django import forms
from django.forms import ModelForm, BaseModelFormSet, modelformset_factory
from .models import Things


class ThingsForm(forms.ModelForm):
    class Meta:
        model= Things
        fields = '__all__'
        labels = {'name':'商品名', 'price': '単品価格', 'amount':'数量'}
        
    
#class BaseThingsFormSet(BaseModelFormSet):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        # 初期値を設定する
#        self.queryset = Memo.objects.filter(title__startswith=title)

#ThingsFormSet = modelformset_factory(Things, Form=ThingsForm, formset=BaseThingsFormSet)

