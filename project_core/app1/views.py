from django.shortcuts import render, redirect
from .forms import MetadataForm
from .tasks import add_metadata

def success_view(request):
    # Render a simple success message template
    return render(request, 'app1/success.html')

def submit_metadata(request):
    if request.method == 'POST':
        form = MetadataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            add_metadata.delay(name)  # Use delay to run the task asynchronously
            return redirect('success_url')
    else:
        form = MetadataForm()
    return render(request, 'app1/metadata_form.html', {'form': form})
