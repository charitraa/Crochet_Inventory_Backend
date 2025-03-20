"""
URL configuration for crochet_inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import RouterDetailsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('product/', include('products.urls')),
    path('category/', include('category.urls')),
    path('auth/', include('authentications.urls')),
    path('color/', include('colors.urls')),
    path('size/', include('sizes.urls')),
    path('material/', include('materials.urls')),
    path('order/', include('orders.urls')),
    path('beads_size/', include('beads_size.urls')),
    path('beads_type/', include('beads_type.urls')),
    path('glue_type/', include('glue_type.urls')),
    path('ribbon_type/', include('ribbon_type.urls')),
    path('ribbon_size/', include('ribbon_size.urls')),
    path('keyring_type/', include('keyring_type.urls')),
    path('wrapper_type/', include('wrapper_type.urls')),
    path('wire_size/', include('wire_size.urls')),
    path('wire_type/', include('wire_type.urls')),
    path('yarn_size/', include('yarn_size.urls')),
    path('yarn_type/', include('yarn_type.urls')),
    path('purchase_material/', include('purchaseMaterials.urls')),
    path('', RouterDetailsView.as_view(), name='router_details'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
