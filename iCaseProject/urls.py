from django.contrib import admin
from django.urls import path,include
import pages.views as page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",page.home_view,name='home-view'),
    path("home/",page.home_view),
    # path("cases/",page.cases_view),
    path('cases/',include('product.urls')),
    # path("collection/",page.collection_view),

]
