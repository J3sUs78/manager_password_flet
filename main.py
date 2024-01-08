import flet as ft
from src.user import Usuario

def main(pg: ft.Page):
    pg.title = "AutoMSG"
    pg.bgcolor = "#200E3A"
    pg.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"
    }
    pg.theme = ft.Theme(font_family="zpix")
    def page_resize(e):
        pw.value = f"{pg.width} px"
        pw.update()

    pg.on_resize = page_resize
    pw = ft.Text(bottom=50, right=50, style="displaySmall")

    pg.overlay.append(pw)


    def setContact(e):
        if not txt_name.value and not txt_number.value and not txt_message.value:
            txt_name.error_text = "Porfavor Ingresa el nombre, se amable..."
            txt_number.error_text = "Porfavor Ingresa el numero, se amable..."
            txt_message.error_text = "Porfavor Ingresa el mensaje, se amable..."
            pg.update()
        else:
            user = Usuario(txt_name.value,txt_number.value,txt_message.value)
            
            pg.clean()
            pg.add(ft.Text(f"Hola, Bienvenido... {user.nombre}!"))
            


    txt_name = ft.TextField(label="Nombre ", col={"md": 4},bgcolor="#38419D")
    txt_number= ft.TextField(label="Numero", col={"md": 4},bgcolor="#38419D")
    txt_message = ft.TextField(label="Mensaje", max_lines=25, col={"md": 4},bgcolor="#38419D")



    pg.add(
        ft.ResponsiveRow([
            ft.Container(
                ft.Text("Bienvenido, Registra tu primer contacto",style=ft.TextThemeStyle.TITLE_MEDIUM),
                padding=5,
                bgcolor= "#3887BE",
                col={"sm": 6, "md": 4, "xl": 2},
                border_radius=50,
            
            )
        ]),
        ft.ResponsiveRow(
            [txt_name, txt_number, txt_message],
            run_spacing={"xs": 10},
        ),
        ft.ElevatedButton("Registrar!", on_click=setContact, bgcolor="#38419D",color="#52D3D8"),
    )
    page_resize(None)



ft.app(target=main)
