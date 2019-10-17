from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Home Page</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title" : "This is about us",
        "my_number" : 123,
        "my_list" : [1,12,123,'aa'],
        "my_html" : "<h1>my_html</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
