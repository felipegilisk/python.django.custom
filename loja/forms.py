from django import forms


class ProdutoForm(forms.Form):
    nome_produto = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "digite o nome do produto"
            }
        )
    )

    descricao_produto = forms.CharField(
        label="Descrição",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "digite a descricao do produto"
            }
        )
    )

    preco_produto = forms.FloatField(
        label="Preço",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': "form-control",
                'placeholder': "0.0"
            }
        )
    )

