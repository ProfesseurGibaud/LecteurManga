import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.core.window import Window



OnOff = 0
Compteur = 0
path = r"C:\Users\Sylgi\Desktop\Manga"

with open(os.path.join(path,"En_Cours.txt"),"r") as file:
    M = file.read()
    path = os.path.join(path,M)

sm = ScreenManager()
Liste = os.listdir(path)

def Nextt():
    global Compteur,Liste,OnOff
    if OnOff == 0: # On passe à la slide suivante sans modifier compteur
         ScreenImpairr.Maj()
         sm.current = "Impair"
         OnOff = 1
    else:
        Compteur += 1
        ScreenPairr.Maj()
        sm.current = "Pair"
        OnOff = 0

if "Save.txt" in os.listdir(path):
    with open(os.path.join(path, "Save.txt"), "r") as file:
        Compteur = int(file.read())
else:
    Compteur = 0

def _on_keyboard_handler(instance, key, scancode, codepoint, modifiers):
    global Compteur
    Nextt()
    with open(os.path.join(path,"Save.txt"),"w+") as file:
        file.write(str(Compteur))

def _on_touch_handler(instance, key):
    global Compteur
    Nextt()
    with open(os.path.join(path,"Save.txt"),"w+") as file:
        file.write(str(Compteur))

Window.bind(on_keyboard=_on_keyboard_handler)
Window.bind(on_touch_down = _on_touch_handler)

class ScreenPair(Screen):
    def build(self):
        self.name = "Pair"
        self.layout = BoxLayout()
        n = 0
        self.imgpair = Image(source = os.path.join(path,Liste[n]))
        self.layout.add_widget(self.imgpair)
        self.add_widget(self.layout)
        sm.add_widget(self)
    def Maj(self):
        global Compteur
        print(Compteur)
        n = 2*Compteur
        self.imgpair.source = os.path.join(path,Liste[n])

class ScreenImpair(Screen):
    def build(self):
        global Compteur
        self.name = "Impair"
        n = 2 * Compteur + 1

        Liste = os.listdir(path)
        self.layout = BoxLayout()
        self.imgimpair = Image(source = os.path.join(path,Liste[n]))
        self.layout.add_widget(self.imgimpair)
        self.add_widget(self.layout)
        sm.add_widget(self)
    def Maj(self):
        global Compteur
        print(Compteur)
        n = 2*Compteur + 1
        self.imgimpair.source = os.path.join(path,Liste[n])

ScreenPairr = ScreenPair()
ScreenPairr.build()
ScreenImpairr = ScreenImpair()
ScreenImpairr.build()



class ScreenApp(App):
    def build(self):
        sm.current = "Impair"
        return sm

ScreenApp().run()

