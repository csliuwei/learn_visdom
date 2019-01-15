from visdom import Visdom
import numpy as np

viz = Visdom(env='My_plot')
tr_loss = list(range(100))
viz.line(Y=np.array(tr_loss), opts=dict(showlegent=True))
