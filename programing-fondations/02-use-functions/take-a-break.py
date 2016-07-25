import time
import webbrowser

breaks = 3
for iter in range(breaks):
    time.sleep(10)
    print "Time to take a break it's", time.ctime()
    print "This is break number", iter + 1, "of", breaks,"\n" 
    webbrowser.open("https://youtu.be/UmO9LmvLVyM")
