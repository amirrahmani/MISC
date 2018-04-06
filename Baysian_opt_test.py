import pickle
import time
from hyperopt import fmin, tpe, hp, STATUS_OK

# def objective(x,y,z,penalty):
#     if penalty == 
#     return {'loss': x ** 2+y**2+z**2}

def objective(args):  
    print(args)
    x,y,c = args
    case = c[0]
    z = c[1]
    t = c[2]
    if case == 'l1':
        return {'loss':x ** 2+y**2+z**2+t,'status': STATUS_OK}
    if case == 'l2':
        return {'loss':x ** 2+y**2+z**2+t,'status': STATUS_OK}

#def objective2(args):
#    return objective(*args)


space=[hp.uniformint('x',-10,10),
       hp.uniformint('y',-10,10),
       hp.choice('a',
                   [
                       ('l1',
                        hp.randint('z',1),
                       hp.uniformint('t',4,10)),
                       ('l2',
                        hp.uniformint('z1',-10,10),
                       hp.uniformint('t1',0,4))
                   ]
                )
      ]

best = fmin(objective,
    space = space,
    algo=tpe.suggest,
    max_evals=100)

print(best)
