from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=views.homepage),
    path('', include('django_vite_plugin.urls')),
    path("about/", views.about),
    path("tags/", views.tags_index, name="tags"),
    path("tags/<uuid:pk>", views.show_tag, name="tags.show"),
    path("posts/", include("posts.urls")),
    path("", include("users.urls")),
    path("posts/<slug:post_slug>/comments/", include("comments.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

    # path("api/", include("api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
