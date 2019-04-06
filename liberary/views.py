from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import View
from .models import Book_Detail, Category_Table, Borrower_Detail, Student_Detail, Staff_Detail, Shelf_Detail, Language_Table
from .forms import StudentForm, Student_DetailForm

# Create your views here.

def index(request):
	try:
		categories = Category_Table.objects.all()
		languages = Language_Table.objects.all()
		context = {'languages': languages, 'categories': categories}
		return render(request, 'liberary/index.html', context)
	except Category_Table.DoesNotExist or Language_Table.DoesNotExist :
		raise Http404("Content does not exist")

def book_list_by_category(request, id):
	try:
		books = Book_Detail.objects.filter(category_id=id)
		categories = Category_Table.objects.all()
		languages = Language_Table.objects.all()
		context = {'languages': languages, 'categories': categories, 'books': books}
		return render(request, 'liberary/book_list.html', context)
	except Book_Detail.DoesNotExist :
		raise Http404("Books does not exist")

def book_list_by_language(request, id):
	try:
		books = Book_Detail.objects.filter(language_id=id)
		categories = Category_Table.objects.all()
		languages = Language_Table.objects.all()
		context = {'languages': languages, 'categories': categories, 'books': books}
		return render(request, 'liberary/book_list.html', context)
	except Book_Detail.DoesNotExist :
		raise Http404("Books does not exist")

def book_details(request, id):
	try :
		book = Book_Detail.objects.get(ISBN=id)
		categories = Category_Table.objects.all()
		languages = Language_Table.objects.all()
		context = {'languages': languages, 'categories': categories, 'book': book}
		return render(request, 'liberary/book_details.html', context)
	except Book_Detail.DoesNotExist :
		raise Http404("Books does not exist")

class UserFormView(View):
	form_class1 = StudentForm
	form_class2 = Student_DetailForm
	template_name = 'liberary/registration_form.html'

	def get(self, request):
		context = {'form' : self.form_class1(None), 'form2' : self.form_class2(None)}
		return render(request, self.template_name, context)

	def post(self, request):
		context = {'form': self.form_class1(request.POST), 'form2': self.form_class2(request.POST)}

		if context['form'].is_valid():
			user = context['form'].save(commit=False)

			username = context['form'].cleaned_data['username']
			password = context['form'].cleaned_data['password']
			user.set_password(password)
			user.save()
			context['form2'].save()
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('liberary:index')

		return render(request, self.template_name, context)

class Book_detailCreate(CreateView):
	model = Book_Detail
	fields = ['ISBN', 'book_title', 'author', 'publisher', 'publication_date', 'language_id', 'category_id', 'online', 'no_of_copies_available_offline', 'shelf_id']
	template_name = 'liberary/book_form.html'

