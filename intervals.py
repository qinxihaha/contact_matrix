import numpy as np
import scipy.stats

Tmax = 100
def interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return [m, m-h, m+h]

class intervals:
    def __init__(self, dat):
        self.dat = dat

    def get(self):
        means = []
        higher_cis = []
        lower_cis = []
        for t in range(0, 100):
            one_time = []
            for i in range(0, len(self.dat)):
                one_time.append(self.dat[i][t])
            mean_higher_lower = interval(data = one_time)

            means.append(mean_higher_lower[0])
            higher_cis.append(mean_higher_lower[1])
            lower_cis.append(mean_higher_lower[2])

        return(means, higher_cis, lower_cis)


