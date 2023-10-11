from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms
from .forms import ThingsForm
from django.shortcuts import render



#FORM_NUM = 1      # フォーム数
#FORM_VALUES = {}#保存
FORM_NUM=1
FORM_VALUES= {}

# Create your views here.
class IndexView(FormView):

    template_name = 'Kanemi/index.html'
    success_url = reverse_lazy('index')
    ThingsFormSet = forms.formset_factory(
        form=ThingsForm,
        extra=1,
        max_num=10,
    )
    form_class = ThingsFormSet
    
    def get_form_kwargs(self):
        # デフォルトのget_form_kwargsメソッドを呼び出す
        kwargs = super().get_form_kwargs()
        # FORM_VALUESが空でない場合（入力中のフォームがある場合）、dataキーにFORM_VALUESを設定
        if FORM_VALUES and 'btn_add' in FORM_VALUES:
            kwargs['data'] = FORM_VALUES
        return kwargs
    
    def post(self, request, *args, **kwargs):
        global FORM_NUM
        global FORM_VALUES
        # 追加ボタンが押された時の挙動
        if 'btn_add' in request.POST:
            FORM_NUM += 1    # フォーム数をインクリメント
            FORM_VALUES = request.POST.copy()  # リクエストの内容をコピー
            FORM_VALUES['form-TOTAL_FORMS'] = FORM_NUM   # フォーム数を上書き
        
        elif 'btn_submit' in request.POST:
            formset = self.get_form()
            if formset.is_valid():
                total_prices = {}  # 商品ごとの合計金額を保持する辞書
                all_total = 0  # 全商品の合計金額
                for form in formset:
                    if form.cleaned_data.get('name'):
                        name = form.cleaned_data.get('name')
                        price = form.cleaned_data.get('price') or 0  # 単品価格が入力されていない場合は0として計算
                        amount = form.cleaned_data.get('amount') or 0  # 数量が入力されていない場合は0として計算
                        total = price * amount
                        total_prices[name] = total_prices.get(name, 0) + total
                        all_total += total

            # 合計金額をテンプレートに渡す
                return self.render_to_response(self.get_context_data(formset=formset, total_prices=total_prices, all_total=all_total))
        
        return super().post(request, args, kwargs)

def my_view(request):
    return render(request, 'myapp/mytemplate.html', {})

