## Projeto Django de Aprendizado de Inglês

Este é um projeto Django destinado a ajudar na aprendizagem de inglês, permitindo aos usuários registrar palavras, frases e conjugações verbais, além de acompanhar seu progresso.


## Configuração do Ambiente

Antes de começar, certifique-se de ter o Python e o Django instalados no seu sistema. Você pode instalá-los usando o seguinte comando:

- pip install Django



## Configuração do Projeto

1. Clone este repositório para o seu ambiente local.
- git clone https://github.com/seu-usuario/nome-do-repositorio.git


2. Navegue até o diretório do projeto.
- cd nome-do-repositorio


3. Crie um ambiente virtual para o projeto.

- python -m venv venv


4. Ative o ambiente virtual.

- No Windows:
    - venv\Scripts\activate

- No Linux/Mac:
    - source venv/bin/activate


5. Instale as dependências do projeto.
    - pip install -r requirements.txt


6. Execute as migrações do banco de dados.
    - python manage.py migrate

7. Crie um superusuário para acessar o painel de administração.
    - python manage.py createsuperuser


8. Inicie o servidor de desenvolvimento.
    - python manage.py runserver
        O projeto estará disponível em http://localhost:8000/.

## Funcionalidades

# Registro de Palavras

- Adicione palavras em inglês, suas traduções e níveis de dificuldade.
- Acompanhe se você aprendeu ou não cada palavra.


# Registro de Frases

- Registre frases em inglês, suas traduções e níveis de dificuldade.
- Associe frases a palavras específicas para um aprendizado contextual.


# Conjugação de Verbos
- Pratique a conjugação de verbos em inglês, acompanhando suas dificuldades e progresso.

# Acompanhamento de Progresso
- Visualize palavras e frases aprendidas.
- Acompanhe o seu progresso na conjugação de verbos.


## Contribuição
Sinta-se à vontade para contribuir para o desenvolvimento deste projeto. Se encontrar problemas ou tiver sugestões, abra uma issue. Pull requests são bem-vindos!