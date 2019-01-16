from django.shortcuts import render
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'base/index.html',
                          {'new_user': new_user})
    else:
        form = UserRegistrationForm(initial={'email': 'pupkin@com'}, )

    return render(request, 'user_profile/registration_form.html', {'form': form})
