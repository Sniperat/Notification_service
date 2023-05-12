from rest_framework.viewsets import ModelViewSet, mixins, generics, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import ClientModel, MailModel, MessageModel
from .serializers import ClientModelSerializer, MailModelSerializer, MessageModelSerializer
from django.db.models import Count, Q
        

mail_id = openapi.Parameter('mail_id', openapi.IN_QUERY, type=openapi.TYPE_STRING)


class ClientView(ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientModelSerializer
    permission_classes = [IsAuthenticated, ]


class MailView(ModelViewSet):
    queryset = MailModel.objects.annotate(
        total_sent=Count('messages', filter=Q(messages__status='Sent'), distinct=True),
        total_failed=Count('messages', filter=Q(messages__status='Failed'), distinct=True),
        total_retry=Count('messages', filter=Q(messages__status='Retry'), distinct=True),
    )
    serializer_class = MailModelSerializer
    permission_classes = [IsAuthenticated, ]


class MessagesByMailView(mixins.ListModelMixin,GenericViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
            manual_parameters=[mail_id]
    )
    def list(self, request, *args, **kwargs):
        mail_id = request.GET.get('mail_id', False)
        if mail_id:
            self.queryset = self.queryset.filter(mail__id=mail_id)
        return super().list(request, *args, **kwargs)



