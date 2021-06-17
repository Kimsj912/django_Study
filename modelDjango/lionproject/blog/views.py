from django.shortcuts import render, redirect, get_object_or_404 # redirect를 써서 다시 이전 페이지로감.
from django.utils import timezone
from .models import  Blog
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})


def detail(request, id):
    #객체를 가져오거나 404를 리턴하게 함. #pk는 db기준의 값을 넣어줘야함.
    blog = get_object_or_404(Blog, pk=id) 
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form =BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid() :
        new_blog=form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id) 
    return redirect('home')

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date =timezone.now()
    update_blog.save() #save를 안하면 db에 적용이 안됨. 이건 꼭 해야함.
    return redirect('detail', update_blog.id) 

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete() # 삭제해주는 메소드
    return redirect('home')