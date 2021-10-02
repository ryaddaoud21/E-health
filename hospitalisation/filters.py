import django_filters
from .models import *
from django_filters import DateFilter,TimeFilter


class Medcinfilter(django_filters.FilterSet):
    start_time = TimeFilter(field_name="heure_debut", lookup_expr='gte')
    end_time = TimeFilter(field_name="heure_fin", lookup_expr='lte')


    class Meta:
        model = Médcin
        fields =['Nom','heure_debut','heure_fin','jourtravail']



class AssistantFilter(django_filters.FilterSet) :
    start_time = TimeFilter(field_name="heure_debut", lookup_expr='gte')
    end_time = TimeFilter(field_name="heure_fin", lookup_expr='lte')
    class Meta:
        model = Assistant
        fields =['Nom','heure_debut','heure_fin','jour_travail']



class Sallefilter(django_filters.FilterSet) :
    class Meta:
        model = Salle
        fields = ['Nemero_salle']

class Hospfilter(django_filters.FilterSet) :
    start_date = TimeFilter(field_name="Date_Entrée", lookup_expr='gte')
    end_date = TimeFilter(field_name="Date_Sortie", lookup_expr='lte')
    class Meta:
        model = Hospitalisation
        fields = '__all__'


class Patientfilter(django_filters.FilterSet) :
    class Meta:
        model = Patient
        fields = ['Nom']
