from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('user_books',views.user_books,name='user_books'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout', views.logoutUser,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addbook/', views.addbook, name='addbook'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('admin_Interface/', views.admin_Interface, name='admin_Interface'),
    path('user_Interface/', views.user_Interface, name='user_Interface'),
    path('home/', views.home, name='home'),
    path('book_update/<int:pk>', views.book_update, name='book_update'),
    path('user_Interface/borrow_book/',views.borrowBook,name='borrow_book'),
    path('return_book/' , views.returnBook ,name='return_book'),
    path('extend_book/' , views.extendBook ,name='extend_book')
]
