from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def service(request):
    return render(request, 'core/service.html')

def blog(request):
    return render(request, 'core/blog.html')

def blog_details(request):
    return render(request, 'core/blog_details.html')