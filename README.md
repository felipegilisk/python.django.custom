# python.django

- comandos para executar:
1. Instalar a biblioteca de ambiente virtual
```
pip install virtualenv
```

2. Criar o ambiente virtual
```
virtualenv venv
```

3. Ambiente Virtual:
- Ativar
    ```
    venv\Scripts\Activate
    ```
    - Desativar
    ```
    deactivate
    ```


4. Instalar as dependências do projeto (no ambiente virtual)
```
pip install -r requirements.txt
```

5. Serviço do django
- Iniciar
    ```
    python manage.py runserver
    ```
- Interromper
    CTRL+C no terminal

6. Para criar um app chamado 'funcionarios':
    ```
    python manage.py startapp funcionarios
    ```

7. Criar uma página nova:
- Inserir um arquivo HTML na pasta templates, respeitando a governança
- Criar uma função no arquivo views.py do app (ex: core/views.py)
- Incluir o arquivo HTML no retorno da função criada
- Opcional:
• Realizar a consulta no BD (ex: Veiculos.objects.all() )
• Enviar as informações do BD no retorno da função criada
- Incluir os dados da nova página em urls.py, no mesmo app da view (ex: core/urls.py)

