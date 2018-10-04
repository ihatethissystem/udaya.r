import random
dic={1:'r',2:'p',3:'s'}	
a=0
b=0
while a<3 and b<3:
	p=input("press r for rock, p for paper ,s for scissor")
	c=dic[random.randint(1,3)]
	print('you choose',p,'comp choose:',c)
	if p==c:
		print("tie")
	elif p=='r':
		if c=='p':
			print("computer wins")
			b=b+1
		else:
			print("Player wins")
			a=a+1	
	elif p=='p':
		if c=='s':
			print("computer wins")
			b=b+1
		else:
			print("player wins")
			a=a+1	
	elif p=='s':
		if c=='r':
			print("computer wins")
			b=b+1
	else:
	 	print("you win")
	if(a==3):
		print("u win the game")
	elif b==3:
		print("computer win the game")		