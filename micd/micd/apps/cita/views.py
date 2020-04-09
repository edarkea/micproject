from django.shortcuts import render

# Create your views here.
def cita_form(request):
    return render(request, 'cita_form.html', {})
