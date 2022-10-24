from django.shortcuts import render
from django.http import HttpResponse



kkk =  [
{
    'id':1,
    'title' : "E-commerce website",
    'description' : 'E commerce telling '
},
    {
    'id':2,
    'title' : "Profolio website",
    'description' : 'Profolio telling '
},
    {
    'id':3,
    'title' : "Social network website",
    'description' : 'Social network telling '
}
]

def projects(request):
    page = 'projects'
    number =10
    context = {'page':page,'number':number,'projects':kkk}
    return render(request,'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in kkk:
        if str(i['id']) == pk:
            projectObj=i

    return render(request,'projects/singles-projects.html',{'project':projectObj})

