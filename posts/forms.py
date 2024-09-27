from django import forms
from .models import Post
from products.models import Product

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'product', 'content'
                  'image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        image = forms.ImageField(label='Image', required=False,)

        product = forms.ModelChoiceField(
        queryset=Product.objects.filter(tags__contains="coffee"),
        blank=True, to_field_name="name")

        self.fields['product'].label = "SouthRoast"