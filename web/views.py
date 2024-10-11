from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from web.forms import PostForm
from web.models import Post


# Handling form
def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Image')
            return redirect('web:index')  # Redirect to index view after successful upload
        else:
            messages.error(request, 'Failed to upload image. Please try again.')  # Error message
    else:
        form = PostForm()
    return render(request, 'index.html', {'form': form})  


# Displaying content
def index(request):
    pictures = Post.objects.all()
    return render(request, 'home.html', {'pictures': pictures})
