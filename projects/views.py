from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# views 裡面的所有內容 都會導航(render)到相對印的html黨 而後面的context 是傳道html黨的內容 (用python字典傳)

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)
    

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/singles-projects.html',{'project':projectObj})


# CRUD stands for create, read, update, delete


#if else 操作也是寫在view裡面
def createProject(request):
    form = ProjectForm()
    context={'form':form}

    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request,"projects/project_form.html",context) 


#if else 操作也是寫在view裡面

def updateProject(request,pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context={'form':form}

    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request,"projects/project_form.html",context) 


#if else 操作也是寫在view裡面
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context={'object':project}
    return render(request,'projects/delete_template.html',context)