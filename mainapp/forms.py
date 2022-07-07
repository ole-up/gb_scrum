from django.forms import ModelForm, TextInput, CharField, IntegerField, NumberInput

from mainapp.models import Comment, Article


class CommentForm(ModelForm):
    parent_path = CharField(required=False)
    article_id = IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ('author', 'comment_body')
        widgets = {
            'comment_body': TextInput(),
            'parent_path': TextInput(),
            'article_id ': NumberInput()
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['parent_path'].widget.attrs['class'] = 'hidden'
        self.fields['article_id'].widget.attrs['class'] = 'hidden'
        self.fields['author'].widget.attrs['class'] = 'hidden'

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.path = f'{self.cleaned_data["parent_path"]}'
        comment.level = comment.path.count('.')
        comment.article = Article.objects.get(id=self.cleaned_data["article_id"])
        if commit:
            comment.save()
            comment.path = f'{self.cleaned_data["parent_path"]}.{str(comment.pk).zfill(9)}' if self.cleaned_data[
                'parent_path'] else str(comment.pk).zfill(9)
            comment.level = comment.path.count('.')
            comment.save()
        return comment
