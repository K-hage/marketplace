from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.paginations import AdPagination
from ads.permissions import IsUser, IsAdmin
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    default_serializer = AdSerializer
    serializer_classes = {
        'retrieve': AdDetailSerializer,
        'create': AdDetailSerializer,
        'update': AdDetailSerializer,
        'partial_update': AdDetailSerializer,
        'destroy': AdDetailSerializer,
    }

    default_permission = (AllowAny(),)
    permissions = {
        'retrieve': (IsAuthenticated(),),
        'create': (IsAuthenticated(), IsUser() or IsAdmin()),
        'destroy': (IsAuthenticated(), IsUser() or IsAdmin()),
        'update': (IsAuthenticated(), IsUser() or IsAdmin()),
        'partial-update': (IsAuthenticated(), IsUser() or IsAdmin()),
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(
        detail=False,
        methods=[
            "get",
        ],
    )
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    default_permission = (IsAuthenticated(),)
    permissions = {
        'create': (IsUser() or IsAdmin(),),
        'destroy': (IsUser() or IsAdmin(),),
        'update': (IsUser() or IsAdmin(),),
        'partial-update': (IsUser() or IsAdmin(),),
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()
