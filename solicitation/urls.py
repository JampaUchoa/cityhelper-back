# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'solicitation', views.SolicitationViewSet, basename='Solicitation')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.LoadCSV.as_view()),

]