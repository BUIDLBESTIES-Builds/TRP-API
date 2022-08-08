from django.urls import include, path

from rest_framework import routers

from django.urls import path
# from .views import UserDetailAPI,RegisterUserAPIView

from api.views import UserViewSet, ReimbursementDetailViewSet, ReimbursementViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'reimbursement', ReimbursementViewSet)
router.register(r'details',ReimbursementDetailViewSet, basename="MyObject")



urlpatterns = [
    path('', include(router.urls)),
]

