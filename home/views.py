from django.shortcuts import render,HttpResponse
from home.models import blogs

# Create your views here.
def index(request):
    post = blogs.objects.all()
    return render(request,"index.html",{'posts' : post})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title1')
        blogBody = request.POST.get('blogBody')
        blogss = blogs(title=title,dec=blogBody)
        blogss.save()
    return render(request,"add.html")

def post(request,pk):
    posts = blogs.objects.get(id = pk)
    return render(request,"post.html",{"posts" : posts})