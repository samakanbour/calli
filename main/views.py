from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from models import UploadFile
import json

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadFile
		fields = '__all__'

def upload(request):
	# UploadFile.objects.all().delete()
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			new_file = UploadFile(file=request.FILES['file'])
			new_file.save()
			new_file_name = str(new_file.file).split('/')[-1]
			return HttpResponse(json.dumps({'image':new_file_name}), content_type="application/json")
	else:
		form = UploadFileForm()
	images = [str(f.file).split('/')[-1] for f in UploadFile.objects.all()]
	return render(request, 'main/upload.html', {'form':form, 'images':images})
	
