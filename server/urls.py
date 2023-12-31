# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('projects/', include("projects.urls")),
#     path('', TemplateView.as_view(template_name="index.html"), name="index")
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]
