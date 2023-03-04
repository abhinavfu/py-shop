from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.settings import MEDIA_ROOT

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/<str:mc>/<str:sc>/<str:br>/', views.shop, name='shop'),
    path('productInfo/<str:pk>/', views.productInfo, name='productInfo'),
    path('userprofile/addProduct/', views.addProduct, name='addProduct'),
    path('userprofile/editProduct/<str:pk>',
         views.editProduct, name='editProduct'),
    path('userprofile/delProduct/<str:pk>',
         views.delProduct, name='delProduct'),
    path('cart/', views.cart, name='cart'),
    path('cartCreate/<str:pk>', views.cartCreate, name='cartCreate'),
    path('cartUpdate/<str:pk>/<str:update>',
         views.cartUpdate, name='cartUpdate'),
    path('cartDelete/<str:pk>', views.cartDelete, name='cartDelete'),
    path('payment/<str:pk>', views.payment, name='payment'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('userprofile/', views.userProfile, name='userprofile'),
    path('editprofile/<int:pk>', views.editProfile, name='editprofile'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
