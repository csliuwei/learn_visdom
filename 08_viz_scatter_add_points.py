import numpy as np
import visdom 
import time 

viz = visdom.Visdom()

win = viz.scatter(
        X = np.random.rand(255, 2),
        opts = dict(
            markersize=10,
            markercolor=np.random.randint(0, 255, (255,3,)),
            ),
        )

assert viz.win_exists(win)

time.sleep(2)

viz.scatter(
        X=np.random.rand(255,2),
        win=win,
        opts = dict(
            markersize=10,
            markercolor=np.random.randint(0, 255, (255,3,)),
            ),

        update='append')
