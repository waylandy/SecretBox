def draw_ss(ss, x, ypos=20, height=2):
    for s, p in zip(ss, x):
        if s=='S': # blue:  sheet
            pat=patches.Rectangle(width=1,height=height,fc='#0000ff',lw=0,xy=(p-0.5, ypos))
        if s=='H': # red:   helix
            pat=patches.Rectangle(width=1,height=height,fc='#ff0000',lw=0,xy=(p-0.5, ypos))
        if s=='L': # black: loop
            pat=patches.Rectangle(width=1,height=height/4,fc='#ffffff',lw=0, xy=(p-0.5,ypos+(height*(3/8))))
        plt.gca().add_patch(pat)
        del pat


def read_xvg(xvg):
    x,y=[],[]
    r = open(xvg)
    for l in r:
        if l[0] not in '#@':
            l=l.split()
            x.append(float(l[0]))
            y.append(float(l[1]))
    r.close()
    return x,y


def moving_average(x, w=3):
    s=(w*2)+1
    return [sum(x[n-w if n>w else 0:n+w+1])/s for n, xi in enumerate(x)]
