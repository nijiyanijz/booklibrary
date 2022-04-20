from owner.models import Books
import django_filters
class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='contains')#contains for fiter nmml kodkunathm evdelum indayaal mathii
    price = django_filters.CharFilter(lookup_expr='contains')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model=Books
        fields=['book_name','author','price']