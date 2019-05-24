import simplegui,random
W=600
H=600
R=20
y1=y2=0
v1=v2=0
s1=s2=0
x=y=0
ball=[W/2,H/2]
p11=[0,H/2-50]
p12=[0,H/2+50]
p21=[W,H/2-50]
p22=[W,H/2+50]
lst=[-3,-2,2,3]
p1=''
p2=''
def draw(canvas):
    global y1,y2,s1,s2,v1,v2,x,y,ball,p1,p2
    canvas.draw_line([W/2,0],[W/2,H],10,"white")
    canvas.draw_text(p1,[100,50],26,"white")
    canvas.draw_text("score:"+str(s1),[100,80],26,"red")
    canvas.draw_text(p2,[400,50],26,"white")
    canvas.draw_text("score:"+str(s2),[400,80],26,"blue")
    
    canvas.draw_line([15,0],[15,H],1,"white")
    canvas.draw_line([W-15,0],[W-15,H],1,"white")
    
    canvas.draw_line(p11,p12,30,"red")
    canvas.draw_line(p21,p22,30,"blue")

    p11[1]+=v1
    p12[1]+=v1
    p21[1]+=v2
    p22[1]+=v2
    
    if p11[1]==0 or p12[1]==H:
        v1=0
    if p21[1]==0 or p22[1]==H:
        v2=0

    canvas.draw_circle(ball,R,2,"black","yellow")
    ball[0]+=x
    ball[1]+=y

    if ball[0]==36: 
        if ball[1]<=p12[1] and ball[1]>=p11[1]:
            s1+=1
        if ball[1]>=p12[1] or ball[1]<=p11[1]:
            s2+=1
            ball=[W/2,H/2]
            x=random.choice(lst)
            y=random.choice(lst)     
          
    if ball[0]==W-36:
        if ball[1]<=p22[1] and ball[1]>=p21[1]:
            s2+=1
        if ball[1]>=p22[1] or ball[1]<=p21[1]:
            s1+=1
            ball=[W/2,H/2]
            x=random.choice(lst)
            y=random.choice(lst)

    if ball[0]<=35 or ball[0]>=W-35:
        x=-x
    if ball[1]<=20 or ball[1]>=H-20:
        y=-y
        
    if s1>=20 and s2<20:
        x=y=0
        s1=20
        canvas.draw_text("Winner is..."+p1+"!",[90,200],40,"white")
    if s2>=20 and s1<20:
        x=y=0
        s2=20
        canvas.draw_text("Winner is..."+p2+"!",[90,200],40,"white")
    if s1==s2 and s2>=20:
        x=y=0
        s2=20
        s1=20
        canvas.draw_text("MATCH IS TIE!!!!",[90,200],40,"white")
        
    
def kd(k):
    global v1,v2
    if k==simplegui.KEY_MAP['q']:
        v1=-5
    if k==simplegui.KEY_MAP['a']:
        v1=5
    if k==simplegui.KEY_MAP['up']:
        v2=-5
    if k==simplegui.KEY_MAP['down']:
        v2=5
        
def ku(k):
    global v1,v2
    if k==simplegui.KEY_MAP['q']:
        v1=0
    if k==simplegui.KEY_MAP['a']:
        v1=0
    if k==simplegui.KEY_MAP['up']:
        v2=0
    if k==simplegui.KEY_MAP['down']:
        v2=0
def start():
    global x,y
    x=random.choice(lst)
    y=random.choice(lst)
def pl1(p):
    global p1
    p1=p
def pl2(p):
    global p2
    p2=p

frame=simplegui.create_frame("pong",W,H)
frame.set_canvas_background("green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
frame.set_keyup_handler(ku)
frame.add_button("start",start,50)
frame.add_input('player-1:',pl1,100)
frame.add_input('player-2:',pl2,100)
frame.start()