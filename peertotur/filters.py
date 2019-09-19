import django_filters
from .models import Peertotur

class PeerFilter(django_filters.FilterSet):

    class Meta:
        model =Peertotur
        fields=('pname','pmajor','pgsm')