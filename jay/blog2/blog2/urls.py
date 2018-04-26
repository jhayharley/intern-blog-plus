from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import get_user_model
from info.views import RegisterView
User = get_user_model()
from info.models import Info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls', namespace='posts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(model=User, success_url="/accounts/login/"), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)