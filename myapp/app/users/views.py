from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, ProfileFirstUpdateForm
from .models import Profile 
from django.contrib.auth.decorators import login_required



@login_required
def profileupdateview(request):
	if request.method == 'POST':
		profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('mainapp:your-account')
	else:
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	return render(request, 'mainapp/youraccount-update.html', {'profile_form':profile_form})

@login_required
def profilefirstupdateview(request):
		if request.method == 'POST':
			form = ProfileFirstUpdateForm(request.POST, request.FILES)
			if form.is_valid():
				bell = form.save(commit=False)
				bell.user = request.user
				bell.save()
				return redirect('mainapp:your-account')
		else:
			form = ProfileFirstUpdateForm()

		context = {
			'form':form
		}
		return render(request, 'mainapp/youraccount-firstupdate.html', context)
