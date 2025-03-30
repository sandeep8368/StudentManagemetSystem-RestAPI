from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import StudentViewset


router = DefaultRouter()
router.register(r'items',StudentViewset,basename='student')
urlpatterns = [
    path('', include(router.urls)),
]