from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=64, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'content': 'Message'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'my-2'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
