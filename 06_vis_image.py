import visdom 

viz = visdom.Visdom()

import numpy as np
viz.image(
        np.random.rand(3, 512,256),
        opts=dict(title='Random images', caption='How random'),
        )
viz.images(
        np.random.randn(20, 3, 64,64),
        opts=dict(titel='several images', caption='iamges'),
        )

