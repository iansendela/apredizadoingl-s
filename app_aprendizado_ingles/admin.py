from django.contrib import admin
from .models import Palavra
from .models import Frase, VerbosConjugacao



admin.site.register(Palavra)
admin.site.register(Frase)
admin.site.register(VerbosConjugacao)

 