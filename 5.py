import numpy as np
def get_percentile(a, b):
    c = b * [0]
    for i in range(b):
        p = i / b * 100
        if p == 0:
            c[i] = 0.0
        else:
            c[i] = np.percentile(a, p)
def v_equalization(v, p):