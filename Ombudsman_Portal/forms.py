from django.forms import ModelForm, TimeInput, DateInput
from . import models


class OmbudsmanForm(ModelForm):
    class Meta:
        model = models.OmbudsmanPortalForm
        fields = [
            'fm_name',
            'fm_email',
            'fm_phone',
            'fm_type_complaint',
            'fm_complaint_description',
            'fm_complaint_datetime',
            'fm_status_complaint',
        ]