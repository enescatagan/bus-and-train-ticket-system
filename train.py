class Train():
    """Train Tickets"""
    def __init__(self, id, company, departure, destination, date, time, fee) -> None:
      self.id = id
      self.company = company
      self.departure = departure
      self.destination = destination
      self.date = date
      self.time = time
      self.fee = fee