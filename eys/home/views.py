from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from home.models import Setting

from home.models import ContactFormu
from home.models import ContactFormMessage


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {"setting": setting, 'page': 'home'}  # indexe gönderildi
    return render(request, "index.html", context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {"setting": setting, 'page': 'hakkimizda'}  # indexe gönderildi
    return render(request, "hakkimizda.html", context)


def iletisim(request):

    if request.method == "POST":
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kurmak için
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.subject = form.cleaned_data['subject']
            data.save()
            messages.success(request,
                            'Mesaj başarı ile gönderilmiştir. Geri dönüş maili en kısa sürede tarafınıza iletilecektir.')
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {"setting": setting, "form": form }  # indexe gönderildi
    return render(request, "iletisim.html", context)
