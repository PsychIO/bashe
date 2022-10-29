import database.client as Client

class Source:
  def __init__(self) -> None:
    self.db = Client.DB()
    pass

  def query(self):
    result = self.db.query("""
      SELECT 
        id, name, phone, 
        lang1_speaking_self as l1s, lang2_speaking_self as l2s,
        lang1_listening_self as l1l, lang2_listening_self as l2l
      FROM analysis_groups
    """)
    return result
