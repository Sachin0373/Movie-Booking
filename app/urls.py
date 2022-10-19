from django.contrib import admin
from django.urls import path
from . import views
from app.views import home_page,Thankyouview,PersonCreateView,PersonListView,PersonUpdateView,PersonDetailView,PersonDeleteView

app_name = 'app'

urlpatterns = [
    path("",home_page.as_view(),name = 'home'),
    path('signup/', views.home_page.as_view(), name= 'signup'),
    path('design/', views.design_page, name= 'design'),
    path('thankyou/',Thankyouview.as_view(),name = 'thankyou'),
    path('create_person/',PersonCreateView.as_view(),name = 'create_person'),
    path('list_person/',PersonListView.as_view(),name = 'list_person'),
    path('update_person/<int:pk>/',PersonUpdateView.as_view(),name = 'update_person'),
    path('person/<int:pk>/',PersonDetailView.as_view(),name = 'person'),
    path('delete_person/<int:pk>/',PersonDeleteView.as_view(),name = 'delete_person')
]
