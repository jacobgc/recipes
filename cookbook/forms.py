from django.utils.translation import gettext as _
from django import forms
from .models import *
from django.forms import widgets


class MultiSelectWidget(widgets.SelectMultiple):
    class Media:
        js = ('custom/js/form_multiselect.js',)


class EmojiWidget(forms.TextInput):
    class Media:
        js = ('custom/js/form_emoji.js',)
        # TODO add class to input fields so there is no longer a static reference to #id_icon in the js but a class based like in multiselect
        

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'keywords', 'path')

        labels = {
            'name': _('Name'),
            'category': _('Category'),
            'keywords': _('Keywords'),
            'path': _('Path'),
        }
        widgets = {'keywords': MultiSelectWidget}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'icon', 'description')
        widgets = {'icon': EmojiWidget}


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ('name', 'icon', 'description')
        widgets = {'icon': EmojiWidget}


class MonitorForm(forms.Form):
    path = forms.CharField(label=_('Path'))


class BatchEditForm(forms.Form):
    search = forms.CharField(label=_('Search String'))
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('id'), required=False)
    keywords = forms.ModelMultipleChoiceField(queryset=Keyword.objects.all().order_by('id'), required=False)

    class Media:
        js = ('custom/js/form_multiselect.js',)


class ImportRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'keywords', 'path')

        labels = {
            'name': _('Name'),
            'category': _('Category'),
            'keywords': _('Keywords'),
            'path': _('Path'),
        }
        widgets = {'keywords': MultiSelectWidget}
