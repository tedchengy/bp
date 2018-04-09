# -*- coding: utf-8 -*-

import numpy as np
A=np.mat([[1 ,0],[0, 2]])
b=np.mat([[0],[0]])
x0=[[2],[1]]
epsilon=1e-5

x=x0;
iter=0;
grad=2*(A*x+b);

while (np.linalg.norm(grad)>epsilon):
    iter=iter+1
    t=float(np.linalg.norm(grad)**2/(2*grad.T*A*grad))
    x=x-t*grad
    grad=2*(A*x+b)
    fun_val=x.T*A*x+2*b.T*x
    print('iter_number = ',iter ,'norm_grad = ',np.linalg.norm(grad), 'fun_val = ',fun_val);

print x