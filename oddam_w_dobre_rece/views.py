from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login as auth_login

# Create your views here.
from django.views import View
from django.views.generic import CreateView, FormView

from oddam_w_dobre_rece.forms import *
from oddam_w_dobre_rece.models import Donation, Institution, CustomUser


def validate_username(request):
    username = request.GET.get('username', None)
    kapcie = request.GET.get('kapcie', None)
    # data = {
    #     'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    # }
    # if data['is_taken']:
    #     data['error_message'] = 'A user with this username already exists.'

    print(username)
    print(kapcie)
    return JsonResponse({'morska bryza': 'morska bryza'})


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


class AddDonationView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        form = DonationForm()
        donation = Donation.objects.all()
        institution = Institution.objects.all()
        categories = Category.objects.all()
        ctx = {
            'form': form,
            'donation': donation,
            'institution': institution,
            'categories': categories,
        }
        return render(request, "form.html", ctx)

    def post(self, request):
        # categories = [category for category in request.POST['categories']],
        # test = request.POST['test']
        user = CustomUser.objects.get(username=request.user.username)
        if request.is_ajax():
            form = DonationForm(request.POST)
            form1 = request.POST
            if form.is_valid():
                form.save()
                print('UDAŁO SIĘ ZAPISAĆ MODEL!', form1)
            else:
                # bags = request.POST['bags']
                print('NIE UDAŁO SIĘ ZAPISAĆ MODELU...', form1)
            # institution = Institution.objects.get(name=request.POST['institution'])
            # gifts = request.POST['gifts']
            # bags = request.POST['bags']
            # address = request.POST['address']
            # city = request.POST['city']
            # postcode = request.POST['postcode']
            # phone = request.POST['phone']
            # data = request.POST['data']
            # time = request.POST['time']
            # more_info = request.POST['more_info']
            # kwargs = {
            #     'quantity': request.POST['bags'],
            #     'institution': institution,
            #     'address': request.POST['address'],
            #     'city': request.POST['city'],
            #     'zip_code': request.POST['postcode'],
            #     'phone_number': request.POST['phone'],
            #     'pick_up_date': request.POST['data'],
            #     'pick_up_time': request.POST['time'],
            #     'pick_up_comment': request.POST['more_info'],
            #     'user': request.user
            # }
            # print(gifts)
            # print(bags)
            # print(address)
            # print(city)
            # print(postcode)
            # print(phone)
            # print(data)
            # print(time)
            # print(more_info)
            print(user)
            # print(test)
            # Donation.objects.create(**kwargs)
            return redirect('confirm-donation')
        else:
            HttpResponse('error')


class ConfirmDonationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


# class AddDonationView(LoginRequiredMixin, CreateView):
#     login_url = '/login'
#     template_name = 'form.html'
#     form_class = DonationForm


# LOGIN JEST WYŚWIETLANY I OBSŁUGIWANY PRZEZ WBUDOWANE W DJANGO URLe
# PATRZ "url.py"
# class LoginView(View):
#     def get(self, request):
#         return render(request, "registration/login.html")


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        ctx = {
            'form': form,
        }
        return render(request, "register.html", ctx)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect('login')
        raise Http404("Something went terribly wrong...")

# class RegisterView(CreateView):
#     template_name = 'register.html'
#     form_class = UserRegistrationForm
#     success_url = '/login'
