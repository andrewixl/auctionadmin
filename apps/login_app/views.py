from django.shortcuts import render, redirect, HttpResponse
from models import User
from django.contrib import messages

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	return render(request, 'login_app/index.html')

def register(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	results = User.objects.registerVal(request.POST)
	if results['status'] == True:
		user = User.objects.createUser(request.POST)
		messages.success(request, 'User Registered! Please Log In.')
	else:
		genErrors(request, results['errors'])
	return redirect('/login')
def login(request):
	try:
		request.session['user_id']
		redirect("/")
	except KeyError:
		pass
	results = User.objects.loginVal(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/login')

	request.session['first_name'] = results['user'][0].first_name
	request.session['last_name'] = results['user'][0].last_name
	request.session['phone'] = results['user'][0].phone
	request.session['email'] = results['user'][0].email
	request.session['username'] = results['user'][0].username
	request.session['city'] = results['user'][0].city
	request.session['state'] = results['user'][0].state
	request.session['user_id'] = results['user'][0].id
	print request.session['user_id']
	return redirect('/')


def logout(request):
	request.session.flush()
	return redirect('/')
