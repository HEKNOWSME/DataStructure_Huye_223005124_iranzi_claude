from collections import deque

# Event class to store event details


class Event:
    def __init__(self, event_id, event_name, date, seats_available):
        self.event_id = event_id
        self.event_name = event_name
        self.date = date
        self.seats_available = seats_available
        self.bookings_queue = deque()  # Queue for bookings
        self.cancellations_stack = []  # Stack for cancellations

    # Book a ticket (enqueue in the booking queue)
    def book_ticket(self, customer_name):
        if self.seats_available > 0:
            self.bookings_queue.append(customer_name)
            self.seats_available -= 1
            print(f"Ticket successfully booked for {
                  customer_name}. Seats left: {self.seats_available}")
        else:
            print(f"Sorry {customer_name}, the event is fully booked.")

    # Cancel a ticket (pop from the cancellation stack)
    def cancel_ticket(self):
        if self.bookings_queue:
            canceled_booking = self.bookings_queue.pop()
            self.cancellations_stack.append(canceled_booking)
            self.seats_available += 1
            print(f"Ticket for {canceled_booking} has been canceled. Seats left: {
                  self.seats_available}")
        else:
            print("No bookings to cancel.")

    # Refund the most recent canceled ticket
    def refund_ticket(self):
        if self.cancellations_stack:
            refunded_booking = self.cancellations_stack.pop()
            print(f"Ticket for {refunded_booking} has been refunded.")
        else:
            print("No cancellations to refund.")


# Manage events in a list
events = [
    Event(601, "Concert A", "12/05/2024", 100),
    Event(602, "Theater B", "15/05/2024", 50),
]

# Example of booking, cancellation, and refund
event_concert = events[0]  # Concert A

# Book tickets
event_concert.book_ticket("Alice")
event_concert.book_ticket("Bob")

# Cancel a booking
event_concert.cancel_ticket()

# Refund a cancellation
event_concert.refund_ticket()

# View event details
for event in events:
    print(f"Event ID: {event.event_id}, Event: {event.event_name}, Date: {
          event.date}, Seats Available: {event.seats_available}")

# Define the MenuItem class to store menu items


class MenuItem:
    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price

# Define the Order class to manage orders


class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # List of items ordered

# Define the RestaurantOrderManager class to manage the system


class RestaurantOrderManager:
    def __init__(self):
        self.menu = []  # List to store menu items
        self.order_queue = deque()  # Queue for processing orders in the kitchen
        self.undo_stack = []  # Stack to undo recent orders

    # Add item to the menu
    def add_menu_item(self, item_id, item_name, price):
        item = MenuItem(item_id, item_name, price)
        self.menu.append(item)

    # Show the menu
    def show_menu(self):
        if not self.menu:
            print("The menu is empty.")
        else:
            print("Menu:")
            for item in self.menu:
                print(f"Item ID: {item.item_id}, Name: {
                      item.item_name}, Price: {item.price}")

    # Place an order (add to order queue and undo stack)
    def place_order(self, order_id, customer_name, item_ids):
        items = [item for item in self.menu if item.item_id in item_ids]
        if items:
            order = Order(order_id, customer_name, items)
            # Add to the kitchen processing queue
            self.order_queue.append(order)
            self.undo_stack.append(order)  # Track the order for potential undo
            print(f"Order {order_id} placed for {customer_name}.")
        else:
            print(f"No valid items found for order {order_id}.")

    # Process an order (remove from order queue)
    def process_order(self):
        if self.order_queue:
            order = self.order_queue.popleft()  # Process the first order in the queue
            print(f"Processing order {order.order_id} for {
                  order.customer_name}.")
        else:
            print("No orders to process.")

    # Undo the last placed order
    def undo_last_order(self):
        if self.undo_stack:
            last_order = self.undo_stack.pop()  # Undo the most recent order
            # Remove the order from the queue
            self.order_queue.remove(last_order)
            print(f"Order {last_order.order_id} for {
                  last_order.customer_name} has been undone.")
        else:
            print("No orders to undo.")


# Example usage
restaurant = RestaurantOrderManager()

# Add items to the menu
restaurant.add_menu_item(1, "Burger", 5.99)
restaurant.add_menu_item(2, "Pizza", 8.99)
restaurant.add_menu_item(3, "Pasta", 7.99)

# Show the menu
restaurant.show_menu()

# Place some orders
restaurant.place_order(101, "Alice", [1, 3])  # Alice orders a Burger and Pasta
restaurant.place_order(102, "Bob", [2])       # Bob orders a Pizza

# Process orders
restaurant.process_order()  # Process Alice's order

# Undo the last order
restaurant.undo_last_order()  # Undo Bob's order

# Show the current state of orders
restaurant.process_order()  # No more orders after undo


# Define the Event class to manage events

class Event:
    def __init__(self, event_id, event_name, date, seats_available):
        self.event_id = event_id
        self.event_name = event_name
        self.date = date
        self.seats_available = seats_available
        self.attendee_queue = deque()  # Queue to manage attendees
        self.purchase_stack = []  # Stack to track and undo ticket purchases

    # Method to book a ticket
    def book_ticket(self, customer_name):
        if self.seats_available > 0:
            # Add customer to the queue
            self.attendee_queue.append(customer_name)
            # Track the purchase in stack for undo
            self.purchase_stack.append(customer_name)
            self.seats_available -= 1  # Decrease available seats
            print(f"Ticket successfully booked for {
                  customer_name}. Seats left: {self.seats_available}")
        else:
            print(f"Sorry {customer_name}, the event is fully booked.")

    # Method to undo the last ticket purchase
    def undo_ticket_purchase(self):
        if self.purchase_stack:
            last_customer = self.purchase_stack.pop()  # Get the last ticket purchase (LIFO)
            # Remove from the attendee queue
            self.attendee_queue.remove(last_customer)
            self.seats_available += 1  # Increase available seats
            print(f"Ticket purchase for {
                  last_customer} has been undone. Seats left: {self.seats_available}")
        else:
            print("No ticket purchases to undo.")

    # Method to view the list of attendees
    def view_attendees(self):
        if self.attendee_queue:
            print(f"Attendees for {self.event_name}:")
            for attendee in self.attendee_queue:
                print(f"- {attendee}")
        else:
            print(f"No attendees for {self.event_name} yet.")

# Define the SportsEventManager class to manage all events


class SportsEventManager:
    def __init__(self):
        self.available_events = []  # List to manage available events

    # Add an event to the list of available events
    def add_event(self, event_id, event_name, date, seats_available):
        event = Event(event_id, event_name, date, seats_available)
        self.available_events.append(event)
        print(f"Event '{event_name}' has been added.")

    # Show available events
    def show_available_events(self):
        if not self.available_events:
            print("No events are available.")
        else:
            print("Available Events:")
            for event in self.available_events:
                print(f"Event ID: {event.event_id}, Name: {event.event_name}, Date: {
                      event.date}, Seats Available: {event.seats_available}")


# Example usage
manager = SportsEventManager()

# Add some events
manager.add_event(101, "Football Match", "20/10/2024", 100)
manager.add_event(102, "Basketball Game", "25/10/2024", 50)

# Show available events
manager.show_available_events()

# Access an event
football_event = manager.available_events[0]

# Book tickets
football_event.book_ticket("Alice")
football_event.book_ticket("Bob")

# View attendees
football_event.view_attendees()

# Undo the last ticket purchase
football_event.undo_ticket_purchase()

# View attendees again after undo
football_event.view_attendees()

# Show the updated available seats
manager.show_available_events()


