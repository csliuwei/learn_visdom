import numpy as np
import visdom 

viz = visdom.Visdom()
Y = np.random.rand(100)

old_scatter = viz.scatter(
        X = np.random.rand(100,2),
        Y = (Y[Y>0]+1.5).astype(int),
        opts=dict(legend=['a','b'],xtickmin=-50,xtickmax=50,xtickstep=0.5, ytickmin=-50, ytickmax=50, ytickstep=0.5, markersymbol='cross-thin-open'),)

import time
time.sleep(5)

viz.update_window_opts(
    win=old_scatter,
    opts=dict(
        legend=['Apples', 'Pears'],
        xtickmin=0,
        xtickmax=1,
        xtickstep=0.5,
        ytickmin=0,
        ytickmax=1,
        ytickstep=0.5,
        markersymbol='cross-thin-open',
    ),
)

