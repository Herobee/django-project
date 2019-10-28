from django.shortcuts import render
from django.views import View

# BASE VIEW Class = VIEW

class CourseView(View):
    def get(self, reqeust, *args, **kwargs):
        return render(request, 'about.html', {})

    # def post(reqeust, *args, **kwargs):
    #     return render(request, 'about.html', {})
# HTTP METHODS
def my_fbv(reqeust, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})