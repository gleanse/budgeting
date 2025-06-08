from django.shortcuts import render

# FOR /  HOME OF DJANGO URL
def home_page(request):
    return render(request, 'home.html')