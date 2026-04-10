from gpiozero import LED,Button
from time import sleep,time
from random import uniform

left_score=0
right_score=0

led_off_time=0

led=LED(4)
right_button=Button(15)
left_button=Button(14)

left_name=input('left player name is ')
right_name=input('right player name is ')

game_over = False

def pressed(button):
	global game_over,left_score,right_score,led_off_time
	if game_over:
		return
	reaction_ms=(time() - led_off_time)*1000
	if button.pin.number==14:
		left_score+=1
		print(left_name+' won the game')
		print(f"reaction time:{reaction_ms:.1f} ms")
		print(f"{left_name}{left_score} : {right_score}{right_name}")
	else:
		right_score+=1
		print(right_name+' won the game')
		print(f"reaction time:{reaction_ms:.1f} ms")
		print(f"{left_name}{left_score} : {right_score}{right_name}")
	game_over = True

right_button.when_pressed=pressed
left_button.when_pressed=pressed


while True:
	game_over = False
	led.on()
	sleep(uniform(5,10))
	led.off()
	led_off_time=time()
	print("LED turned off!Press your button FAST!")

	sleep(uniform(5,10))
	led.off()
	while not game_over:
		sleep(0.01)

	sleep(2)
