from django.urls import path, include
from rest_framework import routers
from .views import ClientView, MailView, MessagesByMailView


router = routers.DefaultRouter()
router.register('client', ClientView)
router.register('mail', MailView)
router.register('mailMessages', MessagesByMailView)

urlpatterns = [
    path('', include(router.urls)),
]