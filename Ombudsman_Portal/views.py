from django.shortcuts import render, redirect
from django.views.generic import FormView
from . import forms

# Create your views here.
class OmbudsmanPForm(FormView):
    #permission_required = 'app.can_view_schedule'
    form_class = forms.OmbudsmanForm
    template_name = 'Ombudsman_Portal/OmbudsmanPortal.html'
    success_url = 'OmbudsmanPortal'

    def form_valid(self, form):
        ombudsman_form = form.save(commit=False)
        if form.is_valid():
            ombudsman_form.save()
            return redirect('OmbudsmanPortal')
        return super().form_invalid(form)

    def form_invalid(self, form):
        if not form.is_valid():
            return redirect('OmbudsmanPortal')
        return self.render_to_response(self.get_context_data(form=form))

