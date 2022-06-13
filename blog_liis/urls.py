from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/api-auth/', include('rest_framework.urls')),
    path('api/v1/blog/', include('blog_api.urls'))

]
