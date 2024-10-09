from collections import deque
class Event:
   def __init__(self, eventId, eventName, Date, seat_available):
      self.Id = eventId
      self.name = eventName
      self.Date = Date
      self.seats = seat_available

class Ticket:
   def __init__(self, ticketId, eventId, bookedCustomer):
      self.Id = ticketId
      self.eventId = eventId
      self.customer = bookedCustomer
class EventTicketingSystem:
   def __init__(self):
      self.events = []
      self.booked_tickets = deque()
      self.ticket_stack = []
      