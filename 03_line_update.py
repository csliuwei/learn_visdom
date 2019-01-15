from visdom import Visdom
import numpy as np

import time

viz = Visdom(env='my_plot_3')
x,y = 0,0
win = viz.line(
        X=np.array([x]),
        Y=np.array([y]),
        opts=dict(title='two lines')
        )

for i in range(10):
    x += i
    y += i*i
    viz.line(
            X = np.array([x]),
            Y = np.array([y]),
            win=win,
            update='append'
            )
    time.sleep(5)
