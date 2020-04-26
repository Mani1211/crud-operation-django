from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .form import PostForm

# Create your views here.



def index(request):
    return render(request,'index.html')
    
def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.desc =  request.POST['desc']
        post.price = request.POST['price']
        post.save()

        post = Post.objects.all()
        return render(request,'main.html',{'post':post})
    else:
        post = Post.objects.all()
        return render(request,'main.html',{'post':post})

def update(request,pk):
  
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        return render(request,'update.html',{'form':form})
    

def delete(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    post = Post.objects.all()
    return redirect('/create')

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'post':post})

