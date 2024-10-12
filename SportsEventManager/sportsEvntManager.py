from collections import deque


class Ticket:
    def __init__(self, eventId, customerName) -> None:
        self.eventId = eventId
        self.customerName = customerName
        self.price = 1000


allTicketsPurchased = [["EventId", "|", "customerName"]]
class Event:
    def __init__(self, Id, eventName, availableSeats) -> None:
        self.eventId = Id
        self.eventName = eventName
        self.availableSeats = availableSeats
        
allEvents = [["EventId", "|", "eventName", "|", "availableSeats"]]
class SportsEventManager:
    def __init__(self) -> None:
        self.undoTicketPurchases = []
        self.eventAttendees = deque()
        self.listOfAvailableEvents = []

    def addEvent_push(self, eventId, eventName, availableSeats):
        event = Event(eventId, eventName, availableSeats)
        eventDuplicate = [event.eventId, "|", event.eventName,"|" ,event.availableSeats]
        allEvents.append(eventDuplicate)
        self.listOfAvailableEvents.append(event)

    def view_events(self):
        if len(allEvents) > 1:
            print("{:<10}".format("All Events purchased with customers"))
            print("{:<10}".format('------------------------------------'))
            for event in allEvents:
                print("{:<10} {:<3} {:<10} {:<3} {:<10}".format(*event))
        else:
            print('no event yet')

    def purchase_ticket_push(self, eventId, customerName):
        for event in self.listOfAvailableEvents:
            if event.eventId == eventId:
                if event.availableSeats:
                    ticket = Ticket(eventId, customerName)
                    self.eventAttendees.append(ticket)
                    allTicketsPurchased.append([eventId, "|", customerName])
                    self.undoTicketPurchases.append(ticket)
                    event.availableSeats -= 1
                    print(event.availableSeats)
                    print(f"{customerName} has booked event {ticket.eventId} called {event.eventName} seats remain {event.availableSeats}")
                    break
                else:
                    print("No seats remain")
                    break
        else:
            print("no event with this id")
        for event in allEvents:
            if eventId in event and event[4]:
                event[4] -= 1
                break

    def view_allTicketsPurchased(self):

        if len(allTicketsPurchased) > 1:
            print("{:<30}".format('All ticket purchased with customers'))
            print("{:<30}".format('------------------------------------'))
            for ticket in allTicketsPurchased:
                print("{:<10} {:<3} {:<20}".format(*ticket))
        else:
            print("no ticket booked yet")

    def peek_the_last_ticket(self):

        if self.eventAttendees:
            print(f"the latest customer booking is {self.eventAttendees[-1].customerName} in the event {self.eventAttendees[0].eventId}")
        else:
            print("NO ticket booked")

    def undoTicket(self):
        if self.eventAttendees and self.undoTicketPurchases:
            cancelled_ticket = self.eventAttendees.popleft()
            eventId = cancelled_ticket.eventId
            self.undoTicketPurchases.pop()
            allTicketsPurchased.pop(1)
            for event in self.listOfAvailableEvents:
                if event.eventId == eventId:
                    event.availableSeats += 1
                    break
            for event in allEvents:
                if eventId in event:
                    event[4] += 1          
            print(f"customer{cancelled_ticket.customerName} is cancelled")
        else:
            print("No ticket booked")


sportsEventManager = SportsEventManager()
sportsEventManager.addEvent_push(1, 'event 1', 2)
sportsEventManager.addEvent_push(2, 'event 2', 3)
sportsEventManager.addEvent_push(3, 'event 3', 7)
sportsEventManager.addEvent_push(4, 'event 4', 6)
sportsEventManager.addEvent_push(5, 'event 5', 5)

sportsEventManager.view_events()
sportsEventManager.purchase_ticket_push(1, "claude")
sportsEventManager.purchase_ticket_push(1, "erisa")

sportsEventManager.view_allTicketsPurchased()

sportsEventManager.peek_the_last_ticket()
sportsEventManager.undoTicket()

sportsEventManager.view_events()
def answer():

    while True:
        print("\n1. Add event")
        print("2. view events")
        print("3. Purchase Ticket")
        print("4. view all tickets purchased")
        print("5. view latest ticket")
        print("6. cancel Your ticket")
        print("7. Exit")
        response = input(f"\nwhat is your choice: ").strip().lower()

        if response == '1':
            eventID = int(input(f" write event Id: ").strip().lower())
            EventName = input(f"write event name : ").strip().lower()
            seats = int(input(f"write event seats: ").strip().lower())
            sportsEventManager.addEvent_push(eventID, EventName, seats)

        elif response == "2":
            sportsEventManager.view_events()

        elif response == "3":
            eventID = int(input(f" write event Id: ").strip().lower())
            customer = input(f"write customer name : ").strip().lower()
            sportsEventManager.purchase_ticket_push(eventID, customer)

        elif response == "4":
            sportsEventManager.view_allTicketsPurchased()

        elif response == "5":
            sportsEventManager.peek_the_last_ticket()

        elif response == "6":
            sportsEventManager.undoTicket()

        elif response == "7":
            print("Thank you !")
            break
        else:
            print("invalid choice")


answer()
