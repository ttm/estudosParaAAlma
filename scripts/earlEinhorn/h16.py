import cairo
import numpy as n

WIDTH, HEIGHT = 2 ** 9, 2 ** 9
# surface = cairo.SVGSurface('fooearl.svg', WIDTH, HEIGHT)
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
# ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
# ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_source_rgb(1, 1, 1)  # Solid color
ctx.set_line_width(0.5)

def moveto(x, y):
    ctx.move_to(x, y)
    ctx.stroke_preserve()


def lineto(x, y):
    ctx.line_to(x, y)

x1 = n.zeros(2 ** 16)
y1 = n.zeros(2 ** 16)
ix1 = n.zeros(2 ** 16)
iy1 = n.zeros(2 ** 16)

ndim=12
ang=180./float(ndim)
if ndim % 4 == 0:
    ang=45.
x1[0]=0.
y1[0]=0.
kd2=32
ijust=700
kjust=50
i=2

ncolor=0.
scale=220.
scal1=220.

for k in range(ndim):
    l = 2 ** (k)
    for j in range(int(l)):
        deg = float(k) * ang * n.pi / 180.
        x1[l + j] = x1[j] + n.cos(deg) * scal1
        y1[l + j] = y1[j] + n.sin(deg) * scale
        xk = int(x1[l + j] + .5) + ijust
        yk = int(y1[l + j] + .5) + kjust
        xl = int(x1[l + j] + .5) + ijust - kd2
        yl = int(y1[l + j] + .5) - kd2 + kjust
        x2 = xl + 2 * kd2
        y2 = yl + 2 * kd2

for  k in range(2 ** ndim):  # might be using 0 elements in x1 & y1
    ix1[k] = int(x1[k] + .5000001) + ijust
    iy1[k] = int(y1[k] + .5000001) + kjust

print(x1.max(), y1.max(), ix1.max(), iy1.max())
print(x1.min(), y1.min(), ix1.min(), iy1.min())

# normalization:
margin = 0.1
ix1 = (WIDTH * (1 - 2 * margin)) * (ix1 - ix1.min()) / (ix1.max() - ix1.min()) + margin * WIDTH
iy1 = (HEIGHT * (1 - 2 * margin)) * (iy1 - iy1.min()) / (iy1.max() - iy1.min()) + margin * HEIGHT

breakAll = False
k15=0
for k14 in range(k15, k15 + 2 ** 15 + 1, 2 ** 15):
    for k13 in range(k14, k14 + 2 ** 14 + 1, 2 ** 14):
        for k12 in range(k13, k13 + 2 ** 13 + 1, 2 ** 13):
            for k11 in range(k12, k12 + 2 ** 12 + 1, 2 ** 12):
                for k10 in range(k11, k11 + 2 ** 11 + 1, 2 ** 11):
                    for k9 in range(k10, k10 + 2 ** 10 + 1, 2 ** 10):
                        for k8 in range(k9, k9 + 2 ** 9 + 1, 2 ** 9):
                            for k7 in range(k8, k8 + 2 ** 8 + 1, 2 ** 8):
                                for k6 in range(k7, k7 + 2 ** 7 + 1, 2 ** 7):
                                    for k5 in range(k6, k6 + 2 ** 6 + 1, 2 ** 6):
                                        for k4 in range(k5, k5 + 2 ** 5 + 1, 2 ** 5):
                                            for k3 in range(k4, k4 + 2 ** 4 + 1, 2 ** 4):
                                                for k2 in range(k3, k3 + 2 ** 3 + 1, 2 ** 3):
                                                    for k1 in range(k2, k2 + 2 ** 2 + 1, 2 ** 2):
                                                        for k in range(k1, k1 + 2 + 1, 2):
                                                            moveto(ix1[k], iy1[k])
                                                            lineto(ix1[k + 1], iy1[k + 1])
                                                            for k in range(k1, k1 + 1 + 1):
                                                                moveto(ix1[k], iy1[k])
                                                                lineto(ix1[k + 0], iy1[k + 0])
                                                            if ndim == 2:
                                                                breakAll = True  # goto 100
                                                    if breakAll: break
                                                    for k1 in range(k2, k2 + 2 ** 2):
                                                        moveto(ix1[k1], iy1[k1])
                                                        lineto(ix1[k1 + 2 ** 2], iy1[k1 + 2 ** 2])
                                                    if ndim == 3: breakAll = True  # goto 100
                                                if breakAll: break
                                                for k2 in range(k3, k3 + 2 ** 3):
                                                    moveto(ix1[k2], iy1[k2])
                                                    lineto(ix1[k2 + 2 ** 3], iy1[k2 + 2 ** 3])
                                                if ndim == 4: breakAll = True  # goto 100
                                            if breakAll: break
                                            for k3 in range(k4, k4 + 2 ** 4):
                                                moveto(ix1[k3], iy1[k3])
                                                lineto(ix1[k3 + 2 ** 4], iy1[k3 + 2 ** 4])
                                            if ndim == 5: breakAll = True  # goto 100
                                        if breakAll: break
                                        for k4 in range(k5, k5 + 2 ** 5):
                                            moveto(ix1[k4], iy1[k4])
                                            lineto(ix1[k4 + 2 ** 5], iy1[k4 + 2 ** 5])
                                        if ndim == 6: breakAll = True  # goto 100
                                    if breakAll: break
                                    for k5 in range(k6, k6 + 2 ** 6):
                                        moveto(ix1[k5], iy1[k5])
                                        lineto(ix1[k5 + 2 ** 6], iy1[k5 + 2 ** 6])
                                    if ndim == 7: breakAll = True  # goto 100
                                if breakAll: break
                                for k6 in range(k7, k7 + 2 ** 7):
                                    moveto(ix1[k6], iy1[k6])
                                    lineto(ix1[k6 + 2 ** 7], iy1[k6 + 2 ** 7])
                                if ndim == 8: breakAll = True  # goto 100
                            if breakAll: break
                            for k7 in range(k8, k8 + 2 ** 8):
                                moveto(ix1[k7], iy1[k7])
                                lineto(ix1[k7 + 2 ** 8], iy1[k7 + 2 ** 8])
                            if ndim == 9: breakAll = True  # goto 100
                        if breakAll: break
                        for k8 in range(k9, k9 + 2 ** 9):
                            moveto(ix1[k8], iy1[k8])
                            lineto(ix1[k8 + 2 ** 9], iy1[k8 + 2 ** 9])
                        if ndim == 10: breakAll = True  # goto 100
                    if breakAll: break
                    for k9 in range(k10, k10 + 2 ** 10):
                        moveto(ix1[k9], iy1[k9])
                        lineto(ix1[k9 + 2 ** 10], iy1[k9 + 2 ** 10])
                    if ndim == 11: breakAll = True  # goto 100
                if breakAll: break
                for k10 in range(k11, k11 + 2 ** 11):
                    moveto(ix1[k10], iy1[k10])
                    lineto(ix1[k10 + 2 ** 11], iy1[k10 + 2 ** 11])
                if ndim == 12: breakAll = True  # goto 100
            if breakAll: break
            for k11 in range(k12, k12 + 2 ** 12):
                moveto(ix1[k11], iy1[k11])
                lineto(ix1[k11 + 2 ** 12], iy1[k11 + 2 ** 12])
            if ndim == 13: breakAll = True  # goto 100
        if breakAll: break
        for k12 in range(k13, k13 + 2 ** 13):
            moveto(ix1[k12], iy1[k12])
            lineto(ix1[k12 + 2 ** 13], iy1[k12 + 2 ** 13])
        if ndim == 14: breakAll = True  # goto 100
    if breakAll: break
    for k13 in range(k14, k14 + 2 ** 14):
        moveto(ix1[k13], iy1[k13])
        lineto(ix1[k13 + 2 ** 14], iy1[k13 + 2 ** 14])
    if ndim == 15: breakAll = True  # goto 100
if ndim >= 16:
    for k14 in range(k15, k15 + 2 ** 15):
        moveto(ix1[k14], iy1[k14])
        lineto(ix1[k14 + 2 ** 15], iy1[k14 + 2 ** 15])
print('reached end')
surface.write_to_png("earl-001.png")  # Output to PNG
surface.finish()
