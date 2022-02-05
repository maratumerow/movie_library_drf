from django.urls import path

from . import views

    
urlpatterns = [
    path('', views.MovieViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', views.MovieViewSet.as_view({'get': 'retrieve'})),
    path('comment/', views.CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>/',
         views.CommentsView.as_view({'get': 'retrieve',
                                     'put': 'update',
                                     'delete': 'destroy'})),
    path('like/', views.LikeView.as_view({'post': 'create'})),
    path('like/<int:pk>/', views.LikeView.as_view({'delete': 'destroy'})),
]
