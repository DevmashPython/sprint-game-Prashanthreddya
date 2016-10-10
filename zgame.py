import msvcrt
import time


finish=10
count=0
std=15

print "Press enter key to get started"
raw_input()

s_time=time.time()

print "Try drawing a Z! 'a' for right and 's' for 'bottom'"


print "\nTake a Right\n"
while(1):
	key=msvcrt.getch()
	if key=='a':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break
	else:
		print "You have locked the game with a wrong move !"
		exit()

		

print "Go Down"
while(1):
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "       				      |v"
		if count==finish:
			count=0
			break
	else:
		print "You have locked the game with a wrong move !"
		exit()

print "Take a Right   		             ",
while(1):
	key=msvcrt.getch()
	if key=='a':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break
	else:
		print "You have locked the game with a wrong move !"
		exit()

time_elapsed=time.time()-s_time;

<<<<<<< HEAD
print "\nCongrats! you have taken %d seconds out of the standard %d seconds"%(time_elapsed,std)
=======
print "Congrats! you have taken %d seconds out of the standard %d seconds"%(time_elapsed,std)

'''
1. The game should be lost if i press a wrong key.

'''
>>>>>>> a74477e660a1cd230bd6fc33833c814b3dd590b1
