from scipy.stats import norm, kurtosis

class Processor:
  def __init__(self) -> None:
    pass

  def process(self, data):
    data = norm.rvs(size=1000, random_state=3)
    kurtosis(data)
    return data
