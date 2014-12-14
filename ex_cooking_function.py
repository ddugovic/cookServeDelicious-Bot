import time

timer = []
def steak():
    timer.append(5)
    print "cooking steak...will be ready in approx %d" % timer[0]
    cook()
    print "Done!"
    del timer[:]
    

def cook():
    start = time.time()
    while time.time() < start + timer[0]:
        print "Doing stuff..."
        
        

