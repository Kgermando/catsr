from django.shortcuts import render
from django.template import RequestContext
from django.views.defaults import page_not_found
# Create your views here.
#Bad request
def handler400(request, exception):
	return render(request,  template_name='error/400.html')
	response.status_code = 400
	return response

#Permission denied
def handler403(request, exception):
	return render(request,  template_name='error/403.html')
	response.status_code = 403
	return response

#Page not found
def handler404(request, exception):
	return render(request,  template_name='error/404.html')
	response.status_code = 404
	return response

#Server error
def handler500(request):
	return render(request,  template_name='error/500.html')
	response.status_code = 500
	return response

