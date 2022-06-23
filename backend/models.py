from django.db import models

handicaps = (
    ('Moteur', 'Moteur'),
    ('Mental', 'Mental'),
    ('Visuel', 'Visuel'),
    ('Auditif', 'Auditif'),
)


class Beneficiaire(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    cin = models.CharField(max_length=10)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    handicap = models.CharField(max_length=250, choices=handicaps)
    motpass = models.CharField(max_length=10)

    def __str__(self):
        return self.nom +" "+ self.prenom


class Demande(models.Model):
    beneficiaire =models.ForeignKey(Beneficiaire, on_delete= models.CASCADE, null=True)
    appareil = models.CharField(max_length=250)
    date_demande = models.DateField(null=True)