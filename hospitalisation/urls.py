from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView , LogoutView



from .views import *

urlpatterns = [
    path('dashboard/',Dashboard, name='dashboard'),

    path('Medcins/',Dashboard_Medcins, name='dashboard_Medcins'),
    path('Medcins/Liste/',Dashboard_Medcins_Liste, name='dashboard_Medcins_Liste'),
    path('Medcins/Ajouter/',AjouterMedcin, name='dashboard_ajouter_medcin'),

    path('Ressource_Matérielles/',Chart, name='dashboard_Matériel'),
    path('Ressource_Matérielles/Ajouter/',AjouterMateriel, name='dashboard_ajouter_materiel'),

    path('Assistants/',Dashboard_Assistants, name='dashboard_Assistants'),
    path('Assistants/liste/',Dashboard_Assistants_Liste, name='dashboard_Assistants_liste'),
    path('Assistants/Ajouter/',AjouterAssistant, name='dashboard_ajouter_assistant'),

    path('Patients/',Dashboard_Patients, name='dashboard_Patients'),
    path('Patients/Ajouter/',AjouterPatient, name='dashboard_ajouter_patient'),

    path('Salles/',Dashboard_Salles, name='dashboard_Salles'),
    path('Salles/Ajouter/',AjouterSalle, name='dashboard_ajouter_salle'),

    path('Hospitalisations/',Dashboard_Hospitalisations, name='dashboard_Hospitalisations'),
    path('Hospitalisations/Ajouter/',AjouterHospitalisation, name='dashboard_ajouter_hospitalisation'),
    path('<int:Hospitalisation_id>/Hospitalisations/Modifier/',Modifier_Hospitalisation, name='dashboard_modifier_hospitalisation'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LoginView.as_view(template_name='hospitalisation/Loginpage.html'), name='login'),

    path('population-chart/', population_chart, name='population-chart'),
    path('population-chart-line1/', pie_chart_medecin, name='population-chart-medecin'),
    path('population-chart-line2/', pie_chart_assistant, name='population-chart-assistant'),
    path('population-chart-patient/', pie_chart_patient, name='population-chart-patient'),



]
