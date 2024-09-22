import flet as ft 
from models import Produto
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

CONN = "sqlite:///parcolab.db"
engine = create_engine(CONN, echo = True) 
Session = sessionmaker(bind=engine)
session = Session()


def main(page: ft.Page):
    page.title = "Cadastro parColab"
    def cadastrar(e):
        novo_produto = Produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()
        print('Produto salvo com Sucesso!')

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