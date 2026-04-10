from gpiozero import LED,Button
from time import sleep
from random import uniform

left_score=0
right_score=0

led=LED(4)
right_button=Button(15)
left_button=Button(14)

left_name=input('left player name is ')
right_name=input('right player name is ')
game_over = False
def pressed(button):
	global game_over,left_score,right_score
	if game_over:
		return
	if button.pin.number==14:
		left_score+=1
		print(left_name+' won the game')
		print(f"{left_name}:{right_name}={left_score}:{right_score}")
	else:
		right_score+=1
		print(right_name+' won the game')
		print(f"{left_name}:{right_name}={left_score}={left_score}:{right_score}")
	game_over = True

right_button.when_pressed=pressed
left_button.when_pressed=pressed


while True:
	game_over = False
	led.on()
	sleep(uniform(5,10))
	led.off()

	while not game_over:
		sleep(0.01)

	sleep(2)
