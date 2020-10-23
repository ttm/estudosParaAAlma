USE DFLIB
CALL graphicsmode()
Call Zorax()
END
SUBROUTINE graphicsmode()
  USE DFLIB
  LOGICAL modestatus
  INTEGER(2) maxx, maxy
  TYPE (windowconfig) myscreen
  COMMON maxx, maxy
  ! Set highest resolution graphics mode.
  myscreen.numxpixels=-1
  myscreen.numypixels=-1
  myscreen.numtextcols=-1
  myscreen.numtextrows=-1
  myscreen.numcolors=-1
  myscreen.fontsize=-1
  myscreen.title = " "C ! blank
  modestatus=SETWINDOWCONFIG(myscreen)
  ! Determine the maximum dimensions.
  modestatus=GETWINDOWCONFIG(myscreen)
  maxx=myscreen.numxpixels - 1
  maxy=myscreen.numypixels - 1
  END
  Subroutine zorax()
    USE DFLIB
    dimension x1(65536),y1(65536),ix1(65536),iy1(65536)
    integer*2 dummy, xl, yl, x2, y2, i, xk, yk, ix1, iy1
    integer*4 ncolor,dummy4,rgb,ired,igreen,iblue
    RECORD /xycoord/ xy
    pii=3.14159
    ndim=8
    ang=180./float(ndim)
    ang=45.
    x1(1)=0.
    y1(1)=0.
    kd2=32
    ijust=700
    kjust=50
    ncolor=15
    i=2
    dummy=floodfill(60,5,i)
    ncolor=0.
    dummy=setcolor(ncolor)
    scale=220.
    scal1=220.
    do 20 k=1,ndim
    l=2**(k-1)
    do 20 j=1,l
    deg=float(k-1)*ang*pii/180.
    x1(l+j)=x1(j)+cos(deg)*scal1
    y1(l+j)=y1(j)+sin(deg)*scale
    xk=int(x1(l+j)+.5)+ijust
    yk=int(y1(l+j)+.5)+kjust
    xl=int(x1(l+j)+.5)+ijust-kd2
    yl=int(y1(l+j)+.5)-kd2+kjust
    x2=xl+2*kd2
    y2=yl+2*kd2
    20 continue
    do 21 k=1,2**ndim
    ix1(k)=int(x1(k)+.5000001)+ijust
    21 iy1(k)=int(y1(k)+.5000001)+kjust
    k15=1
    do 50 k14=k15,k15+2**15,2**15
    do 51 k13=k14,k14+2**14,2**14
    do 52 k12=k13,k13+2**13,2**13
    do 53 k11=k12,k12+2**12,2**12
    do 54 k10=k11,k11+2**11,2**11
    do 55 k9=k10,k10+2**10,2**10
    do 56 k8=k9,k9+2**9,2**9
    do 57 k7=k8,k8+2**8,2**8
    do 58 k6=k7,k7+2**7,2**7
    do 59 k5=k6,k6+2**6,2**6
    do 60 k4=k5,k5+2**5,2**5
    do 61 k3=k4,k4+2**4,2**4
    do 62 k2=k3,k3+2**3,2**3
    do 63 k1=k2,k2+2**2,2**2
    do 64 k=k1,k1+2,2
    call moveto(ix1(k),iy1(k),xy)
    64 dummy=lineto(ix1(k+1),iy1(k+1))
    do 70 k=k1,k1+1
    call moveto(ix1(k),iy1(k),xy)
    70 dummy=lineto(ix1(k+2),iy1(k+2))
    if(ndim.eq.2) go to 100
    63 continue
    do 71 k1=k2,k2+2**2-1
    call moveto(ix1(k1),iy1(k1),xy)
    71 dummy=lineto(ix1(k1+2**2),iy1(k1+2**2))
    if(ndim.eq.3) go to 100
    62 continue
    do 72 k2=k3,k3+2**3-1
    call moveto(ix1(k2),iy1(k2),xy)
    72 dummy=lineto(ix1(k2+2**3),iy1(k2+2**3))
    if(ndim.eq.4) go to 100
    61 continue
    do 73 k3=k4,k4+2**4-1
    call moveto(ix1(k3),iy1(k3),xy)
    73 dummy=lineto(ix1(k3+2**4),iy1(k3+2**4))
    if(ndim.eq.5) go to 100
    60 continue
    do 74 k4=k5,k5+2**5-1
    call moveto(ix1(k4),iy1(k4),xy)
    74 dummy=lineto(ix1(k4+2**5),iy1(k4+2**5))
    if(ndim.eq.6) go to 100
    59 continue
    do 75 k5=k6,k6+2**6-1
    call moveto(ix1(k5),iy1(k5),xy)
    75 dummy=lineto(ix1(k5+2**6),iy1(k5+2**6))
    if(ndim.eq.7) go to 100
    58 continue
    do 76 k6=k7,k7+2**7-1
    call moveto(ix1(k6),iy1(k6),xy)
    76 dummy=lineto(ix1(k6+2**7),iy1(k6+2**7))
    if(ndim.eq.8) go to 100
    57 continue
    do 77 k7=k8,k8+2**8-1
    call moveto(ix1(k7),iy1(k7),xy)
    77 dummy=lineto(ix1(k7+2**8),iy1(k7+2**8))
    if(ndim.eq.9) go to 100
    56 continue
    do 78 k8=k9,k9+2**9-1
    call moveto(ix1(k8),iy1(k8),xy)
    78 dummy=lineto(ix1(k8+2**9),iy1(k8+2**9))
    if(ndim.eq.10) go to 100
    55 continue
    do 79 k9=k10,k10+2**10-1
    call moveto(ix1(k9),iy1(k9),xy)
    79 dummy=lineto(ix1(k9+2**10),iy1(k9+2**10))
    if(ndim.eq.11) go to 100
    54 continue
    do 80 k10=k11,k11+2**11-1
    call moveto(ix1(k10),iy1(k10),xy)
    80 dummy=lineto(ix1(k10+2**11),iy1(k10+2**11))
    if(ndim.eq.12) go to 100
    53 continue
    do 81 k11=k12,k12+2**12-1
    call moveto(ix1(k11),iy1(k11),xy)
    81 dummy=lineto(ix1(k11+2**12),iy1(k11+2**12))
    if(ndim.eq.13) go to 100
    52 continue
    do 82 k12=k13,k13+2**13-1
    call moveto(ix1(k12),iy1(k12),xy)
    82 dummy=lineto(ix1(k12+2**13),iy1(k12+2**13))
    if(ndim.eq.14) go to 100
    51 continue
    do 83 k13=k14,k14+2**14-1
    call moveto(ix1(k13),iy1(k13),xy)
    83 dummy=lineto(ix1(k13+2**14),iy1(k13+2**14))
    if(ndim.eq.15) go to 100
    50 continue
    do 84 k14=k15,k15+2**15-1
    call moveto(ix1(k14),iy1(k14),xy)
    84 dummy=lineto(ix1(k14+2**15),iy1(k14+2**15))
    100 continue
    Read(*,*) ! Wait for enter to be pressed
    dummy=setvideomode($DEFAULTMODE)
    END
    integer*4 function rgb(r,g,b)
      integer*4 r,g,b
      rgb=ishl( ishl( b,8) .or. g,8) .or. r
      return
      end
