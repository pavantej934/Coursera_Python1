# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:15:05 2016

@author: pavantej
"""
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
counter = 0
A = 0
B = 0
C = 0
D = 0

X = 0
Y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A,B,C,D,E
    if t < 10:
        D = t
        C = 0
        B = 0
        A = 0
    elif 10 <= t < 100 :
        D = t % 10
        C = t // 10
        B = 0
        A = 0
    elif 100 < t < 600 :
        D = t % 10
        C = (t // 10) % 10
        B = (t // 10) // 10
        A = 0
    elif 600 <= t :
        D = t % 10
        C = ((t // 10) % 60 ) % 10
        B = ((t // 10) % 60 ) // 10
        A = ((t // 10) // 60)
        
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global X,Y,timer
    if timer.is_running():
        timer.stop()
        Y += 1
    if D == 0 :
        X += 1
    
def reset():
    global counter, X , Y
    counter = 0
    X = 0
    Y = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    #print counter


# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter),[70,100],30,'white')
    canvas.draw_text(str(X) + ' / ' + str(Y),[140,30],30,'gray')

    
# create frame
timer = simplegui.create_timer(100,tick)
frame = simplegui.create_frame("Stop Watch",200,200)
frame.set_canvas_background('black')
frame.set_draw_handler(draw)


# register event handlers
frame.add_button('Start',start,100)
frame.add_button('Stop',stop,100)
frame.add_button('Reset',reset,100)


# start frame
#timer.start()
frame.start()
