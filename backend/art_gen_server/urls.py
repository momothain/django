from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = ([
    # path('', include(router.urls)),
    path("", views.index, name="index"),
    #
    path('image/', views.ImageView.as_view()),
    #
    path("getJeff", views.get_jeff, name="getJeff"),
    path("getJeffBytes", views.get_jeff_bytes),
    path("getJeffUrl", views.get_jeff_url),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
