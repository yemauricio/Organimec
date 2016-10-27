# kivy.requier("1.9.1")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager

#Generar las pantallas necesarias
Builder.load_string("""
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition

# Menu de inicio que muestra las funciones de la aplicacion

<MenuScreen>:
    canvas.before:
        Color: 
            rgba: 153./255.,167./255.,244./255.,0.5
        Rectangle:
            source:'background.png'
            size: self.size
            
    BoxLayout:
        pos: root.x + 0.8*self.width, root.y + 1.85*self.height
        size_hint: 0.4, 0.3

        Button:
            text: 'Medicamentos'
            on_press: root.manager.current = 'Medicamentos'
            background_normal: 'medicine.png' 
            on_release: root.manager.transition = RiseInTransition()
            
    BoxLayout:
    
        pos: root.x + 1.06*self.width, root.y + 0.4*self.height
        size_hint: 0.3, 0.4

        Button:
            text: 'Citas Medicas'
            on_press: root.manager.current = 'CitasMedicas'
            on_release: root.manager.transition = RiseInTransition()
            background_normal: 'citamedica.png' #imagen cargada para el boton


# Pantalla de la funcion 'medicamentos', que muestra los botones y
# la pantalla para cada uno      

<Medicamentos>:

    BoxLayout:
    
        pos: root.x - 0.1*self.width, root.y + 9*self.height
        size_hint: 0.1,0.1
        
        Button:
            text: 'menu'
            on_press: root.manager.current = 'Menu'
            background_normal: 'menu.png'
            background_color: (1,1,0,0.5)
            on_release: root.manager.transition = RiseInTransition()
            
    BoxLayout:
    
        pos: root.x + 0.3*self.width, root.y + 9*self.height
        size_hint: 0.3,0.1
        
        Button:
            background_color:(0.5,0.6,0.4,0.6)
            text: 'Nuevo'
            Button:
                text:'Enter'

    
    BoxLayout:
    
        pos: root.x + 1.3*self.width, root.y + 9*self.height
        size_hint: 0.3,0.1
        
        Button:
            background_color:(0.5,0.6,0.4,0.6)
            text: 'Existentes'

    BoxLayout:
    
        pos: root.x + 2.3*self.width, root.y + 9*self.height
        size_hint: 0.3,0.1
        
        Button:
            background_color:(0.5,0.6,0.4,0.6)
            text: 'Calendario'


           

<CitasMedicas>:

    BoxLayout:
    
        Button:
            text: 'Funciones citas'
            
        Button:
            text: 'menu'
            background_normal: 'menu.png' #imagen cargada para el boton
            on_press: root.manager.current = 'Menu'
            on_release: root.manager.transition = RiseInTransition()

""")

class MenuScreen(Screen):
    ''' Pantalla de inicio Menu '''
    pass

class Medicamentos(Screen):
    ''' Pantalla de Medicamentos '''
    pass

class CitasMedicas(Screen):
    ''' Pantalla de Citas Medicas '''
    pass

class Contenedor(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''
    container = ObjectProperty(None)
    
ScreenManager = ScreenManager()
ScreenManager.add_widget(MenuScreen(name = 'Menu'))
ScreenManager.add_widget(Medicamentos(name = 'Medicamentos'))
ScreenManager.add_widget(CitasMedicas(name = 'CitasMedicas'))


class Application(App):
    def build(self):
        return ScreenManager
    

if __name__ == '__main__':
    Application().run()


