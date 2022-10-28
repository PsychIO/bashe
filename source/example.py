import database.client as Client

class Source:
  db: None

  def __init__(self) -> None:
    self.db = Client.DB()
    pass

  def query(self):
    result = self.db.query("""
      SELECT id, phone, status, is_active FROM leapq_samples
    """)
    return result
