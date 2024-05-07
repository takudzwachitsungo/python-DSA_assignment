from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import MyRecordForm

def create_record(request):
    if request.method == 'POST':
        form = MyRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_created')  # Redirect to a success page
    else:
        form = MyRecordForm()
    return render(request, 'myapp/create_record.html', {'form': form})

