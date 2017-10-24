from joblib import Parallel, delayed
from math import sqrt
Parallel(n_jobs=20, backend="threading")(delayed(sqrt)(i ** 2) for i in range(1000))
