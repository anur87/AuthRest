from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters, viewsets, pagination
from django_filters.rest_framework import FilterSet, DjangoFilterBackend, DateFilter

from .serializers import BlogSerializer
from .models import Blog
from .permissions import IsAuthorOrReadOnly



class BlogPaginatoin(pagination.PageNumberPagination):
    '''
    PageNumberPagination - обеспечивает пагинацию для модели News.
    page_size - количество элементов на странице.
    page_size_query_param - параметр для указания количества элементов на странице.
    max_page_size - максимальное количество элементов на странице.
    '''
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class FilterBlog(FilterSet):
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Blog
        fields = ['start_date', 'end_date', 'author']


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['title', 'date', 'description', 'author__username']
    pagination_class = BlogPaginatoin
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = FilterBlog