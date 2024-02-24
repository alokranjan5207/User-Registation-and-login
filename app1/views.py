from django.shortcuts import render

# Create your views here.
def user_registation(request):
    return render(request=request,template_name='registation.html')