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
        # Valida los campos de texto
        if not txt_name.value:
            txt_name.error_text = "Por favor, ingresa el nombre."
        if not txt_number.value:
            txt_number.error_text = "Por favor, ingresa el número de teléfono."
        if not txt_message.value:
            txt_message.error_text = "Por favor, ingresa el mensaje."

        # Si todos los campos son válidos, crea el objeto Usuario y guárdalo en el almacenamiento
        if not any(error_text for error_text in [txt_name.error_text, txt_number.error_text, txt_message.error_text]):
            try:
                user = Usuario(txt_name.value, txt_number.value, txt_message.value)
                
                pg.client_storage.set("user", user)

                # Accediendo a los atributos del usuario almacenado
                local_user = pg.client_storage.get("user")
                
                pg.clean()
                pg.add(ft.Text(f"Local storage: {local_user}!"))
                pg.add(ft.Text(f"user created: : {user}!"))
                pg.add(ft.Text(f"Hola, Bienvenido... {local_user['_nombre']}!"))
                pg.add(ft.Text(f"Tu número de teléfono es: {local_user['_numero_de_telefono']}"))
                pg.add(ft.Text(f"Tu mensaje es: {local_user['_mensaje']}"))
            except ValueError as err:
                # Maneja los errores de validación de la clase Usuario
                message = f"Error: {err}"
                pg.clean()
                pg.add(ft.Text(message, style="error"))
        else:
            # Actualiza la página para mostrar los mensajes de error
            pg.update()



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
                margin= 80
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
