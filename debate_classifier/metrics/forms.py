from django import forms
from common.forms_util import get_topics_options, get_models_options


class GenerateSampleForm(forms.Form):
    filename = forms.CharField(max_length=25)
    topic = forms.ChoiceField(choices=get_topics_options())


class TopicClassificationForm(forms.Form):
    topic = forms.ChoiceField(choices=get_topics_options())
    model_name = forms.ChoiceField(choices=get_models_options())
