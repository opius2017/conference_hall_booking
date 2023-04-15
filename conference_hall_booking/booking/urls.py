from django.urls import path
from . import views
from django.urls import path, include


"""
urlpatterns = [
    path('', include('booking.urls')),
    path('', views.home, name='home'),
    path('book/', views.book_conference_hall, name='book_conference_hall'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('approve/<int:booking_id>/',
         views.approve_booking, name='approve_booking'),
    path('reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
"""


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('approve/int:booking_id/', views.approve, name='approve'),
    path('reject/int:booking_id/', views.reject, name='reject'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
