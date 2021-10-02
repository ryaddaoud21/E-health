from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .filters import Medcinfilter,Sallefilter,AssistantFilter,Hospfilter,Patientfilter
from django.db.models import Count
from itertools import chain
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required








@login_required
def Dashboard(request):
    assistants=Assistant.objects.all()
    patients=Patient.objects.all()
    docteurs=Médcin.objects.all()
    total_médcins =Médcin.objects.count()
    total_assistants =Assistant.objects.count()
    total_patients =Patient.objects.count()
    total_hospitalisations=Hospitalisation.objects.count()
    salles = Salle.objects.all()
    filter = Medcinfilter(request.GET, queryset=docteurs)
    docteurs = filter.qs

    combined_results = list(chain(docteurs, assistants))
    combined_results_total = len(combined_results)

    context={'combined_results_total':combined_results_total,'docteurs':docteurs ,'patients':patients,'total_médcins':total_médcins,'total_assistants':total_assistants,'total_patients': total_patients,'total_hospitalisations':  total_hospitalisations, 'assistants': assistants,'salles':salles,'filter':filter,'combined_results':combined_results}
    return render(request,'hospitalisation/Dashboard.html',context)
@login_required
def Dashboard_Medcins(request):
    docteurs=Médcin.objects.all()
    filter = Medcinfilter(request.GET, queryset=docteurs)
    docteurs = filter.qs
    jours = Date_travail.objects.all()

    context={'docteurs':docteurs , 'filter':filter,'jours':jours}
    return render(request,'hospitalisation/dashboard_Medcins.html',context)

@login_required
def Dashboard_Medcins_Liste(request):
    docteurs=Médcin.objects.all()
    context={'docteurs':docteurs }
    return render(request,'hospitalisation/dashboard_Medcins_Liste.html',context)

@login_required
def Dashboard_Assistants(request):
    assistants=Assistant.objects.all()
    filter = AssistantFilter(request.GET, queryset=assistants)
    assistants = filter.qs
    jours = Date_travail.objects.all()

    context={'assistants':assistants, 'filter': filter,'jours':jours}
    return render(request,'hospitalisation/Dashboard_Assistans.html',context)

@login_required
def Dashboard_Assistants_Liste(request):
    assistants=Assistant.objects.all()
    filter = AssistantFilter(request.GET, queryset=assistants)
    assistants = filter.qs
    context={'assistants':assistants, 'filter': filter}
    return render(request,'hospitalisation/Dashboard_Assistans_Liste.html',context)

@login_required
def Dashboard_Patients(request):
    docteurs=Médcin.objects.all()
    patients=Patient.objects.all()
    filter = Patientfilter(request.GET, queryset=patients)
    patients = filter.qs
    context={'docteurs':docteurs,'patients':patients,'filter':filter}
    return render(request,'hospitalisation/Dashboard_Patients.html',context)

@login_required
def Dashboard_Salles(request):
    salles=Salle.objects.all()
    filter = Sallefilter(request.GET, queryset=salles)
    salles = filter.qs
    context={'salles':salles,'filter':filter}
    return render(request,'hospitalisation/Dashboard_Salles.html',context)


@login_required
def Dashboard_Hospitalisations(request):
    hospitalisations=Hospitalisation.objects.all()
    filter = Hospfilter(request.GET, queryset=hospitalisations)
    hospitalisations = filter.qs
    context={'hospitalisations':hospitalisations,'filter':filter}
    return render(request,'hospitalisation/Dashboard_Hospitalisation.html',context)

@login_required
def Dashboard_Materiel(request):
    docteurs=Médcin.objects.all()
    hospitalisations=Hospitalisation.objects.all()
    Mats = Ressource_Materiel.objects.all()
    context={'docteurs':docteurs , 'hospitalisations':hospitalisations, 'Mats':Mats}
    return render(request,'hospitalisation/Dashboard_Matériel.html',context)

@login_required
def AjouterMedcin(request):
    if request.method =='POST':
        form = MedcinForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('dashboard_Medcins')
    else:
        form = MedcinForm
    context = {'form': form}
    return render(request,'hospitalisation/Dashboard_Ajouter_Medcin.html', context)


@login_required
def AjouterPatient(request):
    if request.method =='POST':
        form = PatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_Patients')
    else:
        form = PatForm
    context = {'form': form}
    return render(request,'hospitalisation/Dashboard_Ajouter_Patient.html', context)




@login_required
def AjouterAssistant(request):
    if request.method =='POST' :
        form = AssistantForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('dashboard_Assistants')
    else:
        form = AssistantForm
    context = {'form': form}

    return render(request,'hospitalisation/Dashboard_Ajouter_Assistant.html',context )

@login_required
def AjouterSalle(request):
    if request.method =='POST' :
        form = SalleForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('dashboard_Salles')
    else:
        form = SalleForm
    context = {'form': form}

    return render(request,'hospitalisation/Dashboard_Ajouter_Salle.html',context )

@login_required
def AjouterMateriel(request):
    if request.method =='POST' :
        form = MaterielForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('dashboard_Matériel')
    else:
        form = MaterielForm
    context = {'form': form}

    return render(request,'hospitalisation/Dashboard_Ajouter_Meteriel.html',context )

@login_required
def AjouterHospitalisation(request):
    if request.method == 'POST':
        form = HospitalisationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_Hospitalisations')
    else:
        form = HospitalisationForm
    context = {'form': form}

    return render(request,'hospitalisation/Dashboard_Ajouter_Hospitalisation.html',context )


@login_required
def Chart(request):
    docteurs = Médcin.objects.all()
    hospitalisations = Hospitalisation.objects.all()
    Mats = Ressource_Materiel.objects.all()
    labels = []
    data = []

    queryset = Ressource_Materiel.objects.order_by('quantié')[:5]
    for materiel in queryset:
        labels.append(materiel.type)
        data.append(materiel.quantié)
    context = {'docteurs': docteurs, 'hospitalisations': hospitalisations, 'Mats': Mats,'labels': labels,'data': data}

    return render(request, 'hospitalisation/Dashboard_Matériel.html', context)


from django.db.models import Sum
from django.http import JsonResponse


@login_required
def Modifier_Hospitalisation(request, Hospitalisation_id):
    hospitalisation = Hospitalisation.objects.get(pk=Hospitalisation_id)
    if request.method == 'POST':
        form = HospitalisationForm(request.POST,instance=hospitalisation)

        if form.is_valid():
            hospitalisation = form.save(commit=False)
            hospitalisation.status = request.POST.get('status')
            hospitalisation.save()

            return redirect('/')
    else:
        form = HospitalisationForm(instance=hospitalisation)

    context = {'form': form ,'hospitalisation':hospitalisation}
    return render(request, 'hospitalisation/Dashboard_Modifier_Hospitalisation.html',context)


from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse



@login_required
def population_chart(request):
    labels = []
    data = []

    queryset = Hospitalisation.objects.values('Date_Entrée').annotate(jour_total=Sum('valeur'))
    for entry in queryset:
        labels.append(entry['Date_Entrée'])
        data.append(entry['jour_total'])
    return JsonResponse(data={ 'labels': labels, 'data': data, })



@login_required
def pie_chart_medecin(request):

    labels = []
    data= []

    queryset = Médcin.objects.values('jourtravail__date').annotate(jour_totals1=Sum('valeur'))

    for entry in queryset:
        labels.append(entry['jourtravail__date'])
        data.append(entry['jour_totals1'])


    return JsonResponse(data={'labels': labels, 'data': data ,})





@login_required
def pie_chart_assistant(request):

    labels = []
    data= []

    queryset = Assistant.objects.values('jour_travail__date').annotate(jour_totals1=Sum('valeur'))

    for entry in queryset:
        labels.append(entry['jour_travail__date'])
        data.append(entry['jour_totals1'])


    return JsonResponse(data={'labels': labels, 'data': data })





@login_required
def pie_chart_patient(request):
    labels = []
    data = []

    queryset = Patient.objects.values('Date_visite').annotate(jour_totals=Sum('valeur'))

    for entry in queryset:
        labels.append(entry['Date_visite'])
        data.append(entry['jour_totals'])


    return JsonResponse(data={'labels': labels, 'data': data})


























