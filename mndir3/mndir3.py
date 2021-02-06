from kivy.app import App
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config
Config.set('graphics','resizable',True)
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty,ListProperty,ObjectProperty
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import sqlite3 as sql
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from functools import partial
from kivymd.uix.card import MDCardSwipe

#con=sql.connect('students_detail.db')
#cur=con.cursor()
#cur.execute("""CREATE TABLE students(
		#	fname text,
#			lname text,
#			mobile int,
#			address text,
#			email text,
#			age int,
#			dob text,
#			bmark text,
#			gender text,
#			nationality text,
#			catogery text)
#			""")
#con.commit()
#con.close()


Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory

<buttons>:
	FloatLayout:
		canvas.before:
			Color:
        	    rgba:
			Rectangle:
				pos: self.pos
            	size: self.size
            	source:'images(5).jpg' 
		
		Image:
			source:'kisspng-rapunzel-scalable-vector-graphics-icon-cartoon-princess-tower-5a7be.png'
			size_hint:.7,1
			pos_hint:{'x':-.1,'y':.1}
            		
		Label:
			text:'User_Name'
			font_size:35
			pos_hint:{'x':.5,'center_y':1.2}
			color:0,0,0,1
			text_size:self.size
			
		TextInput:
			id:username
			size_hint_x:.4
			size_hint_y:.06
			pos_hint:{'x':.51,'center_y':.635}
			font_size:30
			color:0,0,0,1
			background_color:0,0,0,0
			multiline:False
			
		Label:
			text:'_________________________'
			pos_hint:{'x':.5,'center_y':1.12}
			color:0,0,0,1
			text_size:self.size
			
		Label:
			text:'Password'
			font_size:35
			pos_hint:{'x':.5,'center_y':1}
			color:0,0,0,1
			text_size:self.size
		TextInput:
			id:pwd
			size_hint_x:.4
			size_hint_y:.06
			pos_hint:{'x':.51,'center_y':.435}
			color:0,0,0,1
			background_color:0,0,0,0
			multiline:False
		
		Label:
			text:'_________________________'
			pos_hint:{'x':.5,'center_y':.92}
			color:0,0,0,1
			text_size:self.size
			
		Button:
			text:'LOG IN'
			size_hint_x:.27
			size_hint_y:.07
			pos_hint:{'x':.5,'center_y':.3}
			background_color:1,1,1,0.2
			border:1,0,0,5
			color:0,0,0,1
			bold:True
			on_release:
				root.manager.current='screen' if username.text=='shivam' and pwd.text=='semwal' else 'button'
				root.manager.transition.direction='left'
		Button:
			text:''
			size_hint:.06,.04
			pos_hint:{'x':.07,'y':.73}
			background_color:0,0,0,0
			on_press:
				root.manager.current='screen'
				root.manager.transition.direction='left'
<screen2>:
	FloatLayout:
		canvas:
			Rectangle:
				size:self.size
				pos:self.pos
				source:'crm.jpg'
		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		FloatLayout:
            pos_hint:{'x':0.050,'y':.010}
            size_hint:.900,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	Label:
		text:'Drsh_Sem'
		font_size:65
		pos_hint:{'x':.0,'y':.445}
		bold:True
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True

	Label:
		text:'Students'
		font_size:35
		pos_hint:{'x':-.29,'y':.17}
		color:0,0,0,1
			
	Label:
		text:'Search'
		font_size:35
		pos_hint:{'x':.27,'y':.17}
		color:0,0,0,1
		
	Label:
		text:'Transport'
		font_size:35
		pos_hint:{'x':-.29,'y':-.077}
		color:0,0,0,1
		
	Label:
		text:'Fee Structure'
		font_size:35
		pos_hint:{'x':.27,'y':-.077}
		color:0,0,0,1
		
	Label:
		text:'Teachers'
		font_size:35
		pos_hint:{'x':-.29,'y':-.33}
		color:0,0,0,1
		
	Label:
		text:'Acessories'
		font_size:35
		pos_hint:{'x':.27,'y':-.33}
		color:0,0,0,1
		
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'delete-icon-ios-19.jpg'
		pos_hint:{'x':.04,'y':.03}
		background_color:0,1,0,.4
		on_release:app.stop()
	
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'free-black-left-arrow-icon-png-vector-241709.png'
		pos_hint:{'x':.75,'y':.03}
		background_color:0,1,0,.4
		on_release:
			root.manager.current='button'
			root.manager.transition.direction='right'
			
	ImageButton:
		source:'student.png'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.05,'y':.67}
		back_color:(0,0,0,.2)
		on_press:
			root.manager.current='student'
			root.manager.transition.direction='left'
		
	ImageButton:
		source:'search(1).png'
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.6,'y':.67}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'bus-driver-icon-png-2.png'
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.05,'y':.42}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'save-money-icon-png-5.png'
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.6,'y':.42}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'presentation.png'
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.05,'y':.17}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'kisspng-computer-icons-sport-physical-exercise-physical-fi-sports-activitie.png'
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.6,'y':.17}
		back_color:(0,0,0,.2)			
			
<student>:
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'crm.jpg'
		FloatLayout:
            pos_hint:{'x':0.050,'y':.010}
            size_hint:.900,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
                    
		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
             
				
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'delete-icon-ios-19.jpg'
		pos_hint:{'x':.04,'y':.03}
		background_color:0,1,0,.4
		on_release:app.stop()
		
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'PinClipart.com_clipartradio-gr_1316563.png'
		pos_hint:{'x':.4,'y':.03}
		background_color:0,1,0,.4
		on_release:
			root.manager.current='screen'
			root.manager.transition.direction='up'
	
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'free-black-left-arrow-icon-png-vector-241709.png'
		pos_hint:{'x':.75,'y':.03}
		background_color:0,1,0,.4
		on_release:
			root.manager.current='screen'
			root.manager.transition.direction='right'					

	ImageButton:
		source:'it-icon-png-7.jpg'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.2
		pos_hint:{'x':.05,'y':.72}
		back_color:(0,0,0,.2)
		on_press:
			root.manager.current='it'
			root.manager.transition.direction='left'
		
	ImageButton:
		source:'programming.png'
		size_hint_y:.2
		size_hint_x:.2
		pos_hint:{'x':.05,'y':.57}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'science_research_equipment-07-512.png'
		size_hint_y:.2
		size_hint_x:.2
		pos_hint:{'x':.05,'y':.42}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'06a804a3569e45e5d1e1bbf78158bd8c.png'
		size_hint_y:.2
		size_hint_x:.2
		pos_hint:{'x':.05,'y':.27}
		back_color:(0,0,0,.2)
		
	ImageButton:
		source:'car.png'
		size_hint_y:.2
		size_hint_x:.2
		pos_hint:{'x':.05,'y':.12}
		back_color:(0,0,0,.2)
	Label:
		text:'B.Tech'
		font_size:65
		pos_hint:{'x':.0,'y':.445}
		bold:True
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True
		
	Label:
		text:'Information Technology'
		font_size:45
		pos_hint:{'x':.16,'y':.325}
		color:0,0,0,1
		bold:True
	Label:
		text:'Computer Science'
		font_size:45
		pos_hint:{'x':.08,'y':.175}
		color:0,0,0,1
		bold:True
	Label:
		text:'Robotics'
		font_size:45
		pos_hint:{'x':-.04,'y':.025}
		color:0,0,0,1
		bold:True
	Label:
		text:'Mechanics'
		font_size:45
		pos_hint:{'x':-.02,'y':-.125}
		color:0,0,0,1
		bold:True
	Label:
		text:'Automobile'
		font_size:45
		pos_hint:{'x':.0,'y':-.275}
		color:0,0,0,1
		bold:True
		
	
<it>:
	container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'crm.jpg'

		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		FloatLayout:
            pos_hint:{'x':0.050,'y':.010}
            size_hint:.900,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	Label:
		text:'Details'
		font_size:65
		pos_hint:{'x':.0,'y':.445}
		color:
		bold:True
		#italic:True
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True

	BoxLayout:
		#orientation:'horizontal'
		FloatLayout:
			size_hint:.42,.78
			pos_hint:{'x':0,'y':.12}
			canvas.before:
                Color:
                	rgba:get_color_from_hex('#ffffff')
                    #rgba:get_color_from_hex('#f98b88')
                    #rgba:get_color_from_hex('#fff5ed')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
            Label:
            	text:'Filter'
            	pos_hint:{'x':.18,'y':.85}
            	size_hint:.2,.2
            	font_size:'30sp'
            	bold:True
				color:0,0,0,1
            	markup:True
            	underline:True
            	underline:True
			CheckBox:
				pos_hint:{'x':.07,'y':.665}
				size_hint: .2,.2
				background_checkbox_down:'chk3.png'
				background_checkbox_normal:'unchk.png'
				height:'12dp'
			TextInput:
				pos_hint:{'x':.25,'y':.74}
				size_hint: .75,.05
				background_color:0,0,0,0
				multiline:False
				hint_text:'Name'
			Label:
				text:'________________________________'
				pos_hint:{'x':.28,'y':.74}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:17
			CheckBox:
				pos_hint:{'x':.07,'y':.54}
				size_hint: .2,.2
				background_checkbox_down:'chk3.png'
				background_checkbox_normal:'unchk.png'
			TextInput:
				pos_hint:{'x':.25,'y':.62}
				size_hint: .9,.05
				background_color:0,0,0,0
				multiline:False
				hint_text:'Age'
			Label:
				text:'________________________________'
				pos_hint:{'x':.28,'y':.62}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:17
			CheckBox:
				pos_hint:{'x':.07,'y':.42}
				size_hint: .2,.2
				background_checkbox_down:'chk3.png'
				background_checkbox_normal:'unchk.png'
	
			TextInput:
				pos_hint:{'x':.25,'y':.50}
				size_hint: .9,.05
				background_color:0,0,0,0
				multiline:False
				hint_text:'Mobile.No'
			Label:
				text:'________________________________'
				pos_hint:{'x':.28,'y':.50}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:17
			
		BoxLayout:
			size_hint:.012,.9
			pos_hint:{'x':.4}
			pos_hint:{'y':.12}

		ScrollView:
            size_hint: (.4, .78)
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:10
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:280
				size_hint_y:None

				
			
				
	ImageButton:
		size_hint:.15,.15
		pos_hint:{'x':.07,'y':.12}
		source:'add.png'
		on_release:
			Factory.custompopup().open()
	ImageButton:
		size_hint:.15,.15
		pos_hint:{'x':.27,'y':.12}
		source:'refresh.png'
		on_release:
			root.add_text_inputs()

	
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'delete-icon-ios-19.jpg'
		pos_hint:{'x':.04,'y':.03}
		background_color:0,1,0,.4
		on_release:app.stop()
		
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'PinClipart.com_clipartradio-gr_1316563.png'
		pos_hint:{'x':.4,'y':.03}
		background_color:0,1,0,.4
		on_release:
			root.manager.current='screen'
			root.manager.transition.direction='up'
	
	ImageButton:
		size_hint_x:.25
		size_hint_y:.05
		source:'free-black-left-arrow-icon-png-vector-241709.png'
		pos_hint:{'x':.75,'y':.03}
		background_color:0,1,0,.4
		on_release:
			root.manager.current='student'
			root.manager.transition.direction='right'	

<custompopup@Popup>:
	title:''
	fnameb:fnameb
	lnameb:lnameb
	mobileb:mobileb
	addressb:addressb
	emailb:emailb
	ageb:ageb
	dobb:dobb
	bmarkb:bmarkb
	genderb:genderb
	nationalityb:nationalityb
	categoryb:categoryb
	size_hint:.8,.8
	separator_height: 0
	background_color:0,0,0,0.4
	border: (1, 1, 1, 1)
	FloatLayout:
		canvas.before:
			Color:
				rgba:get_color_from_hex('#ffffff')
			Rectangle:
				size:self.size
				pos:self.pos
		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
                    
		ImageButton:
			source:'student2.png'
			size_hint_y:.35
			size_hint_x:.35
			pos_hint:{'x':.3,'y':.7}
			
		BoxLayout:
			pos_hint:{'x':.0,'y':.0}          
            size_hint:1,.75
			orientation:'horizontal'
			ScrollView:
				bar_width:10
				GridLayout:
					cols:1
					height:self.minimum_height
					row_default_height:60
					size_hint_y:None
					Label:
						text:'Name'
						font_size:35
						pos_hint:{'x':.5,'center_y':1.2}
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					Label:
						text:'First Name'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:fnameb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					Label:
						text:'Last Name'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:lnameb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
					Label:
						text:'Contact'
						font_size:35
						pos_hint:{'x':.5,'center_y':1.2}
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					Label:
						text:'Mobile_No'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:mobileb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'State'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:addressb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'Email'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:emailb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
					Label:
						text:'Personal'
						pos_hint:{'x':0,'center_y':1.2}
						font_size:35
						text_size:self.size
						#color:0,0,0,1
						underline:True
						color:get_color_from_hex('#21b68a')
					Label:
						text:'Age'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:ageb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'D.O.B'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:dobb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'Birth Mark'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:bmarkb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'Gender'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:genderb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'Other'
						pos_hint:{'x':0,'center_y':1.2}
						font_size:35
						text_size:self.size
						#color:0,0,0,1
						underline:True
						color:get_color_from_hex('#21b68a')
					Label:
						text:'Nationality'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:nationalityb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
						text:'Category'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:categoryb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
					Label:
					Button:
						text:'Submit'
						font_size:"25sp"
						size_hint:.7,.7
						on_press:app.add_user(fnameb.text,lnameb.text,mobileb.text,addressb.text,emailb.text,ageb.text,dobb.text,bmarkb.text,genderb.text,nationalityb.text,categoryb.text)
						background_color:get_color_from_hex('#00a572')
						on_release:
							root.dismiss()
					Label:
	
<custompopup2@Popup>:
	u1:''
	u2:''
	u3:''
	u4:''
	u5:''
	u6:''
	u7:''
	u8:''
	u9:''
	u10:''
	u11:''
	title:''
	fnameu:fnameu
	lnameu:lnameu
	mobileu:mobileu
	addressb:addressb
	emailb:emailb
	ageb:ageb
	dobb:dobb
	bmarkb:bmarkb
	genderb:genderb
	nationalityb:nationalityb
	categoryb:categoryb
	size_hint:.8,.8
	separator_height: 0
	background_color:0,0,0,0.4
	border: (1, 1, 1, 1)
	FloatLayout:
		canvas.before:
			Color:
				rgba:get_color_from_hex('#ffffff')
			Rectangle:
				size:self.size
				pos:self.pos
		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ea3c53')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
                    
		ImageButton:
			source:'student2.png'
			size_hint_y:.35
			size_hint_x:.35
			pos_hint:{'x':.3,'y':.7}
			
		BoxLayout:
			pos_hint:{'x':.0,'y':.0}          
            size_hint:1,.75
			orientation:'horizontal'
			ScrollView:
				bar_width:10
				GridLayout:
					cols:1
					height:self.minimum_height
					row_default_height:60
					size_hint_y:None
					Label:
						text:'Name'
						font_size:35
						pos_hint:{'x':.5,'center_y':1.2}
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#ea3c53')
					Label:
						text:'First Name'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:fnameu
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
						text:app.u1
					Label:
						text:'Last Name'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:lnameu
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						text:app.u2
						#background_color:0,0,0,0
					Label:
					Label:
						text:'Contact'
						font_size:35
						pos_hint:{'x':.5,'center_y':1.2}
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#ea3c53')
					Label:
						text:'Mobile_No'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:mobileu
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u3
					Label:
						text:'State'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:addressb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u4
					Label:
						text:'Email'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:emailb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u5
					Label:
					Label:
						text:'Personal'
						pos_hint:{'x':0,'center_y':1.2}
						font_size:35
						text_size:self.size
						#color:0,0,0,1
						underline:True
						color:get_color_from_hex('#ea3c53')
					Label:
						text:'Age'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:ageb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u6
					Label:
						text:'D.O.B'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:dobb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u7
					Label:
						text:'Birth Mark'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:bmarkb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u8
					Label:
						text:'Gender'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:genderb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u9
					Label:
						text:'Other'
						pos_hint:{'x':0,'center_y':1.2}
						font_size:35
						text_size:self.size
						#color:0,0,0,1
						underline:True
						color:get_color_from_hex('#ea3c53')
					Label:
						text:'Nationality'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:nationalityb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u10
					Label:
						text:'Category'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					TextInput:
						id:categoryb
						multiline:False
						color:0,0,0,1
						size_hint:1,.35
						size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						text:app.u11
					Label:
					Button:
						text:'Update'
						font_size:"25sp"
						size_hint:.7,.7
						on_press:app.update(fnameu.text,lnameu.text,mobileu.text)
						background_color:get_color_from_hex('#ea3c53')
						on_release:
							root.dismiss()
					Label:

		
<btn>:
	r1:''
	r2:''
	r3:''
	r4:''
	data:''
	data_id:''
	FloatLayout:
		
		MDCard:
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"
	        padding: "4dp"
	        size_hint: None, None
	        size: "163dp", "130dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	       

	        MDLabel:
	        	orientation:'vertical'
	            text: root.r2
	            theme_text_color: "Secondary"
	            size_hint_y: None
	            height: self.texture_size[1]
			
				
	
	        MDSeparator:
	            height: "1dp"
			MDLabel:
	            text: root.r3
	        MDLabel:
	            text: root.r4
		MDIconButton:
			icon:'account-edit'
			pos_hint:{'x':.75,'y':.7}
			on_press:
				Factory.custompopup2().open()
				#app.root.current='popup2'
		MDIconButton:
			icon:"account-remove"
			pos_hint:{'x':.75,'y':.4}
			on_release:root.delete()

<smooth@Button>:
	background_color:0,0,0,0
	back_color:(0,0,0,0)
	border_radius:[100,]
	canvas.before:
		Color:
			rgba:self.back_color
		RoundedRectangle:
			size:self.size
			pos:self.pos
			radius:[150,]			
		
''')


class buttons(Screen):
	pass
class screen2(Screen):
	pass
class student(Screen):
	pass
class btn(Screen):
	def __init__(self, **kwargs):
		super(btn, self).__init__(**kwargs)
	def delete(self):
		con=sql.connect('students_detail.db')
		cur=con.cursor()
		cur.execute('delete from studenti where ID='+self.data_id)
		con.commit()
		con.close()
		
		
class it(Screen,MDApp):
	#self.data_id=data_id
	text=StringProperty()
	container = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(it, self).__init__(**kwargs)
		Clock.schedule_once(self.setup_scrollview, 1)
	def setup_scrollview(self, dt):
		self.container.bind(minimum_height=self.container.setter('height'))
		self.add_text_inputs()
	def add_text_inputs(self):
		self.container.clear_widgets()
		con=sql.connect('students_detail.db')
		cur=con.cursor()
		cur.execute("""SELECT *FROM studenti""")
		row =cur.fetchall()
		for i in row:
			wid=btn()
			wid2=Weather()
			r1 = str(i[0])+'\n'
			r2 = i[1]+' '+i[2]+'\n'
			r3 = str(i[3])+'\n'
			r4 = str(i[4])
			
			u1=i[1]
			u2=i[2]
			u3=str(i[3])
			u4=i[4]
			u5=i[5]
			u6=str(i[6])
			u7=i[7]
			u8=i[8]
			u9=i[9]
			u10=i[10]
			u11=i[11]
			
			
			wid.data_id = str(i[0])
			wid2.data_id=str(i[0])
			wid.data = r1+r2+r3+r4
			wid2.data=r1,r2,r3,r4
			#wid2.data = r1+r2+r3+r4
			wid.r1=r1
			wid.r2=r2
			wid.r3=r3
			wid.r4=r4
			
			wid2.u1=u1
			wid2.u2=u2
			wid2.u3=u3
			wid2.u4=u4
			wid2.u5=u5
			wid2.u6=u6
			wid2.u7=u7
			wid2.u8=u8
			wid2.u9=u9
			wid2.u10=u10
			wid2.u11=u11
			self.container.add_widget(wid)
			#self.container.add_widget(wid2)
#        for x in range(30):
class ImageButton(ButtonBehavior,Image):
	pass
class popup2(Screen):
	pass

sm = ScreenManager()
sm.add_widget(buttons(name='button'))
sm.add_widget(screen2(name='screen'))
sm.add_widget(student(name='student'))
sm.add_widget(it(name='it'))
sm.add_widget(btn(name="btn"))
sm.add_widget(popup2(name='popup2'))

class Weather(MDApp,App):
	fnameu=StringProperty()
	lnameu=StringProperty()
	mobileu=StringProperty()
	def update(self,fnameu,lnameu,mobileu):
		con=sql.connect('students_detail.db')
		cur=con.cursor()
		a1=(fnameu,lnameu,mobileu)
		s1='update studenti SET'
		s2='fname="%s",lname="%s",mobile="%s" '%a1
		s3=('where ID='+self.data_id)
		cur.execute(s1+' '+s2+' '+s3)
		con.commit()
		con.close()
	
	fnameb=StringProperty()
	lnameb=StringProperty()
	mobileb=StringProperty()
	addressb=StringProperty()
	emailb=StringProperty()
	ageb=StringProperty()
	dobb=StringProperty()
	bmarkb=StringProperty()
	genderb=StringProperty()
	nationalityb=StringProperty()
	categoryb=StringProperty()
	
	
	def add_user(self,fnameb,lnameb,mobileb,addressb,emailb,ageb,dobb,bmarkb,genderb,nationalityb,categoryb):
		
		con=sql.connect('students_detail.db')
		cur=con.cursor()
		cur.execute(""" INSERT INTO studenti(fname,lname,mobile,address,email,age,dob,bmark,gender,nationality,catogery) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(fnameb,lnameb,mobileb,addressb,emailb,ageb,dobb,bmarkb,genderb,nationalityb,categoryb))
		con.commit()
		con.close()
	def build(self):
		return sm
if __name__ == '__main__':
	Weather().run()