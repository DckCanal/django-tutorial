from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('books/',views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/',views.AutoreListview.as_view(), name = 'authors'),
    #path('author/<int:pk>',views.AutoreDetailView.as_view(),name='author-detail'),
    re_path(r'^author/(?P<pk>\d+)$',views.AutoreDetailView.as_view(), name='author-detail'),
    #path('preferito/<int:pk>',views.setPreferito.as_view(),name='pref'),
]
