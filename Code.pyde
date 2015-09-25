#size of the background
size (420, 594)
#Farbe des Hintergrundes 
background (242, 210, 173)

number_of_lines = 35
max_stroke_of_lines = 5
# not finished
# number_of_polygons = 1

# draw lines by random value
for i in range (0, number_of_lines):
    x1 = random(-100, width +100)
    y1 = 0
    x2 = random (-100, width +100)
    y2 = 297
    strokeWeight (random(0,max_stroke_of_lines))
    line(x1,y1,x2,y2)

# draw red lines by random value
for k in range (0, number_of_lines):
    x1 = random (-100, width +100)
    y1 = 297
    x2 = random (-100, width +100)
    y2 = random (297, height +100)
    x3 = random (-100, width +100)
    y3 = random (297, height +100)
    x4 = random (-100, width +100)
    y4 = 594
    noFill()
    stroke (185, 26, 26) 
    strokeWeight (random(0,max_stroke_of_lines))
    bezier (x1,y1,x2,y2,x3,y3,x4,y4)

# take a pictur and save it
# save("10.png")

# not finisehd polygons
'''
for h in range (0, number_of_polygons):
    #x1 = random (0, width)
    #y1 = random (0, 297)
    #x2 = random (0, width)
    #y2 = random (0, 297)
    x1 = random (100, 200)
    y1 = 200
    x2 = random (100, 200)
    y2 = 297
    fill(0)
    noStroke()
    rect(x1, y1, x2, y2)
'''
