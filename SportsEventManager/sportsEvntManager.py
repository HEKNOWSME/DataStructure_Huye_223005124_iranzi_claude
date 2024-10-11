from collections import deque
class Ticket:
   def __init__(self, eventId, customerName) -> None:
      self.eventId =eventId
      self.customerName =customerName
      self.price = 1000
class Event:
   def __init__(self, Id, eventName, availableSeats) -> None:
      self.eventId = Id
      self.eventName = eventName
      self.availableSeats = availableSeats
class SportsEventManager:
   def __init__(self) -> None:
      self.undoTicketPurchases = []
      self.eventAttendees = deque()
      self.listOfAvailableEvents = []
      self.allEvents = [["EventId","|" , "eventName", "|", "availableSeats"]]
      self.allTicketsPurchased = [["EventId","|" , "customerName"]]
   def addEvent_push(self, eventId, eventName, availableSeats):
      event = Event(eventId, eventName, availableSeats)
      self.listOfAvailableEvents.append(event)
      eventDuplicate = []
      eventDuplicate.append(event.eventId)
      eventDuplicate.append("|")
      eventDuplicate.append(event.eventName)
      eventDuplicate.append("|")
      eventDuplicate.append(event.availableSeats)
      self.allEvents.append(eventDuplicate)
   
   def view_events(self):
      print("{:<10}".format("All Events purchased with customers"))
      print("{:<10}".format('------------------------------------'))
      for event in self.allEvents:
         print("{:<10} {:<3} {:<10} {:<3} {:<10}".format(*event))
   
   def purchase_ticket_push(self, eventId, customerName):
      for event in self.listOfAvailableEvents:   
         if event.eventId == eventId:
            if event.availableSeats > 0:
               event.availableSeats -=1
               ticket = Ticket(eventId , customerName)
               self.eventAttendees.append(ticket)
               eventDuplicate = []
               eventDuplicate.append(eventId)
               eventDuplicate.append("|")
               eventDuplicate.append(customerName)
               self.allTicketsPurchased.append(eventDuplicate)
               self.listOfAvailableEvents.append(ticket)
               print(f"the customer {customerName} booked this event with id {eventId}") 
               return
            else:
               print('no seats remain')
               break
      else:
         print("no event with this id")

         
         
   def view_allTicketsPurchased(self):
      print("{:<30}".format('All ticket purchased with customers'))
      print("{:<30}".format('------------------------------------'))
      for ticket in self.allTicketsPurchased:
         print("{:<10} {:<3} {:<20}".format(*ticket))
         
   def peek_the_last_ticket(self):
      if self.eventAttendees:
         print(f"the latest customer booking is {self.eventAttendees[1].customerName} in the event {self.eventAttendees[0].eventId}")
      else:
         print("NO ticket booked")
   def cancelling_ticket_pop(self):
      if self.eventAttendees:
         cancelled_ticket = self.eventAttendees.popleft()
         self.allTicketsPurchased.pop(1)
         print(f"this ticket of the customer {cancelled_ticket.customerName} is cancelled")
         self.view_allTicketsPurchased()
         return self.undoTicketPurchases.append(cancelled_ticket)
      else:
         print("No ticket booked")
         
   def undoing_ticket_cancelled(self):
      if self.undoTicketPurchases:
         undo = self.undoTicketPurchases.pop()
         self.eventAttendees.append(undo)
         newTicket = []
         newTicket.append(undo.eventId)
         newTicket.append("|")
         newTicket.append(undo.customerName)
         self.allTicketsPurchased.append(newTicket)
         self.view_allTicketsPurchased()
      elif not len(self.allTicketsPurchased) == 1:
         pass
      else:
         current_customer = self.allTicketsPurchased[1][2]
         print(f"MR/mrs {current_customer} Your ticket is not canceled")
            
sportsEventManager = SportsEventManager()
sportsEventManager.addEvent_push(1,"event 1", 23)
sportsEventManager.addEvent_push(2,"event 2", 3)
sportsEventManager.addEvent_push(3,"event 3", 2)
sportsEventManager.addEvent_push(4,"event 4", 20)
sportsEventManager.addEvent_push(5,"event 5", 23)
sportsEventManager.addEvent_push(6,"event 6", 3)
sportsEventManager.addEvent_push(7,"event 7", 2)
sportsEventManager.addEvent_push(9,"event 9", 20)
sportsEventManager.addEvent_push(10,"event 10", 20)

sportsEventManager.purchase_ticket_push(1, "customer 1")
sportsEventManager.purchase_ticket_push(3, "customer 3")
sportsEventManager.purchase_ticket_push(3, "customer 3")
sportsEventManager.purchase_ticket_push(4, "customer 4")
sportsEventManager.purchase_ticket_push(5, "customer 5")
sportsEventManager.purchase_ticket_push(6, "customer 6")
sportsEventManager.purchase_ticket_push(7, "customer 7")
sportsEventManager.purchase_ticket_push(8, "customer 8")
sportsEventManager.purchase_ticket_push(9, "customer 9")
sportsEventManager.purchase_ticket_push(10, "customer 10")

sportsEventManager.peek_the_last_ticket()
sportsEventManager.view_events()
sportsEventManager.view_allTicketsPurchased()
sportsEventManager.cancelling_ticket_pop()
sportsEventManager.undoing_ticket_cancelled()






def answer(question):
   while True:
      response = input(f"{question} yes/no: ").strip().lower()
      if response in ['yes', 'no', 'y', 'n']:
         return response
      else:
         print('Please Answer yes/y or no/n')
def pushEvent(number):
   while number < 3:
      response = answer("do you want to add an event?")
      if(response == 'yes'):
         eventName = input("please add event eventName: ").strip().lower()
         seats = int(input("please add event seats: ").strip())
         sportsEventManager.addEvent_push(number, eventName, seats)
         number +=1
      else:
         return False
   return sportsEventManager.view_events()

def bookTicket(number):
   while number < 3:
      response = answer("do you want to book sport ticket?")
      if (response == 'yes'):
         eventId = int(input("please add event eventId: ").strip())
         surname = input("please add event surname: ").strip().lower()
         sportsEventManager.purchase_ticket_push(eventId, surname)
         number += 1
      else:
         return False
   return sportsEventManager.view_allTicketsPurchased()
def cancelTicket(number):
   while number <=1:
      response = answer("do you want to cancel your ticket?")
      if (response == 'yes'):
         sportsEventManager.cancelling_ticket_pop()
         number += 1
      else:
         print("Thank you!")
         return False
   return True
def undoTicket(number):
   while number <= 1:
      response = answer("do you want to undo your ticket?")
      if (response == 'yes'):
         sportsEventManager.undoing_ticket_cancelled()
         number += 1
      else:
         print("Thank you!")
         return False
      
def main(number):
   if not pushEvent(number):
      bookTicket(number)
   if cancelTicket(number):
      undoTicket(number)
main(1)
