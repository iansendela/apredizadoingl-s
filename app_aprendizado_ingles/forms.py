from django import forms
from .models import Palavra, Frase


class PalavraForm(forms.ModelForm):
    """
    Formulário para adicionar uma nova palavra.

    Este formulário é um ModelForm para o modelo Palavra, com os campos 'palavra', 'traducao' e 'dificuldade'.
    """
    class Meta: 
        model = Palavra
        fields = ['palavra', 'traducao', 'dificuldade']

class FraseForm(forms.ModelForm):
    """
    Formulário para adicionar uma nova frase.

    Este formulário é um ModelForm para o modelo Frase, com os campos 'palavras', 'frase', 'traducao_frase' e 'dificuldade'.
    Ele também inclui um método __init__ personalizado para filtrar as opções do campo 'palavras' com base no usuário fornecido.
    """
    class Meta:
        model = Frase
        fields = ['palavras', 'frase', 'traducao_frase', 'dificuldade']

    def __init__(self, user, *args, **kwargs):
        super(FraseForm, self).__init__(*args, **kwargs)
        # Filtrar as palavras do usuário atual
        self.fields['palavras'].queryset = Palavra.objects.filter(usuario=user)


class PalavraUpdateForm(forms.ModelForm):
    """
    Formulário para atualizar uma palavra existente.

    Este formulário é um ModelForm para o modelo Palavra, com os campos 'palavra', 'traducao' e 'dificuldade'.
    """
    class Meta:
        model = Palavra
        fields = ['palavra', 'traducao', 'dificuldade']

class FraseUpdateForm(forms.ModelForm):
    """
    Formulário para atualizar uma frase existente.

    Este formulário é um ModelForm para o modelo Frase, com os campos 'frase', 'traducao_frase' e 'dificuldade'.
    """
    class Meta:
        model = Frase
        fields = ['frase', 'traducao_frase', 'dificuldade']


