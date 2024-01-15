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

3. Ativar o ambiente virtual
```
venv\Scripts\Activate
```

4. Instalar as dependências do projeto (no ambiente virtual)
```
pip install -m requirements.txt
```

5. Acionar o serviço do django
```
python manage.py runserver
```


- Desativar o ambiente virtual:
    ```
    deactivate
    ```
- Desativar o servidor django: CTRL+C no terminal

- Para criar um app chamado 'galeria':
    ```
    python manage.py startapp galeria
    ```
