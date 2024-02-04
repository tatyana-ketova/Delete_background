from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .remove_background import remove_back
import tempfile
from django.http import HttpResponse


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_obj = form.instance
            threshold = form.cleaned_data['threshold']
            image_without_back = remove_back(image_obj, threshold)

            # create file without background
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                image_without_back.save(tmp_file.name, format='PNG')

            # sent files for downloading
            with open(tmp_file.name, 'rb') as file:
                response = HttpResponse(file.read(), content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="image_without_back.png"'
                return response
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})
