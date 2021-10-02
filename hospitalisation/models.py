from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from multiselectfield import MultiSelectField
import datetime




class Date_travail(models.Model):
    id_jour = models.AutoField(primary_key=True)
    date = models.DateField()
    def __str__(self):
        return str(self.date)




class Salle(models.Model):
    Nemero_salle = models.IntegerField()
    Numero_lits = models.IntegerField()
    Etage = models.IntegerField()
    complete = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return str(self.Nemero_salle)



class Ressource_Materiel(models.Model):

    type = models.CharField(max_length=50)
    quantié =models.IntegerField()

    def __str__(self):
            return str(self.type)

class Médcin(models.Model):
    id_Médcin = models.AutoField(primary_key=True)
    CHOIX = (
        ('L’allergologie', 'L’allergologie'),
        ('L’anesthésiologie.', 'L’anesthésiologie.'),
        ('L’andrologie.', ' L’andrologie.'),
        ('La cardiologie.', 'La cardiologie.'),
        (' La chirurgie.', ' La chirurgie.'),
        ('La chirurgie cardiaque.', 'La chirurgie cardiaque.'),
        (' La chirurgie esthétique,', ' La chirurgie esthétique,'),
        ('La chirurgie générale.', 'La chirurgie générale.'),
        ('La chirurgie maxillo-faciale.', 'La chirurgie maxillo-faciale.'),
        (' La chirurgie pédiatrique.', ' La chirurgie pédiatrique.'),
        (' La chirurgie thoracique.', ' La chirurgie thoracique.'),
        (' La chirurgie vasculaire.', ' La chirurgie vasculaire.'),
        (' La neurochirurgie.', ' La neurochirurgie.'),
        (' La dermatologie.', ' La dermatologie.'),
        (' L’endocrinologie.', ' L’endocrinologie.'),
        (' La gastro-entérologie.', ' La gastro-entérologie.'),
        ('La gériatrie.', 'La gériatrie'),
        ('La gynécologie.', 'La gynécologie'),
        ('L’hématologie.', 'L’hématologie'),
        ('L’hépatologie.', 'L’hépatologie'),
        ('L’infectiologie.', 'L’infectiologie'),
        ('La médecine aiguë.', 'La médecine aiguë.'),
        ('La médecine du travail.', 'La médecine du travail.'),
        ('La médecine générale.', 'La médecine générale.'),
        (' La médecine interne.', ' La médecine interne.'),
        ('  La médecine nucléaire.', '  La médecine nucléaire.'),
        (' La médecine palliative.', ' La médecine palliative.'),
        ('La médecine physique.', 'La médecine physique.'),
        ('La médecine préventive.', 'La médecine préventive.'),
        ('La néonatologie.', 'La néonatologie.'),
        ('La néphrologie.', 'La néphrologie.'),
        ('La neurologie.', 'La neurologie'),
        (' L’odontologie.', ' L’odontologie'),
        (' L’oncologie.', ' L’oncologie'),
        (' L’obstétrique.', ' L’obstétrique'),
        ('L’ophtalmologie.', 'L’ophtalmologie'),
        (' L’orthopédie.', ' L’orthopédie'),
        ('L’Oto-rhino-laryngologie.', 'L’Oto-rhino-laryngologie'),
        ('La pédiatrie.', 'La pédiatrie'),
        (' La pneumologie.', ' La pneumologie'),
        ('La psychiatrie.', 'La psychiatrie'),
        ('La radiologie.', 'La radiologie'),
        ('La radiothérapie.', 'La radiothérapie'),
        ('La rhumatologie', 'La rhumatologie'),
        ('L’urologie', 'L’urologie'),
    )
    CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    SANG = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    specialite = models.CharField(max_length=50 ,choices=CHOIX)
    Nom = models.CharField(max_length=50, null=True)
    Age = models.IntegerField()
    Sexe = models.CharField(max_length=50, choices=CHOICES)
    Téléphone = models.CharField(max_length=50)
    Email = models.EmailField(max_length=200)
    Address = models.CharField(max_length=200, null=True)
    Sang = models.CharField(max_length=50 ,choices=SANG)
    jourtravail =models.ManyToManyField(Date_travail, related_name="date_travail_medcin", blank=True)
    heure_debut =models.TimeField(default='20:00')
    heure_fin=models.TimeField(default='21:00')
    En_Travail= models.BooleanField(default=False, null=False,blank=False)
    image =models.ImageField(null=True, blank=True)
    valeur = models.IntegerField(default=1)

    def __str__(self):
        return self.Nom


    def get_jours(self):
            jour =self.jour_travail
            return jour

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Assistant(models.Model):
    id_assistant = models.AutoField(primary_key=True)

    CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    SANG = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    Nom = models.CharField(max_length=50, null=True)
    Age = models.IntegerField()
    Sexe = models.CharField(max_length=50, choices=CHOICES)
    Téléphone = models.CharField(max_length=50)
    Email = models.EmailField(max_length=200)
    Address = models.CharField(max_length=200, null=True)
    heure_debut = models.TimeField(default='20:00')
    heure_fin = models.TimeField(default='21:00')
    jour_travail = models.ManyToManyField(Date_travail, related_name="jour_travail_assistant", blank=True)
    Sang = models.CharField(max_length=50 ,choices=SANG)
    En_Travail= models.BooleanField(default=False, null=False,blank=False)
    image = models.ImageField(null=True, blank=True)
    valeur = models.IntegerField(default=1)



    def __str__(self):
        return self.Nom

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url






    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Patient(models.Model):
    SANG = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    id_Patient = models.AutoField(primary_key=True)
    CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    ACT = (
        ('hospitalisé', 'hospitalisé'),
        ('visite', 'visite'),
    )
    Nom = models.CharField(max_length=50, null=True)
    Age = models.IntegerField()
    Sexe = models.CharField(max_length=50, choices=CHOICES)
    Téléphone = models.CharField(max_length=50)
    Address = models.CharField(max_length=200, null=True)
    Sang = models.CharField(max_length=100, choices=SANG)
    Etat = models.CharField(max_length=50, choices=ACT , default='hospitalisé')
    Date_visite =models.DateField(null=True, blank=True)
    valeur =models.IntegerField(default=1)

    def __str__(self):
        return self.Nom




class Hospitalisation(models.Model):
    Date_Entrée =models.DateField(null=True, blank=True)
    Date_Sortie =models.DateField(null=True, blank=True)
    patient = models.ForeignKey(Patient,on_delete=models.SET_NULL, null=True)
    médcin = models.ForeignKey(Médcin,on_delete=models.SET_NULL, null=True)
    Salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    assistant = models.ForeignKey(Assistant,on_delete=models.SET_NULL, null=True)
    materiel = models.ManyToManyField(Ressource_Materiel,)
    valeur =models.IntegerField(default=1)









