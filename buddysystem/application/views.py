from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import ReadyForm
from .models import Profile

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
#logger.error(message)

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.dep_location = 'none'
            user.profile.destination = 'none'
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def ready(request):
    if request.method == 'POST':
        form = ReadyForm(request.POST)
        if form.is_valid():
            u = request.user
            u.refresh_from_db()
            #form.save()
            u.profile.dep_location = form.cleaned_data.get('dep_location')
            u.profile.destination = form.cleaned_data.get('destination')
            u.save()
            return redirect('index')
    else:
        form = ReadyForm()
    return render(request, 'ready.html', {'form': form}) # replace ready.html with index when sarah's done
