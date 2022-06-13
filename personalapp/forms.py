from django.forms import ModelForm, ImageField, FileInput
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from mainapp.models import Habr


class ArticleForm(ModelForm):
    description = SummernoteTextField()
    image = ImageField(widget=FileInput(), required=True)

    class Meta:
        model = Habr
        fields = ('category', 'image', 'name', 'short_desc', 'description')
        widgets = {
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '600px'}}),
                 }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
