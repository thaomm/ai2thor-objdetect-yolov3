import ai2thor.controller
import keyboard
import detector
import cv2

#Object detection
def detect():
	cv2.imwrite('input.jpg', event.cv2img)
	detector.detect()

if __name__ == "__main__":
	#Start up ai2thor and initialize floor
	controller = ai2thor.controller.Controller()
	controller.start(player_screen_height=666, player_screen_width=666)
	controller.reset('FloorPlan3')
	mapnum = 3 
	mapm = mapnum
	m = False
	##FloorPlan: <=30 ; 201<=<=230 ; 301<=<=330 ; 401<=<=430
	controller.step(dict(action='Initialize', gridSize=0.5))
	print('Initialized')	
	
	#Control with keyboard
	while True:
		
			if keyboard.is_pressed('a'):
				event = controller.step(dict(action = 'MoveLeft'))
				detect()
			elif keyboard.is_pressed('d'):
				event = controller.step(dict(action = 'MoveRight'))
				detect()
			elif keyboard.is_pressed('w'):
				event = controller.step(dict(action = 'MoveAhead'))
				detect()
			elif keyboard.is_pressed('s'):
				event = controller.step(dict(action = 'MoveBack'))
				detect()
			elif keyboard.is_pressed('up arrow'):
				event = controller.step(dict(action = 'LookUp'))
				detect()
			elif keyboard.is_pressed('down arrow'):
				event = controller.step(dict(action = 'LookDown'))
				detect()
			elif keyboard.is_pressed('right arrow'):
				event = controller.step(dict(action = 'RotateRight'))
				detect()
			elif keyboard.is_pressed('left arrow'):
				event = controller.step(dict(action = 'RotateLeft'))
				detect()         
			
