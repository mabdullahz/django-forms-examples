from django.urls import path

from .views import index, form_submit

urlpatterns = [
    path('', index, name='reviews_index'),
    path('submit/', form_submit, name='review_submit'),
]
