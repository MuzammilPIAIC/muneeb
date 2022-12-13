from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("l", views.index, name="index"),
    path("", views.record, name="record"),
    path("record/detail/<uuid:id>/", views.record_detail, name="record_detail"),
    path("record/text/<str:id>/", views.text, name="text"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)