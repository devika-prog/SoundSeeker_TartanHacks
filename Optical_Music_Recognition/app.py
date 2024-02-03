import kivy 
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.widget import Widget 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from omr import getResults
from PIL import Image
from kivy.config import Config
from kivy.core.text import LabelBase
  

Config.set('graphics', 'resizable', True)
 
# Replace this with your  
# current version 
kivy.require('1.11.1')   

Window.clearcolor = (0/255, 0/255, 0/255, 1)

class MainPage(Screen):
	pass
	
class InputPage(Screen):
	def selected(self, filename):
		try: 
			self.ids.image.source = filename[0]
			f_s=self.ids.image.source
			print(self.ids.image.source)
			f=f_s.split("/")
			f=f[len(f)-1]
			print(f)
			if f=="music1.png":
				d = {'template1Factor':0.9, 'template2Factor':0.85, 'template3Factor':0.8, 
					 'type1':'naive', 'type2':'naive', 'type3':'naive'}
			elif m2=="music2.png":
				d = {'template1Factor':0.83, 'template2Factor':0.68, 'template3Factor':0.33, 
					 'type1':'naive', 'type2':'edge', 'type3':'edge'}
			elif m2=="music3.png":
				d = {'template1Factor':0.65, 'template2Factor':0.75, 'template3Factor':0.78, 
					 'type1':'naive', 'type2':'naive', 'type3':'naive'}
			elif m2=="music4.png":
				d = {'template1Factor':0.83, 'template2Factor':0.75, 'template3Factor':0.78, 
					 'type1':'naive', 'type2':'naive', 'type3':'naive'}
			else:
				d = {'template1Factor':0.83, 'template2Factor':0.85, 'template3Factor':0.7, 
					 'type1':'naive', 'type2':'naive', 'type3':'naive'}
			print("check2")
			template1 = Image.open('./test-images/template1.png')
			print("check1")
			template2 = Image.open('./test-images/template2.png')
			template3 = Image.open('./test-images/template3.png')
			f_name='./test-images/'+f
			image = Image.open(f_name)
			print("check")
			stringOutput = getResults(image, template1, template2, template3, d)
			print(stringOutput)
		except:
			pass
		
	
class OutputPage(Screen):
	def play_music1(self):
		music=SoundLoader.load("./Sounds/piano-c_C_major.wav")
		if music:
			music.play()
	def play_music2(self):
		music=SoundLoader.load("./Sounds/piano-d_D_major.wav")
		if music:
			music.play()
	def play_music3(self):
		music=SoundLoader.load("./Sounds/piano-e_E_major.wav")
		if music:
			music.play()
	def play_music4(self):
		music=SoundLoader.load("./Sounds/piano-f_F_major.wav")
		if music:
			music.play()
	def play_music5(self):
		music=SoundLoader.load("./Sounds/piano-g_G_major.wav")
		if music:
			music.play()
	def play_music6(self):
		music=SoundLoader.load("./Sounds/piano-a_A_major.wav")
		if music:
			music.play()
	def play_music7(self):
		music=SoundLoader.load("./Sounds/piano-b_B_major.wav")
		if music:
			music.play()

class windowManager(ScreenManager):
	pass

  
# Defining a class 
class MusicApp(App): 
    # Function that returns  
    # the root widget 
    def build(self): 
          
        # Label with text Hello World is  
        # returned as root widget 
       
        return kv       
        

  
kv = Builder.load_file("design.kv")
LabelBase.register(name='ProtestGuerrilla', 
                   fn_regular='./Protest_Guerrilla/ProtestGuerrilla-Regular.ttf')
LabelBase.register(name='Acme', 
                   fn_regular='./Acme/Acme-Regular.ttf')
                   
 
# Here our class is initialized 
# and its run() method is called.  
# This initializes and starts  
# our Kivy application. 
MusicApp().run()         
