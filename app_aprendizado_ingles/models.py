from django.db import models
from django.contrib.auth.models import User

class Palavra(models.Model):
    """
    Modelo para armazenar palavras em inglês e suas traduções.

    Campos:
    - usuario: Chave estrangeira para associar a palavra a um usuário.
    - palavra: A palavra em inglês.
    - traducao: A tradução da palavra.
    - dificuldade: Nível de dificuldade da palavra (Fácil, Médio, Difícil).
    - palavra_aprendida: Indica se a palavra foi aprendida pelo usuário.
    - data_aprendizado: Data e hora em que a palavra foi aprendida.

    Método:
    - __str__: Retorna a representação da palavra como uma string. 
    """
    DIFICULDADE_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    palavra = models.CharField(max_length=100)    
    traducao = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=10, choices=DIFICULDADE_CHOICES)
    palavra_aprendida = models.BooleanField(default=False)
    data_aprendizado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.palavra}'


class Frase(models.Model):
    """
    Modelo para armazenar frases em inglês e suas traduções.

    Campos:
    - usuario: Chave estrangeira para associar a frase a um usuário.
    - palavras: Chave estrangeira para associar a frase a uma palavra específica.
    - frase: A frase em inglês.
    - traducao_frase: A tradução da frase.
    - dificuldade: Nível de dificuldade da frase (Fácil, Médio, Difícil).
    - frase_aprendida: Indica se a frase foi aprendida pelo usuário.
    - data_aprendizado_f: Data e hora em que a frase foi aprendida.

    Método:
    - __str__: Retorna uma representação da frase como uma string.
    """
    DIFICULDADE_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    palavras = models.ForeignKey(Palavra, on_delete=models.CASCADE)
    frase = models.CharField(max_length=300)
    traducao_frase = models.CharField(max_length=400)
    dificuldade = models.CharField(max_length=10, choices=DIFICULDADE_CHOICES)
    frase_aprendida = models.BooleanField(default=False)
    data_aprendizado_f = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.frase} - tradução - {self.traducao_frase}'



class VerbosConjugacao(models.Model):
    """
    Modelo para armazenar verbos em inglês e suas conjugações.

    Campos:
    - usuario: Chave estrangeira para associar os verbos a um usuário.
    - verbos: O verbo em inglês.
    - presente: Conjugação para o presente.
    - passado: Conjugação para o passado.
    - futuro: Conjugação para o futuro.
    - traducao: A tradução do verbo.
    - dificuldade: Nível de dificuldade dos verbos (Fácil, Médio, Difícil).
    - verbos_aprendido: Indica se os verbos foram aprendidos pelo usuário.
    - data_aprendida_verbos: Data e hora em que os verbos foram aprendidos.

    Método:
    - __str__: Retorna uma representação dos tempos verbais como uma string.
    """
    DIFICULDADE_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    verbos = models.CharField(max_length=100)
    presente = models.CharField(max_length=100)
    passado = models.CharField(max_length=100)
    futuro = models.CharField(max_length=100)
    traducao = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=10, choices=DIFICULDADE_CHOICES)
    verbos_aprendido = models.BooleanField(default=False)
    data_aprendida_verbos = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.presente} - {self.passado} - {self.futuro}'

