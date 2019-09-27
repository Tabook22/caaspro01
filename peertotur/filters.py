import django_filters
from .models import Peertotur, Peertoturexperties,Document


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

class PeerExpFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Peertoturexperties
        fields = {
            'pname':['in'], #because it is a list of fileds
            'coursename': ['icontains'],
            'coursecode': ['icontains'],
            # 'pmajor': ['icontains'],
        }

    def filter_by_ordering(self, queryset, name, value):
        expression = 'coursename' if value == 'ascending' else 'coursename'
        return queryset.order_by(expression)


class PeerUploadFileFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model =Document
        fields = {
            'pname':['in'], #because it is a list of fileds
            'dateupload': ['icontains']
            # 'pmajor': ['icontains'],
        }

    def filter_by_ordering(self, queryset, name, value):
        expression = 'coursename' if value == 'ascending' else 'coursename'
        return queryset.order_by(expression)