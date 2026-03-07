from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):

    COMBUSTIVEL_CHOICES = [
        ("gasolina", "Gasolina"),
        ("diesel", "Diesel"),
        ("eletrico", "Elétrico"),
        ("hibrido", "Híbrido"),
    ]

    TRANSMISSAO_CHOICES = [
        ("manual", "Manual"),
        ("automatico", "Automático"),
    ]

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    modelo = models.CharField(max_length=100)

    ano = models.IntegerField()

    preco = models.DecimalField(max_digits=10, decimal_places=2)

    quilometragem = models.IntegerField()

    combustivel = models.CharField(
        max_length=20,
        choices=COMBUSTIVEL_CHOICES
    )

    transmissao = models.CharField(
        max_length=20,
        choices=TRANSMISSAO_CHOICES
    )

    cor = models.CharField(max_length=50)

    descricao = models.TextField()

    imagem = models.ImageField(upload_to="veiculos/")

    data_publicacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.marca} {self.modelo}"