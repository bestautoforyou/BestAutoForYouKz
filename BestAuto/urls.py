from django.urls import path
from . import views
from .views import (
    ProductListView,
    SearchView,
    IndividualProductsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    IndexListView,
    ProductImagesCreateView,
)






urlpatterns = [
    path('products/', ProductListView.as_view(), name='products-view'),
    path('products_search/', SearchView.as_view(), name='products-search-view'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    #path('products_individual/', views.products_individual, name='products-individual'),
    path('products/<int:pk>/', IndividualProductsListView.as_view(), name='products-individual'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    path('products/<int:pk>/new-images/', ProductImagesCreateView.as_view(), name='product-create-images'),
    #path('', views.index, name='home-main'),
    path('', IndexListView.as_view(), name='home-main'),
]