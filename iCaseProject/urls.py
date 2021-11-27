from django.contrib import admin
from django.urls import path,include
import pages.views as page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",page.home_view,name='home-view'),
    path('cases/',include('product.urls')),

    # path("cases/",page.cases_view),
    # path("collection/",page.collection_view),

    path('test/',page.test_view),

]
