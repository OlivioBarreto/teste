import flet as ft

def main(page: ft.Page):
    # define a finçÃO para manipular o clique do botão
    def clicar_botão(e):
        text.value = "Olá, Flet"
        page.update()
    
    # cria um texto inicial
    text = ft.Text(value="Clique no botão abaixo!")
    #  # Cria um botão que chama a função button_clicked quando clicado
    botao = ft.ElevatedButton(text="Clique aqui", on_click=clicar_botão)

    # Adiciona os componentes à página
    page.add(text, botao)

ft.app(target=main)