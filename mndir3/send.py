from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
Builder.load_string("""
<Base>:
	Button:
		background_normal: 'images(2).jpg'
   	 background_down: 'images(4).jpg'
 	   border: 30,30,30,30
	GridLayout:
		rows:2	   
		Button:
			text:'a'
		Button:
			text:'b'
		GridLayout:
			rows:2
			Button:
			Button:
			Button:
			Button:
			Button:
			Button:
		
""")


class Base(BoxLayout):
    pass

class ButtonsApp(App):
    def build(self):
        return Base()

if __name__ == "__main__":
    ButtonsApp().run()