import database.client as Client

class Source:
  def __init__(self) -> None:
    pass

  def query(self):
    db = Client.DB()
    result = db.query("""
      SELECT id, phone, status, is_active FROM leapq_samples
    """)
    return result
