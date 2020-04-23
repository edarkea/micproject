from django.shortcuts import render
from django.views.generic import TemplateView
from micd.micd.apps.cita.forms import ContactForm
from django.shortcuts import redirect

# Create your views here.
class ContactView(TemplateView):
    template_name = 'cita_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        
        return context

    def post(self, request, *args, **kwargs):
        return redirect('create_cita')