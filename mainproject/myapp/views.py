from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def CalAdd(request):
    value_a = int(request.POST['valueA'])
    value_b = int(request.POST['valueB'])
    result = value_a + value_b
    return render(request,'cal.html',{'result':result})
    print(value_a,value_b , value_a+value_b)
