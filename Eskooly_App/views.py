from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django .contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView,ListView,DeleteView
from django.utils.decorators import method_decorator
from Eskooly_App.forms import Classes_form
from Eskooly_App.models import Classes
from django.urls import reverse
# Create your views here.
def loginview(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('adminview')
        else:
            messages.info(request,'Username or Password is Incorrect')


    return render(request, 'Eskooly_App/login.html')
@login_required(login_url='login')
def adminview(request):
    return render(request, 'Eskooly_App/adminview.html')
def logoutview(request):
    logout(request)
    return redirect('login')

def Classes_Entry(request):
    Classes_entry = Classes_form()
    class_dict={'Classes_entry':Classes_entry}
    if request.method=='POST':
        Classes_entry = Classes_form(request.POST,request.FILES)
        if Classes_entry.is_valid():
            data = Classes_entry.save(commit=False)
            data.save()
            class_dict.update({'msg':'Class Added Successfully'})
            return redirect('allclass')
    return render(request,'Eskooly_App/Add_class.html',context=class_dict)

class All_Classes(ListView):
    model = Classes
    fields = '__all__'
    context_object_name = 'class_list'
    template_name = 'Eskooly_App/All_Class.html'

class Edit_class(ListView):
    model = Classes
    context_object_name = 'class_list'
    template_name = 'Eskooly_App/editdelete.html'

class DeleteClass(DeleteView):
    model = Classes
    context_object_name = 'class_list'
    template_name = 'Eskooly_App/confirmdelete.html'
    def get_success_url(self):
        return reverse('allclass')

class UpdateClass(UpdateView):
    model = Classes
    fields = '__all__'

class Addclass(CreateView):
    model = Classes
    fields = '__all__'
    context_object_name = 'class_list'
    template_name = 'Eskooly_App/Add_class.html'
    def get_success_url(self):
        return reverse('allclass')
