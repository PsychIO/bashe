import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

class Report:
  def __init__(self) -> None:
    pass

  def generate(self, results):
    ax = plt.subplot()
    colors = ['#03a9f4', '#ff9800', '#9c27b0', '#f44336']
    for index, key in enumerate(results):
      list = results[key]
      x = np.linspace(-5, 5, len(list))
      y = norm.pdf(list)
      ax.plot(x, y, label='{}'.format(key))
      ax.get_lines()[index].set_color(colors[index])
      ax.legend()
    plt.savefig('results/test.png')
    print('Plot is generated to results/test.png')
