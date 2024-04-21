from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def clean_name(self):

        cleaned_data = self.cleaned_data["name"]
        ban_words = [
            "казино",
            "криптовалюса",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in ban_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Запрещенное название продукта")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        ban_words = [
            "казино",
            "криптовалюса",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in ban_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Запрещенное описание продукта")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('ver_name',)
