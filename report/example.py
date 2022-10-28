import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import kurtosis
import np

class Report:
  def __init__(self) -> None:
    pass

  def generate(self, results):
    x = np.linspace(-5, 5, 100)
    ax = plt.subplot()
    distnames = ['laplace', 'norm', 'uniform']
    for distname in distnames:
      if distname == 'uniform':
          dist = getattr(stats, distname)(loc=-2, scale=4)
      else:
          dist = getattr(stats, distname)
      data = dist.rvs(size=1000)
      kur = kurtosis(data, fisher=True)
      y = dist.pdf(x)
      ax.plot(x, y, label="{}, {}".format(distname, round(kur, 3)))
      ax.legend()
    plt.savefig('results/test.png')
    print('Plot is generated to results/test.png')
