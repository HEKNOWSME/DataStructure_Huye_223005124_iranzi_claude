from collections import deque


class Ticket:
    def __init__(self, eventId, customerName) -> None:
        self.eventId = eventId
        self.customerName = customerName
        self.price = 1000


allTicketsPurchased = [["EventId", "|", "name", "|",
                        "customer", "|", "price", "|", "date", "|"]]


class Event:
    def __init__(self, Id, eventName, date, availableSeats, location) -> None:
        self.eventId = Id
        self.eventName = eventName
        self.date = date
        self.availableSeats = availableSeats
        self.location = location


allEvents = [["EventId", "|", "eventName", "|", "Date",
              "|", "SeatsNow", "|", "location", "|"]]


class SportsEventManager:
    def __init__(self) -> None:
        self.undoTicketPurchases = []
        self.eventAttendees = deque()
        self.listOfAvailableEvents = []

    def addEvent_push(self, eventId, eventDate, eventName, availableSeats, location):
        for event in self.listOfAvailableEvents:
            if event.eventId == eventId:
                print(f"\nthis event Id is taken please view the events to set the suitable Id for this { eventName} event")
                break
        else:
            event = Event(eventId, eventName, eventDate,
                          availableSeats, location)
            eventDuplicate = [event.eventId, "|",
                              event.eventName, "|", event.date, "|", event.availableSeats, "|", event.location, "|"
                              ]
            allEvents.append(eventDuplicate)
            self.listOfAvailableEvents.append(event)
            print(f"\nYou have added event with ID: {event.eventId} with name {event.eventName} and available seats are: {event.availableSeats} will take place at {event.location} on {event.date}")

    def view_events(self):
        if len(allEvents) > 1:
            print("\nAll Events Added By Admin")
            print('-------------------------------------------------------------------')
            for event in allEvents:
                print(
                    "{:<7} {:<3} {:<10} {:<3} {:<10} {:<3} {:<8} {:<3} {:<10} {:<3}".format(*event))
            print('-------------------------------------------------------------------')
        else:
            print('\nno event yet')

    def purchase_ticket_push(self, eventId, customerName):
        for event in self.listOfAvailableEvents:
            if event.eventId == eventId:
                if event.availableSeats:
                    ticket = Ticket(eventId, customerName)
                    self.eventAttendees.append(ticket)
                    allTicketsPurchased.append(
                        [eventId, "|", event.eventName, "|", customerName, "|", 1000, "|", event.date, "|"])
                    self.undoTicketPurchases.append(ticket)
                    event.availableSeats -= 1
                    print(f"\n{customerName} you booked event {ticket.eventId} called {event.eventName} will take place at {event.location} on {event.date}")
                    break
                else:
                    print("\nNo seats remain")
                    break
        else:
            print("\nno event with this id")
        for event in allEvents:
            if eventId in event and event[4]:
                event[6] -= 1
                break

    def view_allTicketsPurchased(self):

        if len(allTicketsPurchased) > 1:
            print('\nAll ticket purchased with customers')
            print('--------------------------------------------------------------------')
            for ticket in allTicketsPurchased:
                print(
                    "{:<10} {:<3} {:<10} {:<3} {:<10} {:<3} {:5} {:3} {:11} {:3}".format(*ticket))
            print('--------------------------------------------------------------------')
        else:
            print("\nno ticket booked yet")

    def peek_the_last_ticket(self):

        if self.eventAttendees:
            print(f"\nthe latest customer booking is {self.eventAttendees[-1].customerName} in the event {self.eventAttendees[0].eventId}")
        else:
            print("\nNO ticket booked")

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
                    event[6] += 1
            print(f"\ncustomer{cancelled_ticket.customerName} is cancelled")
        else:
            print("\nNo ticket booked")


sportsEventManager = SportsEventManager()
sportsEventManager.addEvent_push(1, "12/05/2025", 'event 1', 2, "kigali")
sportsEventManager.addEvent_push(2, "13/06/2025", 'event 2', 3, "huye")
sportsEventManager.addEvent_push(3, "14/07/2025", 'event 3', 7, "kayonza")
sportsEventManager.addEvent_push(4, "15/08/2025", 'event 4', 6, "rwamagana")
sportsEventManager.addEvent_push(5, "16/09/2025", 'event 5', 5, "nyanza")

sportsEventManager.view_events()
sportsEventManager.purchase_ticket_push(1, "claude")
sportsEventManager.purchase_ticket_push(1, "erisa")

sportsEventManager.view_allTicketsPurchased()

sportsEventManager.peek_the_last_ticket()
sportsEventManager.undoTicket()

sportsEventManager.view_events()


def yesOrNo(question):
    while True:
        response = input(f"{question} yes/y or no/n: ").strip().lower()
        if response in ["yes", "y", "n", "no"]:
            return response
        else:
            print("answer yes or no")


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
            eventID = int(input(f"\nwrite event Id: ").strip().lower())
            EventName = input(f"\nwrite event name : ").strip().lower()
            location = input(f"\nwrite event location : ").strip().lower()
            date = input(f"\nwrite event date : ").strip().lower()
            seats = int(input(f"\nwrite event seats: ").strip().lower())
            sportsEventManager.addEvent_push(
                eventID, date, EventName, seats, location)

        elif response == "2":
            sportsEventManager.view_events()

        elif response == "3":
            response = yesOrNo(
                "the Ticket is 1000 $fr, do you want to continue?")
            if response in ['yes', 'y']:
               eventID = int(input(f"\nwrite event Id: ").strip().lower())
               customer = input(f"\nwrite customer name : ").strip().lower()
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
