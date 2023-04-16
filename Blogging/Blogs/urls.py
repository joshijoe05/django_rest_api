from django.urls import path,include
from . import views

urlpatterns = [
    path('all/',views.BlogList.as_view()),
    path('create/',views.BlogCreate.as_view()),
    path('create/<int:pk>/',views.BlogRetrieveUpdate.as_view()),
]