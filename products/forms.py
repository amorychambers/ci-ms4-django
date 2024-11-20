from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=True,)

    def __init__(self, *args, **kwargs):
        """
        Add mininum value for product quantity
        """
        super().__init__(*args, **kwargs)

        self.fields['price'].widget.attrs['min'] = 0
        self.fields['stock'].widget.attrs['min'] = 0
