from django.urls import path 
from . import views

urlpatterns = [
  path('',views.MainPage, name='Home'),
  path('login/', views.login_page, name='login'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_page, name='register'),
  path('biz_kimiz/', views.biz_kimiz, name='biz_kimiz'),
  path('derstalepleri/', views.DersTalepleri,name='DersTalepleri'),
  path('OzelDers/',views.OzelDers,name='OzelDers' ),
  path('matematik/',views.Matematik, name='matematik'),
  path('python/',views. Python, name='python'),
  path('fizik/',views.Fizik, name='fizik'),
  path('gitar/',views.Gitar, name='gitar'),
]
