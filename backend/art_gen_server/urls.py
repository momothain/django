from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = ([
    # path('', include(router.urls)),
    path("", views.index, name="index"),
    path("getJeff", views.getJeff, name="getJeff"),
    path("getJeffBytes", views.getJeffBytes),
    path("getJeffUrl", views.getJeffUrl),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
