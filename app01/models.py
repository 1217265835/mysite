from django.db import models

# Create your models here.
class Gene_Dis(models.Model):
    Gene=models.CharField(max_length=32)
    Dis=models.CharField(max_length=32)

class Gene_Gene(models.Model):
    Gene1=models.CharField(max_length=32)
    Gene2 = models.CharField(max_length=32)
    num=models.DecimalField(max_digits=10, decimal_places=5)

class Gene_Node(models.Model):
    Gene = models.CharField(max_length=32)
    Node =models.IntegerField()

class Herb_Node(models.Model):
    Herb=models.CharField(max_length=32)
    Node =models.IntegerField()


class symmap3_herb_mm_symp_jiaoji(models.Model):
    Herb = models.CharField(max_length=128)
    Gene = models.CharField(max_length=128)

class symmap3_herb_target_jiaoji(models.Model):
    Herb = models.CharField(max_length=128)
    Gene = models.CharField(max_length=128)

class symmap3_herb_herb_cosine_jiaoji(models.Model):
    herb1 = models.CharField(max_length=128)
    herb2 = models.CharField(max_length=128)
    num = models.DecimalField(max_digits=10, decimal_places=5)