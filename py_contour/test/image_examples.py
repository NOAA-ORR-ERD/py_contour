#!/usr/bin/env python

# simple test code for contour

import numpy as np
import py_contour
import py_gd # so we can see the results visually

M, N = 1000, 800 #(image size)
# create an array:

x = np.linspace(0, 3*np.pi, 40)
y = np.linspace(0, 3*np.pi, 32) * 0.8
# reshape x:
x.shape = (-1, 1)
z = np.cos(x) + np.sin(y)


levels = np.linspace(z.min(),z.max(), 12)
levels = levels[1:-1]
print levels
segs = py_contour.contour( z,
                        x,
                        y,
                        levels,
                       )

scale_factor = np.array((M / (x.max() - x.min()), N / (y.max() - y.min()) ))
shift = np.array ( (x.min(), y.min()) )

def scale( points ):
    return np.asarray(points)*scale_factor + shift

# scale the values:
for level in segs:
    segs[level] = scale(segs[level])


im = py_gd.Image(M,N)
#im.clear(color='silver')
im.add_color('light_grey', (225,225,225))
im.add_color('med_grey', (175,175,175))
im.clear(color='light_grey')

# draw the grid:
xx = scale(np.c_[x,x])
yy = scale(np.c_[y,y])
for i,_ in xx:
    im.draw_line((i,0),(i,N), color='med_grey', line_width=1)
for j,_ in yy:
    im.draw_line((0,j),(M,j), color='med_grey', line_width=1)


for level, segments in segs.items():
    print "level:", level
    for seg in segments:
        im.draw_line(*seg, color='white', line_width=2)
im.save("example_segments.png")

# sort the segments ....
polygons = {}
for level, segments in segs.items():
    print "level", level
    polygons[level] = py_contour.sort_segments(segments)

print polygons

# draw as polygons
im = py_gd.Image(M,N)
#im.clear(color='silver')
im.add_color('light_grey', (225,225,225))
im.add_color('med_grey', (175,175,175))
im.clear(color='light_grey')


for level, polys in polygons.items():
    print "level", level 
    for p in polys:
        im.draw_polyline(p, line_color='white', line_width=2)
im.save("example_poly.png")




