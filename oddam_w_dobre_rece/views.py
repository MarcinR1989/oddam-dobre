from django.db.models import Count, Sum
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View

from oddam_w_dobre_rece.forms import UserRegistrationForm
from oddam_w_dobre_rece.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        donations_all = Donation.objects.all()
        bags_number = donations_all.aggregate(Sum('quantity'))
        institutions_number = donations_all.annotate(Count('institution_id', distinct=True))

        institutions_all = Institution.objects.all()
        institutions = institutions_all.filter(type='fundacja')
        institutions_local = institutions_all.filter(type='zbórka lokalna')
        institutions_nongovern = institutions_all.filter(type='organizacja pozarządowa')

        ctx = {
            'bags_number': bags_number['quantity__sum'],
            'institutions_number': institutions_number.count(),
            'institutions_local': institutions_local,
            'institutions_nongovern': institutions_nongovern,
            'institutions': institutions,
        }
        return render(request, "index.html", ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        ctx = {
            'user_form': user_form,
        }
        return render(request, "register.html", ctx)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.cleaned_data["first_name"]
            return HttpResponse(user)
            # return HttpResponse('Ojej...')
            pass
        user = user_form.cleaned_data["first_name"]
        return HttpResponse('Coś poszło nie tak...')
