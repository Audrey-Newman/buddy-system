from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import ReadyForm
from .forms import MaleForm
from .forms import FemaleForm
from .forms import OtherForm
from .models import Profile
from django.views import generic

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
#logger.error(message)

def index(request):
    """
    View function for home page of site.
    """
    if request.method == 'POST':
        req = request.POST
        ready_form = ReadyForm(req)
        male_form = MaleForm(req)
        female_form = FemaleForm(req)
        other_form = OtherForm(req)
        u = request.user

        male_is_valid = male_form.is_valid()

        if ready_form.is_valid():
            u.refresh_from_db()
            u.profile.dep_location = ready_form.cleaned_data.get('dep_location')
            u.profile.destination = ready_form.cleaned_data.get('destination')
            u.profile.num_companions = ready_form.cleaned_data.get('num_companions')
            u.save()

        if male_form.is_valid():
            u.refresh_from_db()
            u.profile.desired_companions = male_form.cleaned_data.get('companions')
            u.save()

        if female_form.is_valid():
            u.refresh_from_db()
            u.profile.desired_companions = female_form.cleaned_data.get('companions')
            u.save()

        if other_form.is_valid():
            u.refresh_from_db()
            u.profile.desired_companions = other_form.cleaned_data.get('companions')
            u.save()

            return redirect('waiting')

    else:
        ready_form = ReadyForm()
        male_form = MaleForm()
        female_form = FemaleForm()
        other_form = OtherForm()
    return render(request, 'index.html', {'form': ready_form, 'femaleform': female_form, 'maleform': male_form, 'otherform': other_form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.dep_location = 'none'
            user.profile.destination = 'none'
            user.profile.score = '0'
            user.profile.firstname = form.cleaned_data.get('firstname')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def waiting(request):
    u = request.user
    u.refresh_from_db()
    # check if conditions are met
    profile_list = Profile.objects.filter(dep_location=u.profile.dep_location).filter(destination=u.profile.destination)
    profile_list_women = profile_list.filter(gender='Female')
    profile_list_men = profile_list.filter(gender='Male')

    if(u.profile.desired_companions == 'only women'):
        profile_list = profile_list_women
    else:
        profile_list = profile_list_men

    conditions_met = True
    if(u.profile.num_companions == '> 2' and (profile_list.__len__() <= 2)):
        conditions_met = False

    if u.is_authenticated():
        return render(request, 'waiting.html', {'place': request.user.profile.dep_location,
                                'profile_list': profile_list,
                                'conditions_met': conditions_met})
    return render(request, 'waiting.html', {})

def goodnight(request):
    u = request.user
    u.refresh_from_db()
    u.profile.dep_location = "none"
    u.profile.destination = "none"

    return render(request, 'goodnight.html', {})

def ontheway(request):
    return render(request, 'ontheway.html', {})
