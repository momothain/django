from django.urls import path
from rest_framework.routers import DefaultRouter
from .http_views import image_views

router = DefaultRouter()

urlpatterns = ([
    # path('', include(router.urls)),
    path("", image_views.index, name="index"),
    #
    path('image/', image_views.ImageView.as_view()),
    #
    path("jeff", image_views.get_jeff, name="getJeff"),
    path("jeff-bytes", image_views.get_jeff_bytes),
    path("jeff-url", views.get_jeff_url),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
