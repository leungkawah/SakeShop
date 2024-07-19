from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Sake
from .forms import SakeForm

def sake_list(request):
    sakes = Sake.objects.all()
    return render(request, 'sake_list.html', {'sakes': sakes})

def sake_management(request):
    sakes = Sake.objects.all()
    form = SakeForm()
    return render(request, 'sake_management.html', {'sakes': sakes, 'form': form})

def sake_create(request):
    if request.method == 'POST':
        form = SakeForm(request.POST, request.FILES)
        if form.is_valid():
            sake = form.save()
            return JsonResponse({'id': sake.id, 'name': sake.name, 'price': str(sake.price)})
    return JsonResponse({'error': 'Invalid form'}, status=400)

def sake_update(request, pk):
    sake = get_object_or_404(Sake, pk=pk)
    if request.method == 'POST':
        form = SakeForm(request.POST, request.FILES, instance=sake)
        if form.is_valid():
            sake = form.save()
            return JsonResponse({'id': sake.id, 'name': sake.name, 'price': str(sake.price)})
    return JsonResponse({'error': 'Invalid form'}, status=400)

def sake_delete(request, pk):
    sake = get_object_or_404(Sake, pk=pk)
    sake.delete()
    return JsonResponse({'success': True})