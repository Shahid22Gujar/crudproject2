from django.urls import path
from . import views

urlpatterns = [
   
    #path('home/',views.add_show,name="addandshow"),
    path('home/',views.UserAddShowView.as_view(),name="addandshow"),
    #path('delete/<int:id>',views.delete_data,name="deletedata"),
    path('delete/<int:id>',views.UserDeleteView.as_view(),name="deletedata"),
    #path('update/<int:id>',views.update_data,name="updatedata"),
    path('update/<int:id>',views.UserUpdateView.as_view(),name="updatedata"),
]