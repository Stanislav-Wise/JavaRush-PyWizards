from django import forms
from django.core.exceptions import ValidationError
from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=10,
        label='Заголовок',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Введите заголовок'}
        )
    )

    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Введите содержание поста',
                   'rows': 5}
        )
    )

    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Рейтинг',
        widget=forms.NumberInput(
            attrs={'class': 'form-control',}
        )

    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'rating', 'tags', 'image']
        labels = {
            'author': 'Автор',
            'title': 'Заголовок',
            'content': 'Контент',
            'rating': 'Рейтинг',
            'tags': 'Тэги',
            'image': 'Изображение',
        }
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание поста', 'rows': 5}),
            'rating': forms.NumberInput(attrs={'class': 'form-control',}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control',}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control',}),
        }
        help_texts = {
            'tags': 'Выберите тэги, подходящие к вашему посту'
        }

    def clean_title(self):
        """Кастомная валидация заголовка."""
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть  5 или более симовлов')
        return title

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 100:
            raise ValidationError("Рейтинг не может быть отрицательным или больше 100")
        return rating

    def clean(self):
        cleaned_data =  super().clean()
        content = cleaned_data.get('content')
        title = cleaned_data.get('title')

        FORBIDDEN_WORDS = ['крипта', 'казино']

        if content or title:
            for word in FORBIDDEN_WORDS:
                if word in content.lower():
                    raise ValidationError(f'Контент не должен содержать слово: "{word}" ')
                if word in title.lower():
                    raise ValidationError(f'Заголовок не должен содержать слово: "{word}" ')


class PostDeleteForm(forms.Form):
    """Форма дляподтверждения удаления поста."""
    confirm = forms.BooleanField(
        required=True,
        label='Подтвердите удаление',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )