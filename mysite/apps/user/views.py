from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.


def Home(request):

	return render(request,'index.html')

def CrearUser(request):

	if(request.method == 'POST'):

		User_Form = UserForm(request.POST)

		if (User_Form.is_valid()):

			User_Form.save()

			return redirect('index')

	else:
		
		User_Form = UserForm()
		
	return render(request, 'user/user.html', {'User_Form': User_Form})