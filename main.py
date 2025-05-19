from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

from agregar import agregar_contacto
from eliminar import eliminar_contacto
from buscar import buscar_contacto
from actualizar import actualizar_contacto
from manejo_csv import leer_contactos


class ContactosApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        # Fondo azul muy claro
        with self.canvas.before:
            Color(0.9, 0.95, 1, 1)  # azul clarito
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        input_style = {
            "size_hint_y": None,
            "height": 40,
            "background_color": (1, 1, 1, 1),
            "foreground_color": (0.2, 0.2, 0.2, 1),
            "padding": [10, 10],
            "font_size": 16,
        }

        self.nombre = TextInput(hint_text='Nombre', **input_style)
        self.correo = TextInput(hint_text='Correo', **input_style)
        self.telefono = TextInput(hint_text='Teléfono', **input_style)
        

        self.add_widget(self.nombre)
        self.add_widget(self.correo)
        self.add_widget(self.telefono)

        botones = BoxLayout(size_hint_y=None, height=45, spacing=8)
        acciones = [
            ('Agregar', self.agregar),
            ('Buscar', self.buscar),
            ('Actualizar', self.actualizar),
            ('Eliminar', self.eliminar),
            ('Listar Todos', self.listar),
        ]

        color_boton = (1, 0.8, 0.9, 1)  # rosado suave visible

        for texto, funcion in acciones:
            btn = Button(
                text=texto,
                background_normal='',  # <--- esto activa el color de fondo personalizado
                background_color=color_boton,
                color=(0.2, 0.2, 0.2, 1),
                font_size=14
            )
            btn.bind(on_press=funcion)
            botones.add_widget(btn)

        self.add_widget(botones)

        self.scroll = ScrollView(size_hint=(1, 1))
        self.resultado_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.resultado_layout.bind(minimum_height=self.resultado_layout.setter('height'))
        self.scroll.add_widget(self.resultado_layout)

        self.add_widget(self.scroll)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def agregar(self, _):
        msg = agregar_contacto(self.nombre.text, self.correo.text, self.telefono.text)
        self.mostrar_mensaje(msg)
        self.limpiar()

    def buscar(self, _):
        c = buscar_contacto(self.nombre.text)
        if c:
            self.correo.text = c['correo']
            self.telefono.text = c['telefono']
            msg = f"Contacto encontrado:\n{c['nombre']} - {c['correo']} - {c['telefono']}"
        else:
            msg = "Contacto no encontrado."
        self.mostrar_mensaje(msg)

    def actualizar(self, _):
        msg = actualizar_contacto(self.nombre.text, self.correo.text, self.telefono.text)
        self.mostrar_mensaje(msg)
        self.limpiar()

    def eliminar(self, _):
        msg = eliminar_contacto(self.nombre.text)
        self.mostrar_mensaje(msg)
        self.limpiar()

    def listar(self, _):
        self.resultado_layout.clear_widgets()
        contactos = leer_contactos()
        if not contactos:
            self.mostrar_mensaje("No hay contactos.")
        else:
            tabla = GridLayout(cols=3, spacing=10, size_hint_y=None)
            tabla.bind(minimum_height=tabla.setter('height'))

            # Encabezados
            encabezados = ['Nombre', 'Correo', 'Teléfono']
            for h in encabezados:
                lbl = Label(text=f'[b]{h}[/b]', markup=True, size_hint_y=None, height=30, color=(0.1, 0.1, 0.4, 1))
                tabla.add_widget(lbl)

            for c in contactos:
                tabla.add_widget(Label(text=c['nombre'], size_hint_y=None, height=30, color=(0.2, 0.2, 0.2, 1)))
                tabla.add_widget(Label(text=c['correo'], size_hint_y=None, height=30, color=(0.2, 0.2, 0.2, 1)))
                tabla.add_widget(Label(text=c['telefono'], size_hint_y=None, height=30, color=(0.2, 0.2, 0.2, 1)))

            self.resultado_layout.add_widget(tabla)

    def mostrar_mensaje(self, mensaje):
        self.resultado_layout.clear_widgets()
        lbl = Label(text=mensaje, size_hint_y=None, height=200, color=(0.2, 0.2, 0.2, 1))
        self.resultado_layout.add_widget(lbl)

    def limpiar(self):
        self.nombre.text = ''
        self.correo.text = ''
        self.telefono.text = ''


class MiApp(App):
    def build(self):
        self.title = "Agenda de Contactos"
        return ContactosApp()


if __name__ == '__main__':
    MiApp().run()

