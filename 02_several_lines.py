from visdom import Visdom
import numpy as np

viz = Visdom(env='my_plot_2')
tr_loss = list(range(100))
ts_loss = list(range(10, 110))

viz.line(Y=np.column_stack((np.array(tr_loss), np.array(ts_loss))), opts=dict(showlegend=True))
