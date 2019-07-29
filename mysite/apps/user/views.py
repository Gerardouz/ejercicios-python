from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm
from .models import User

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



def ConsultaUser(request):


	Users = User.objects.all()

	return render (request, 'user/consult_user.html', {'Users': Users})


def EditUser(request,id):

	User_Form = None
	error = None
	try:

		user = User.objects.get(id = id)

		if (request.method == 'GET'):
			User_Form = UserForm(instance = user)

		else:

			User_Form = UserForm(request.POST, instance = user)

			if (User_Form.is_valid()):

				User_Form.save()

			return redirect ('index')

		

	except ObjectDoesNotExist as e:

		error = e


	return render(request, 'user/user.html', {'User_Form': User_Form, 'error':error})



def ElimUser(request,id):


	user = User.objects.get(id = id)

	if(request.method == 'POST'):

		user.delete()
		return redirect('user:consult_user')

	return render(request, 'user/elim_user.html',{'user':user})