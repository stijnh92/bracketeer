from django.forms import inlineformset_factory, ModelForm
from django.forms.models import BaseInlineFormSet

from bracket.models import BracketItem
from nba.models import MatchUp


class MatchUpForm(ModelForm):
    class Meta:
        model = MatchUp
        fields = ['home_team', 'away_team', 'home_score', 'away_score']


class BaseMatchUpFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseMatchUpFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = MatchUpForm()

    def is_valid(self):
        result = super(BaseMatchUpFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result


BracketItemFormSet = inlineformset_factory(MatchUp, BracketItem, exclude=[], extra=1, formset=BaseMatchUpFormset)
