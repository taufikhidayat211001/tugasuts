from django.db import models

class Pondok(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Santri(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pondok = models.ForeignKey(Pondok, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pendaftaran(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    pondok = models.ForeignKey(Pondok, on_delete=models.CASCADE)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.santri} - {self.pondok}"

