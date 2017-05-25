from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.graphics import Line, Color, Rectangle
from kivy.uix.bubble import Bubble
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty, StringProperty

store = JsonStore('academia.json')
class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)
		
	def abrir(self, *args):#preciso jogar esta funcao no primeiro screen, para que eu possa executa la quando for mudar de pagina
#-----------jogar em outra janela---------#
		try:
			treino = self.manager.get_screen('tres')#talvez seja uma boa ideia executar esta funcao ao mudar de pagina, ao inves de abrir o app
			treino.ids.a0.text = store.get('aquecimento0')['velocidade']
			treino.ids.a1.text = store.get('aquecimento0')['tempo']
			treino.ids.a2.text = store.get('aquecimento1')['velocidade']
			treino.ids.a3.text = store.get('aquecimento1')['tempo']
			#biceps#
			treino.ids.p0.text = store.get('biceps0')['series']
			treino.ids.p1.text = store.get('biceps0')['repeticoes']
			treino.ids.r0.text = store.get('biceps1')['series']
			treino.ids.r1.text = store.get('biceps1')['repeticoes']
			treino.ids.ri0.text = store.get('biceps2')['series']
			treino.ids.ri1.text = store.get('biceps2')['repeticoes']
			#peito#
			treino.ids.s0.text = store.get('peito0')['series']
			treino.ids.s1.text = store.get('peito0')['repeticoes']
			treino.ids.si0.text = store.get('peito1')['series']
			treino.ids.si1.text = store.get('peito1')['repeticoes']
			treino.ids.v0.text = store.get('peito2')['series']
			treino.ids.v1.text = store.get('peito2')['repeticoes']
			#perna#
			treino.ids.lp0.text = store.get('perna0')['series']
			treino.ids.lp1.text = store.get('perna0')['repeticoes']
			treino.ids.ps0.text = store.get('perna1')['series']
			treino.ids.ps1.text = store.get('perna1')['repeticoes']
			treino.ids.pp0.text = store.get('perna2')['series']
			treino.ids.pp1.text = store.get('perna2')['repeticoes']
			self.manager.current = 'tres'
		except:
			pass
		
class SegundoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dois'
		super(Screen,self).__init__(**kwargs)
		
	def salva(self):
		#aquecimento#
		aquecimento0 = self.ids.a0.text 
		aquecimento1 = self.ids.a1.text
		aquecimento2 = self.ids.a2.text
		aquecimento3 = self.ids.a3.text
		store.put('aquecimento0', velocidade=aquecimento0, tempo=aquecimento1)
		store.put('aquecimento1', velocidade=aquecimento2, tempo=aquecimento3)
		#biceps#
		puxador0 = self.ids.p0.text
		puxador1 = self.ids.p1.text
		roscadireta0 = self.ids.r0.text
		roscadireta1 = self.ids.r1.text
		roscainvertida0 = self.ids.ri0.text
		roscainvertida1 = self.ids.ri1.text
		store.put('biceps0', series=puxador0, repeticoes=puxador1)
		store.put('biceps1', series=roscadireta0, repeticoes=roscadireta1)
		store.put('biceps2', series=roscainvertida0, repeticoes=roscainvertida1)
		#peito#
		supino0 = self.ids.s0.text
		supino1 = self.ids.s1.text
		supinoi0 = self.ids.si0.text
		supinoi1 = self.ids.si1.text
		voador0 = self.ids.v0.text
		voador1 = self.ids.v1.text
		store.put('peito0', series=supino0, repeticoes=supino1)
		store.put('peito1', series=supinoi0, repeticoes=supinoi1)
		store.put('peito2', series=voador0, repeticoes=voador1)
		#perna#
		legpress0 = self.ids.lp0.text
		legpress1 = self.ids.lp1.text
		panturrilhas0 = self.ids.ps0.text
		panturrilhas1 = self.ids.ps1.text
		panturrilhap0 = self.ids.pp0.text
		panturrilhap1 = self.ids.pp1.text
		store.put('perna0', series=legpress0, repeticoes=legpress1)
		store.put('perna1', series=panturrilhas0, repeticoes=panturrilhas1)
		store.put('perna2', series=panturrilhap0, repeticoes=panturrilhap1)
	def abrir(self, *args):#preciso jogar esta funcao no primeiro screen, para que eu possa executa la quando for mudar de pagina
		#-----------jogar em outra janela---------#
		treino = self.manager.get_screen('tres')#talvez seja uma boa ideia executar esta funcao ao mudar de pagina, ao inves de abrir o app
		treino.ids.a0.text = store.get('aquecimento0')['velocidade']
		treino.ids.a1.text = store.get('aquecimento0')['tempo']
		treino.ids.a2.text = store.get('aquecimento1')['velocidade']
		treino.ids.a3.text = store.get('aquecimento1')['tempo']
		#biceps#
		treino.ids.p0.text = store.get('biceps0')['series']
		treino.ids.p1.text = store.get('biceps0')['repeticoes']
		treino.ids.r0.text = store.get('biceps1')['series']
		treino.ids.r1.text = store.get('biceps1')['repeticoes']
		treino.ids.ri0.text = store.get('biceps2')['series']
		treino.ids.ri1.text = store.get('biceps2')['repeticoes']
		#peito#
		treino.ids.s0.text = store.get('peito0')['series']
		treino.ids.s1.text = store.get('peito0')['repeticoes']
		treino.ids.si0.text = store.get('peito1')['series']
		treino.ids.si1.text = store.get('peito1')['repeticoes']
		treino.ids.v0.text = store.get('peito2')['series']
		treino.ids.v1.text = store.get('peito2')['repeticoes']
		#perna#
		treino.ids.lp0.text = store.get('perna0')['series']
		treino.ids.lp1.text = store.get('perna0')['repeticoes']
		treino.ids.ps0.text = store.get('perna1')['series']
		treino.ids.ps1.text = store.get('perna1')['repeticoes']
		treino.ids.pp0.text = store.get('perna2')['series']
		treino.ids.pp1.text = store.get('perna2')['repeticoes']
		self.manager.current = 'tres' 
class TerceiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'tres'
		super(Screen,self).__init__(**kwargs)
		
	
class RootScreen(ScreenManager):
    pass
    
class topApp(App):
	title = 'Teste Json!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = topApp()
    topApp().run()
