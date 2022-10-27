class Processor:
  def __init__(self) -> None:
    pass

  def process(self, data):
    return [item for item in data if item['is_active'] == 1]
