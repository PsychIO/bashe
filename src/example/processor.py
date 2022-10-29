from scipy.stats import variation

class Processor:
  def __init__(self) -> None:
    self.kinds = ['l1s', 'l2s', 'l1l', 'l2l']
    pass

  def process(self, data):
    statsMapping = {}
    results = {}
    for kind in self.kinds:
      statsMapping[kind] = variation([item[kind] for item in data])
    
    for item in data:
      for kind in self.kinds:
        statsVal = statsMapping[kind]
        result = item[kind] - statsVal
        
        if kind in results:
          results[kind].append(result)
        else:
          results[kind] = [result]
    return results