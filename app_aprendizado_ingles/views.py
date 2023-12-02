from django.shortcuts import get_object_or_404, render
from .models import Palavra, Frase, VerbosConjugacao
from django.shortcuts import render, redirect
from .forms import PalavraForm, FraseForm, PalavraUpdateForm, FraseUpdateForm
from .models import Palavra, Frase
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def adicionar_palavra(request): 
    """
    View para adicionar uma nova palavra ao banco de dados.

    Método:
    - Adiciona a palavra associada ao usuário logado.
    - Redireciona para a página de adição de palavra após a conclusão.

    Template: 'formulario/adicionar_palavra.html'
    """
    if request.method == 'POST':
        form = PalavraForm(request.POST)
        if form.is_valid():
            nova_palavra = form.save(commit=False)
            nova_palavra.usuario = request.user  # Associa a palavra ao usuário logado
            nova_palavra.save()
            return redirect('adicionar_palavra')
    else:
        form = PalavraForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'formulario/adicionar_palavra.html', context)



@login_required
def adicionar_frase(request):
    """
    View para adicionar uma nova frase ao banco de dados.

    Método:
    - Adiciona a frase associada ao usuário logado.
    - Redireciona para a página de adição de frase após a conclusão.

    Template: 'formulario/adicionar_frase.html'
    """
    if request.method == 'POST':
        form = FraseForm(request.user, request.POST)
        if form.is_valid():
            nova_frase = form.save(commit=False)
            nova_frase.usuario = request.user  # Defina o usuário atual
            nova_frase.save()
            return redirect('adicionar_frase')
    else:
        form = FraseForm(user=request.user)  # Passe o usuário como um argumento
    
    frases = Frase.objects.filter(usuario=request.user)
    return render(request, 'formulario/adicionar_frase.html', {'form': form, 'frases': frases})



@login_required
def pagina_inicial(request):
    """
    Página inicial que exibe palavras e frases aprendidas e adicionadas pelo usuário.

    Contexto:
    - palavras_aprendidas: Palavras aprendidas pelo usuário.
    - frases: Frases adicionadas pelo usuário.
    - palavras_adicionadas: Todas as palavras adicionadas pelo usuário.

    Template: 'Visualizar_tudo/home.html'
    """
    # Filtrar palavras aprendidas pelo usuário logado
    palavras_aprendidas = Palavra.objects.filter(palavra_aprendida=True, usuario=request.user)

    # Filtrar frases aprendidas pelo usuário logado
    frases = Frase.objects.filter(usuario=request.user)

    # Filtrar palavras adicionadas pelo usuário logado
    palavras_adicionadas = Palavra.objects.filter(usuario=request.user)

    context = {
        'palavras_aprendidas': palavras_aprendidas,
        'frases': frases,
        'palavras_adicionadas': palavras_adicionadas,
    }
    
    return render(request, 'Visualizar_tudo/home.html', context)


@login_required
def ver_frases(request):
    """
    Visualiza frases adicionadas pelo usuário, organizadas por palavras associadas.

    Contexto:
    - frases_por_palavra: Dicionário que mapeia palavras para suas frases associadas.

    Template: 'Visualizar_tudo/ver_mais_frase.html'
    """
    frases = Frase.objects.filter(usuario=request.user)

    # Organizar as frases por palavra
    frases_por_palavra = {}
    for frase in frases:
        if frase.palavras not in frases_por_palavra:
            frases_por_palavra[frase.palavras] = [frase]
        else:
            frases_por_palavra[frase.palavras].append(frase)

    return render(request, 'Visualizar_tudo/ver_mais_frase.html', {'frases_por_palavra': frases_por_palavra})


@login_required
def frases_com_palavra(request, palavra_id):
    """
    Visualiza frases associadas a uma palavra específica.

    Parâmetros:
    - palavra_id: ID da palavra para a qual as frases devem ser exibidas.

    Contexto:
    - palavra: A palavra associada às frases.
    - frases: Frases associadas à palavra.

    Template: 'tipo_de_filtragem/frase_com_palavras.html'
    """
    palavra = get_object_or_404(Palavra, id=palavra_id)
    frases = Frase.objects.filter(palavras=palavra)
    return render(request, 'tipo_de_filtragem/frase_com_palavras.html', {'palavra': palavra, 'frases': frases})


@login_required
def update_palavra(request, palavra_id):
    """
    View para atualizar uma palavra existente.

    Parâmetros:
    - palavra_id: ID da palavra a ser atualizada.

    Método:
    - Obtém a palavra do banco de dados.
    - Se a solicitação for POST, valida o formulário e salva as alterações.
    - Redireciona para a página de atualização após a conclusão.

    Template: 'formulario/update_palavra.html'
    """
    palavra = get_object_or_404(Palavra, id=palavra_id)
    if request.method == 'POST':
        form = PalavraUpdateForm(request.POST, instance=palavra)
        if form.is_valid():
            form.save()
            return redirect('update_palavra')
    else:
        form = PalavraUpdateForm(instance=palavra)
    return render(request, 'formulario/update_palavra.html', {'form': form, 'palavra': palavra})


@login_required
def update_frase(request, frase_id):
    """
    View para atualizar uma frase existente.

    Parâmetros:
    - frase_id: ID da frase a ser atualizada.

    Método:
    - Obtém a frase do banco de dados.
    - Se a solicitação for POST, valida o formulário e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Template: 'formulario/update_frase.html'
    """
    frase = get_object_or_404(Frase, id=frase_id)
    if request.method == 'POST':
        form = FraseUpdateForm(request.POST, instance=frase)
        if form.is_valid():
            form.save()
            return redirect('frases_com_palavra', palavra_id=frase.palavras_id)  # Redirecionar para a página correta
    else:
        form = FraseUpdateForm(instance=frase)
    return render(request, 'formulario/update_frase.html', {'form': form, 'frase': frase})


@login_required
def delete_frase(request, frase_id):
    """
    View para excluir uma frase existente.

    Parâmetros:
    - frase_id: ID da frase a ser excluída.

    Método:
    - Obtém a frase do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da frase.
    - Deleta a frase do banco de dados.
    - Redireciona para a página correta após a exclusão.

    Redireciona para: 'todas_frases' (ou outra página desejada).
    """
    frase = get_object_or_404(Frase, id=frase_id)
    if frase.usuario == request.user:
        # Deleta a frase do banco de dados
        frase.delete()
        return redirect('todas_frases')  # Redireciona para a página de todas as frases ou onde preferir


@login_required
def todas_palavras_aprendidas(request):
    """
    View para exibir todas as palavras aprendidas pelo usuário.

    Contexto:
    - palavras_aprendidas: Palavras marcadas como aprendidas.

    Template: 'aprendidas/palavras_aprendidas.html'
    """
    palavras_aprendidas = Palavra.objects.filter(palavra_aprendida=True)
    context = {'palavras_aprendidas': palavras_aprendidas}
    return render(request, 'aprendidas/palavras_aprendidas.html', context)


@login_required
def todas_minhas_palavras(request):
    """
    View para exibir todas as palavras adicionadas pelo usuário.

    Contexto:
    - page: Página paginada contendo palavras do usuário.

    Template: 'Visualizar_tudo/todas_palavras.html'
    """
    palavras = Palavra.objects.filter(usuario=request.user)

    paginacao = Paginator(palavras, 2)
    num_page = request.GET.get('page')
    page = paginacao.get_page(num_page)
    return render(request, 'Visualizar_tudo/todas_palavras.html', {'page': page})


@login_required
def delete_palavra(request, palavra_id):
    """
    View para excluir uma palavra existente.

    Parâmetros:
    - palavra_id: ID da palavra a ser excluída.

    Método:
    - Obtém a palavra a ser excluída ou retorna 404 se não existir.
    - Verifica se o usuário autenticado é o proprietário da palavra.
    - Exclui a palavra do banco de dados.
    - Redireciona para a página correta após a exclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    # Obtenha a palavra a ser excluída ou retorne 404 se não existir
    palavra = get_object_or_404(Palavra, pk=palavra_id)

    # Verifique se o usuário autenticado é o proprietário da palavra
    if palavra.usuario == request.user:
        # Exclua a palavra
        palavra.delete()
        return redirect('todas_minhas_palavras')


@login_required
def frases_aprendidas(request):
    """
    View para marcar uma palavra como aprendida.

    Parâmetros:
    - palavra_id: ID da palavra a ser marcada como aprendida.

    Método:
    - Obtém a palavra do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da palavra.
    - Marca a palavra como aprendida e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavras_aprendidas = Frase.objects.filter(frase_aprendida=True)
    context = {'palavras_aprendidas': palavras_aprendidas}
    return render(request, 'app_aprendizado_ingles/palavras_aprendidas.html', context)


@login_required
def verbos_aprendidos(request):
    """
    View para exibir todos os verbos aprendidos pelo usuário.

    Contexto:
    - palavras_aprendidas: Verbos marcados como aprendidos.

    Template: 'app_aprendizado_ingles/palavras_aprendidas.html'
    """
    palavras_aprendidas = VerbosConjugacao.objects.filter(verbos_aprendido=True)
    context = {'palavras_aprendidas': palavras_aprendidas}
    return render(request, 'app_aprendizado_ingles/palavras_aprendidas.html', context)


@login_required
def marcar_como_aprendida(request, palavra_id):
    """
    View para marcar uma palavra como aprendida.

    Parâmetros:
    - palavra_id: ID da palavra a ser marcada como aprendida.

    Método:
    - Obtém a palavra do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da palavra.
    - Marca a palavra como aprendida e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(Palavra, pk=palavra_id)
    if (palavra.usuario == request.user):
        palavra.palavra_aprendida = True
        palavra.save()
        return redirect('todas_minhas_palavras')
    

@login_required
def desmarcar_como_aprendida(request, palavra_id):
    """
    View para desmarcar uma palavra como aprendida.

    Parâmetros:
    - palavra_id: ID da palavra a ser desmarcada como aprendida.

    Método:
    - Obtém a palavra do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da palavra.
    - Atualiza a palavra_aprendida para False e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(Palavra, id=palavra_id)
    # Atualize a palavra_aprendida para False
    if palavra.usuario == request.user:
        palavra.palavra_aprendida = False
        palavra.save()
        return redirect('todas_minhas_palavras')


@login_required
def marcar_frase_como_aprendida(request, palavra_id):
    """
    View para marcar uma frase como aprendida.

    Parâmetros:
    - palavra_id: ID da frase a ser marcada como aprendida.

    Método:
    - Obtém a frase do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da frase.
    - Marca a frase como aprendida e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(Frase, pk=palavra_id)
    if (palavra.usuario == request.user):
        palavra.frase_aprendida = True
        palavra.save()
        return redirect('todas_minhas_palavras')
    

@login_required
def desmarcar_frase_como_aprendida(request, palavra_id):
    """
    View para desmarcar uma frase como aprendida.

    Parâmetros:
    - palavra_id: ID da frase a ser desmarcada como aprendida.

    Método:
    - Obtém a frase do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da frase.
    - Atualiza a frase_aprendida para False e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(Frase, id=palavra_id)
    if palavra.usuario == request.user:
        palavra.frase_aprendida = False
        palavra.save()
        return redirect('todas_minhas_palavras')


@login_required
def marcar_conjugacoes_como_aprendida(request, palavra_id):
    """
    View para marcar uma conjugação verbal como aprendida.

    Parâmetros:
    - palavra_id: ID da conjugação verbal a ser marcada como aprendida.

    Método:
    - Obtém a conjugação verbal do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da conjugação.
    - Marca a conjugação como aprendida e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(VerbosConjugacao, pk=palavra_id)
    if (palavra.usuario == request.user):
        palavra.verbos_aprendido = True
        palavra.save()
        return redirect('todas_minhas_palavras')
    

@login_required
def desmarcar_conjugacoes_como_aprendida(request, palavra_id):
    """
    View para desmarcar uma conjugação verbal como aprendida.

    Parâmetros:
    - palavra_id: ID da conjugação verbal a ser desmarcada como aprendida.

    Método:
    - Obtém a conjugação verbal do banco de dados.
    - Verifica se o usuário autenticado é o proprietário da conjugação.
    - Atualiza a verbos_aprendido para False e salva as alterações.
    - Redireciona para a página correta após a conclusão.

    Redireciona para: 'todas_minhas_palavras' (ou outra página desejada).
    """
    palavra = get_object_or_404(VerbosConjugacao, id=palavra_id)
    if palavra.usuario == request.user:
        palavra.verbos_aprendido = False
        palavra.save()
        # Redirecione para a página ou URL apropriada após a atualização
        return redirect('todas_minhas_palavras')
