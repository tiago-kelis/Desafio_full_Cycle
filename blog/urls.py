from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('core.urls')),
    # Remova ou ajuste o redirecionamento abaixo
    # path('', admin.site.urls),
    path('', include('core.urls')),  # Direciona a raiz para o blog
]
