import flet as ft 

def main(page: ft.Page):
    page.title = "parColab"
    def cadastrar(e):
        print(produto.value ,  preco.value)

    txt_titulo = ft.Text('Titulo do produto:')
    produto = ft.TextField(label="Digite o titulo do produto", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )
    

ft.app(target=main)