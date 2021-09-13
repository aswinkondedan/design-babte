from django.urls import path,include
from . import views

urlpatterns = [
    path('hello',views.TestFun,name='hello'),
    path('signup',views.signupfunction,name='signup'),
    path('register',views.registerfunction,name='register'),
    path('admin',views.adminfunction,name='admin'),
    path('student_home',views.student_homefunction,name='student_home'),
    path('student_update/<int:id>',views.student_updatefunction,name='student_update'),
    path('student_details',views.student_detailsfunction,name='student_details'),
    path('edit/<int:id>',views.editfunction,name='edit'),
    path('active_st',views.active_stfunction,name='active_st'),
    path('inactive_st',views.inactive_stfunction,name='inactive_st'),
    path('inactivate/<int:id>',views.inactivatefunction,name='inactivate'),
    path('activate/<int:id>',views.activatefunction,name='activate'),
   
    
    
]

