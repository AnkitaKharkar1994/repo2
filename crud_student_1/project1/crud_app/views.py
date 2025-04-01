from django.shortcuts import render,redirect
from . forms import StudentModelForm
from.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def student_create_view(request):
    form=StudentModelForm()
    if request.method=="POST":
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrive')
    template_name='crud_app/student_form.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='signin')
def student_retirve_view(request):
    objs= Student.objects.all()
    template_name='crud_app/student_list.html'
    context={'data':objs}
    return render(request, template_name, context)

@login_required(login_url='signin')
def student_update_view(request, pk):
    obj=Student.objects.get(id=pk)
    form=StudentModelForm(instance=obj)
    if request.method=='POST':
        form=StudentModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('retrive')
    template_name='crud_app/student_form.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='signin')
def student_delete_view(request, pk):
    obj=Student.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('retrive')
    template_name='crud_app/delete_confirm.html'
    context={'data':obj}
    return render(request, template_name, context)