from django.shortcuts import render,redirect,get_object_or_404
from .forms import comForm
from .models import com
# Create your views here.
def WT(request):
    return render(request, 'comments/WT.html', {})

def horror(request):
    if request.method == "POST":
        form = comForm(request.POST)
        com = form.save(commit=False)
        com.save()
        return redirect('horror')
    else:
        form = comForm()
    return render(request, 'comments/horror.html', {'form':form})

def scifi(request):
    if request.method == "POST":
        form = comForm(request.POST)
        com = form.save(commit=False)
        com.save()
        return redirect('scifi')
    else:
        form = comForm()
    
    return render(request, 'comments/scifi.html', {'form':form})

def crime(request):
    if request.method == "POST":
        form = comForm(request.POST)
        com = form.save(commit=False)
        com.save()
        return redirect('crime')
    else:
        form = comForm()
    return render(request, 'comments/crime.html', {'form':form})

def comm(request):
    comm=com.objects.all()
    return render(request, 'comments/comment.html',{'comm':comm})