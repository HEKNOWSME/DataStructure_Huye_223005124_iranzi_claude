from collections import deque
class Ticket:
   def __init__(self, eventId, customerName) -> None:
      self.eventId =eventId
      self.customerName =customerName
class Event:
   def __init__(self, Id, eventName, availableSeats) -> None:
      self.event_id = Id
      self.event_name = eventName
      self.available_seats = availableSeats
class SportsEventManager:
   def __init__(self) -> None:
      self.undo_ticket_purchase_stack = []
      self.event_attendees = deque()
      self.list_of_available_events = []
   def addEvent(self, eventId, eventName, availableSeats):
      event = Event(eventId, eventName, availableSeats)
      self.list_of_available_events.append(event)
      print(f'This event {event.event_name} is added with the seats {event.available_seats}')
   def view_events(self):
      for event in self.list_of_available_events:
         print(f"{event.event_id} {event.event_name} {event.available_seats}")
   def purchase_ticket(self, eventId, customerName):
      for event in self.list_of_available_events:   
         if event.event_id == eventId:
            if event.available_seats > 0:
               event.available_seats -=1
               ticket = Ticket(eventId , customerName)
               self.undo_ticket_purchase_stack.append(ticket)
               self.event_attendees.append(customerName) 
               print(self.event_attendees)
               print(f"available seats{event.available_seats} {event.event_name}")
               return
            else:
               print('no seats remain')
               return
         else:
            print('no event with give ID')
            return
   def view_all_tickets_purchased(self):
      for ticket in self.undo_ticket_purchase_stack:
         print(f"event purchased {ticket.eventId}, customer purchased this event:  {ticket.customerName}", end="")
   def cancelling_tickets(self, ticketId):
      for ticket in self.undo_ticket_purchase_stack:
         if ticketId in ticket.ticketId:
            self.undo_ticket_purchase_stack.remove(ticket)
            self.event_attendees.popleft()      
      print('This ticket is not available')
sportsEventManager = SportsEventManager()
sportsEventManager.addEvent(123,'event 1', 1)
sportsEventManager.addEvent(456,'event 2', 34)
sportsEventManager.view_events()
sportsEventManager.purchase_ticket(123,'claude')
sportsEventManager.purchase_ticket(456,'iranzi')
sportsEventManager.view_all_tickets_purchased()
sportsEventManager.cancelling_tickets()
