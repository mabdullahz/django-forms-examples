from django.shortcuts import render

from .forms import ReviewForm

def index(request):
    review = ReviewForm()
    return render(request, 'reviews/review.html', { 'form': review })

def form_submit(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'reviews/thank-you.html', {})
    else:
        return render(request, 'reviews/review.html', {'form': form})