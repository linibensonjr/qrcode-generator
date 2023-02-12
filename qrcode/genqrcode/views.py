from django.shortcuts import render, redirect, get_list_or_404
from .forms import QRCodeForm
from .models import QRCode
from django.conf import settings as django_settings
import qrcode, os
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your views here.
def index(request):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
    if request.method == "POST":
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            code = form.save(commit=False)
            code.save()
            form.save_m2m()
            print(form.cleaned_data['text'])
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
            )
            qr.add_data(form.cleaned_data['text'])
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            image_path = 'genqrcode/static/img/{}.png'.format(form.cleaned_data['qr_name'])
            img.save(image_path)
            # image_file = InMemoryUploadedFile(img, None, "image.jpeg", "image/jpeg", img.tell, None)

            # model = QRCode()
            # model.image = img
            # model.save()

            return redirect(details, pk=code.pk)
    else:
        form = QRCodeForm()
    qrcodes = QRCode.objects.all()

    
        
    return render(request, 'genqrcode/index.html', {'form':form, 'qrcodes':qrcodes})


def details(request, pk):
    entry = get_list_or_404(QRCode, pk=pk)
    return render(request, 'genqrcode/detail.html', {'entry':entry})