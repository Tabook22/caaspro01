import django_filters
from .models import Peertotur


class PeerFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Peertotur
        fields = {
            'pname': ['icontains'],
            'pgsm': ['icontains'],
            # 'pmajor': ['icontains'],
        }

    def filter_by_ordering(self, queryset, name, value):
        expression = 'reqdate' if value == 'ascending' else '-reqdate'
        return queryset.order_by(expression)
