from django.shortcuts import render
import re


def input_string(request):
    l=[]
    if request.method == "POST":
        string = request.POST.get('string')
        print(string)
        l = re.findall("[6-9][\d]{9}", string)

    return render(request, "index.html", {"result": l})

# Create your views here.
