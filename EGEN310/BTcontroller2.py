'''
    Bluetooth controller for Farmer3000
    EGEN 310 Group C.1
    Gage Hilyard
'''

# Includes:
import cb
import ui
import time
import photos
from PIL import Image

# Heavily borrowed code from 'Maker Hacks' for bluetooth functionality
# Delegate handles all BLE events
class MyCentralManagerDelegate(object):
	def __init__(self):
		self.peripheral = None
		self.characteristic = None
		self.button = None
		self.fbutton = None
		self.rbutton = None
		self.bbutton = None
		self.lbutton = None
		self.message = None

		# UI view
		self.view = ui.View()
		self.view.name = 'Farmer 3000'
		self.view.background_color = '#292a29'
		print(self)
		print(self.view)

		# Farm Button
		self.button = ui.Button()
		self.button.image = ui.Image.named('farmer.jpeg').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.button.name = "button"
		self.button.border_width = 0
		self.button.height = 200
		self.button.width = 200

		self.button.corner_radius = self.button.width/2
		self.button.background_color = '#ffffff'
		self.button.enabled = False

		# Forward Button
		self.fbutton = ui.Button(title='fbutton')
		self.fbutton.image = ui.Image.named('iow:arrow_up_a_256').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.fbutton.border_width = 0
		self.fbutton.height = 100
		self.fbutton.width = 100
		self.fbutton.enabled = True

		# Right Button
		self.rbutton = ui.Button(title='rbutton')
		self.rbutton.image = ui.Image.named('iow:arrow_right_a_256').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.rbutton.border_width = 0
		self.rbutton.height = 100
		self.rbutton.width = 100
		self.rbutton.enabled = True

		# Back Button
		self.bbutton = ui.Button(title='bbutton')
		self.bbutton.image = ui.Image.named('iow:arrow_down_a_256').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.bbutton.border_width = 0
		self.bbutton.height = 100
		self.bbutton.width = 100
		self.bbutton.enabled = True

		# Left Button
		self.lbutton = ui.Button(title='lbutton')
		self.lbutton.image = ui.Image.named('iow:arrow_left_a_256').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		self.lbutton.border_width = 0
		self.lbutton.height = 100
		self.lbutton.width = 100
		self.lbutton.enabled = True

		# Position the farm button
		self.button.center = (self.view.width - 90, self.view.height * 0.5)

		# Position the directional buttons
		self.fbutton.center = (self.view.width*2, self.view.height*1.1)
		self.bbutton.center = (self.view.width*2, self.view.height*2.9)
		self.rbutton.center = (self.view.width*2.9, self.view.height*2)
		self.lbutton.center = (self.view.width*1.1, self.view.height*2)

		# Flexible left, right, top and bottom margins are flexible
		self.button.flex = 'LRTB'

		# On button click call this function
		self.button.action = self.farm_button_click
		self.fbutton.action = self.forward_button_click
		self.bbutton.action = self.back_button_click
		self.rbutton.action = self.right_button_click
		self.lbutton.action = self.left_button_click


		# Add the buttons to the view
		self.view.add_subview(self.button)
		self.view.add_subview(self.fbutton)
		self.view.add_subview(self.bbutton)
		self.view.add_subview(self.rbutton)
		self.view.add_subview(self.lbutton)

		self.button = self.view['button']
		self.fbutton = self.view['fbutton']
		self.bbutton = self.view['bbutton']
		self.rbutton = self.view['rbutton']
		self.lbutton = self.view['lbutton']

		# Shows the view
		self.view.present(style='sheet', orientations='landscape-left')

	# If the farm button is pressed
	def farm_button_click(self, sender):
		if self.message != '*':
			self.send_string("*")
			self.message = '*'
			time.sleep(0.10)
			self.button.image = ui.Image.named('tractor.jpeg').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)
		else:
			self.send_string("0")
			self.message = '0'
			time.sleep(0.10)
			self.button.image = ui.Image.named('farmer.jpeg').with_rendering_mode(ui.RENDERING_MODE_ORIGINAL)

	# If the forward button is pressed
	def forward_button_click(self, sender):
		if self.message != 'f':
			self.send_string('f')
			self.message = 'f'
			time.sleep(0.1)
		else:
			self.send_string('0')
			self.message = '0'
			time.sleep(0.1)

	# If the right button is pressed
	def right_button_click(self, sender):
		if self.message != 'r':
			self.send_string('r')
			self.message = 'r'
			time.sleep(0.1)
		else:
			self.send_string('0')
			self.message = '0'
			time.sleep(0.1)

	# If the left button is pressed
	def left_button_click(self, sender):
		if self.message != 'l':
			self.send_string('l')
			self.message = 'l'
			time.sleep(0.1)
		else:
			self.send_string('0')
			self.message = '0'
			time.sleep(0.1)

	# If the back button is pressed
	def back_button_click(self, sender):
		if self.message != 'b':
			self.send_string('b')
			self.message = 'b'
			time.sleep(0.1)
		else:
			self.send_string('0')
			self.message = '0'
			time.sleep(0.1)

	# Maker Hacks' BT code
	# Device discovered
	def did_discover_peripheral(self, p):
		if p.name == 'SH-HC-08' and not self.peripheral:
			print('Discovered ' + p.name)
			self.peripheral = p
			cb.connect_peripheral(self.peripheral)

	# Connected
	def did_connect_peripheral(self, p):
		print('Connected Peripheral ' + p.name)
		print('Looking for Service FFE0')
		p.discover_services()

	# Services discovered
	def did_discover_services(self, p, error):
		for s in p.services:
			if s.uuid == 'FFE0':
				print('Found Service ' + s.uuid)
				print('Looking for Characteristic FFE1')
				p.discover_characteristics(s)

	# Characteristics discovered
	def did_discover_characteristics(self, s, error):
		for c in s.characteristics:
			if c.uuid == 'FFE1':
				print('Found Characteristic ' + c.uuid)
				self.characteristic = c
				print(self.button)
				self.button.enabled = True

	# Send strings
	def send_string(self, string_to_send):
		self.peripheral.write_characteristic_value(self.characteristic, string_to_send, False)


# Initialize
cb.set_central_delegate(MyCentralManagerDelegate())
cb.scan_for_peripherals()
