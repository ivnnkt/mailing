from django.forms import ModelForm
from .models import Profile, Addressees

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mail_address',)


class AddresseesForm(ModelForm):

    class Meta:
        model = Addressees
        fields = ('first_name', 'last_name', 'email', 'group',)