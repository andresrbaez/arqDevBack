# from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
# from rest_framework import routers
# from projects import views

# router = routers.DefaultRouter()
# router.register(r'projects', views.ProjectView, 'projects')

# urlpatterns = [
#     path("api/v1/", include(router.urls)),
#     path('docs/', include_docs_urls(title="Projects API"))
# ]



from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

