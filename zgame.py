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

print "Go Down"
while(1):
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "       				      |v"
		if count==finish:
			count=0
			break

print "Take a Right   		             ",
while(1):
	key=msvcrt.getch()
	if key=='a':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break

time_elapsed=time.time()-s_time;

print "Congrats! you have taken %d seconds out of the standard %d seconds"%(time_elapsed,std)
