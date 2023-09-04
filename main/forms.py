from django import forms
from .models import Article, Category, Comments

class ArticleForm(forms.ModelForm):

    new_tags = forms.CharField(max_length=255, required=False, help_text="Введите новые теги через запятую")

    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'author', 'category', 'image_url', 'tags']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'required': True}),
        }

