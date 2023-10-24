from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import Post, Image, Customer
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PostSerializer, ImageSerializer, CustomerSerializer
from .filters import PostFilter
from .custom_permissions import IsPostOwner, IsImageOwner


class PostViewSet(ModelViewSet):
    permission_classes = [IsPostOwner]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]

    filterset_class = PostFilter
    search_fields = ['title', 'content']

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class ImageViewSet(ModelViewSet):
    permission_classes = [IsImageOwner]

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
