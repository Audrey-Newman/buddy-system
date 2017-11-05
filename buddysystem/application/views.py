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
        ready_form = ReadyForm(request.POST)
        male_form = MaleForm(request.POST)
        if ready_form.is_valid():
            u = request.user
            u.refresh_from_db()
            u.profile.dep_location = ready_form.cleaned_data.get('dep_location')
            u.profile.destination = ready_form.cleaned_data.get('destination')
            u.save()
            return redirect('waiting')
        if male_form.is_valid():
            u_m = request.user
            u_m.refresh_from_db()
            u_m.profile.desired_companions = male_form.cleaned_data.get('companions')
            u_m.save()
            return redirect('waiting')
        if female_form.is_valid():
            u_f = request.user
            u_f.refresh_from_db()
            u_f.profile.desired_companions = female_form.cleaned_data.get('companions')
            u_f.save()
            return redirect('waiting')
        if other_form.is_valid():
            u_o = request.user
            u_o.refresh_from_db()
            u_o.profile.desired_companions = other_form.cleaned_data.get('companions')
            u_o.save()
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
    if u.is_authenticated():
        return render(request, 'waiting.html', {'place': request.user.profile.dep_location, 'profile_list': Profile.objects.filter(dep_location=request.user.profile.dep_location).filter(destination=request.user.profile.destination)})
    return render(request, 'waiting.html', {'place': "nothing", 'profile_list': "nothing"})
