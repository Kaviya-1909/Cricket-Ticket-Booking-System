import mysql.connector
import getpass
from tabulate import tabulate
from datetime import datetime

class Ground:
    def __init__(self, ground_id, ground_name, ground_place, totalSeat):
        self.ground_id = ground_id
        self.ground_name = ground_name
        self.ground_place = ground_place
        self.totalSeat = totalSeat

class Matchdetails:
    def __init__(self, match_id, ground_id, match_name, match_date):
        self.match_id = match_id
        self.ground_id = ground_id
        self.match_name = match_name
        self.match_date = match_date

class User:
    def __init__(self, user_id, user_email, user_name, phone_num, userOrAdmin, password):
        self.user_id = user_id
        self.user_email = user_email
        self.user_name = user_name
        self.phone_num = phone_num
        self.userOrAdmin = userOrAdmin
        self.password = password

class Seat:
    def __init__(self, ground_id, match_id, VIP_seat, firstClass, secondClass, standard):
        self.ground_id = ground_id
        self.match_id = match_id
        self.VIP_seat = VIP_seat
        self.firstClass = firstClass
        self.secondClass = secondClass
        self.standard = standard

class Ticketcost:
    def __init__(self, ground_id, match_id, c_vip, c_fc, c_sc, c_st):
        self.ground_id = ground_id
        self.match_id = match_id
        self.c_vip = c_vip
        self.c_fc = c_fc
        self.c_sc = c_sc
        self.c_st = c_st

class Ticket:
    def __init__(self, ticket_id, user_id, ground_id, No_of_ticket, Seat_Type, Cost_per_ticket, totalAmount, Cur_date):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.ground_id = ground_id
        self.No_of_ticket = No_of_ticket
        self.Seat_Type = Seat_Type
        self.Cost_per_ticket = Cost_per_ticket
        self.totalAmount = totalAmount
        self.Cur_date = Cur_date

class CricketTicketBooking:
    def __init__(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kaviya@19",
                database="cricket_ticket"
            )
            self.cursor = self.db_connection.cursor()
            self.admin_email = "kaviyasekar1909@gmail.com"
            self.admin_password = "1234"
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            exit(1)

    def admin_login(self):
        email = input("Enter admin email: ")
        password = getpass.getpass("Enter admin password: ")
        
        if email == self.admin_email and password == self.admin_password:
            return True
        else:
            print("Admin login failed...")
            return False

    def user_login(self):
        user_id = input("Enter user ID: ")
        user_name = input("Enter user name: ")
        user_email = input("Enter user email: ")
        phone_num = input("Enter user mobile number: ")
        password = getpass.getpass("Enter user password: ")
        
        self.cursor.execute("SELECT * FROM user WHERE user_id = %s AND user_name = %s AND user_email = %s AND phone_num = %s AND password = %s",
                            (user_id, user_name, user_email, phone_num, password))
        user_data = self.cursor.fetchone()
        if user_data:
            print("User login successful...")
            return True
        else:
            print("Invalid user details...")
            return False

    def execute_query(self, query, params=None, fetch=False):
        try:
            self.cursor.execute(query, params) if params else self.cursor.execute(query)
            self.db_connection.commit()
            return self.cursor.fetchall() if fetch else None
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            self.db_connection.rollback()

    def add_ground(self):
        ground_id = input("Enter ground ID: ")
        ground_name = input("Enter ground name: ")
        ground_place = input("Enter ground place: ")
        totalSeat = input("Enter total seats: ")

        query = "INSERT INTO ground (ground_id, ground_name, ground_place, totalSeat) VALUES(%s, %s, %s, %s)"
        params = (ground_id, ground_name, ground_place, totalSeat)
        self.execute_query(query, params)
        print("Ground details added successfully.")

    def add_matchdetails(self):
        match_id = input("Enter match ID: ")
        ground_id = input("Enter ground ID: ")
        match_name = input("Enter match name: ")
        match_date = input("Enter match date (YYYY-MM-DD HH:MM:SS): ")

        query = "INSERT INTO matchdetails (match_id, ground_id, match_name, match_date) VALUES(%s, %s, %s, %s)"
        params = (match_id, ground_id, match_name, match_date)
        self.execute_query(query, params)
        print("Match details added successfully.")

    def add_user(self):
        user_id = input("Enter user ID: ")
        user_email = input("Enter user email: ")
        user_name = input("Enter user name: ")
        phone_num = input("Enter phone number: ")
        userOrAdmin = input("Enter user type (user/admin): ")
        
        while True:
            password = getpass.getpass("Enter password: ")
            if len(password) > 20:  # Assume the column length for password is 20 characters
                print("Password too long, please enter a password with a maximum of 20 characters.")
            else:
                break

        query = "INSERT INTO user (user_id, user_email, user_name, phone_num, userOrAdmin, password) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (user_id, user_email, user_name, phone_num, userOrAdmin, password)
        self.execute_query(query, params)
        
        print("User added successfully.")

    def add_seat(self):
        ground_id = input("Enter ground ID: ")
        match_id = input("Enter match ID: ")
        VIP_seat = input("Enter VIP seats: ")
        firstClass = input("Enter first class seats: ")
        secondClass = input("Enter second class seats: ")
        standard = input("Enter standard seats: ")

        query = "INSERT INTO seat (ground_id, match_id, VIP_seat, firstClass, secondClass, standard) VALUES(%s, %s, %s, %s, %s, %s)"
        params = (ground_id, match_id, VIP_seat, firstClass, secondClass, standard)
        self.execute_query(query, params)
        print("Seat details added successfully.")

    def add_ticketcost(self):
        ground_id = input("Enter ground ID: ")
        match_id = input("Enter match ID: ")
        c_vip = input("Enter cost for VIP seats: ")
        c_fc = input("Enter cost for first class seats: ")
        c_sc = input("Enter cost for second class seats: ")
        c_st = input("Enter cost for standard seats: ")

        query = "INSERT INTO ticketcost (ground_id, match_id, c_vip, c_fc, c_sc, c_st) VALUES(%s, %s, %s, %s, %s, %s)"
        params = (ground_id, match_id, c_vip, c_fc, c_sc, c_st)
        self.execute_query(query, params)
        print("Ticket Cost details added successfully.")

    def add_ticket(self):
        ticket_id = input("Enter ticket ID: ")
        user_id = input("Enter user ID: ")
        ground_id = input("Enter ground ID: ")
        No_of_ticket = input("Enter number of tickets: ")
        Seat_Type = input("Enter seat type: ")
        Cost_per_ticket = input("Enter cost per ticket: ")
        totalAmount = input("Enter total amount: ")
        Cur_date = input("Enter current date (YYYY-MM-DD HH:MM:SS): ")

        query = "INSERT INTO ticket (ticket_id, user_id, ground_id, No_of_ticket, Seat_Type, Cost_per_ticket, totalAmount, Cur_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (ticket_id, user_id, ground_id, No_of_ticket, Seat_Type, Cost_per_ticket, totalAmount, Cur_date)
        self.execute_query(query, params)
        print("Ticket details added successfully.")

    def view_entities(self, entity_name):
        if entity_name not in ["ground", "matchdetails", "user", "seat", "ticketcost", "ticket"]:
            print("Invalid table name...")
            return

        self.cursor.execute(f"SELECT * FROM {entity_name}")
        entities = self.cursor.fetchall()

        if not entities:
            print("No records found...")
            return

        headers = [i[0] for i in self.cursor.description]
        print(tabulate(entities, headers=headers, tablefmt="grid"))

    def delete_entity(self, table_name):
        if table_name not in ["ground", "matchdetails", "user", "seat", "ticketcost", "ticket"]:
            print("Invalid table name...")
            return

        primary_key_name = input("Enter the name of the primary key column: ")
        record_id = input(f"Enter the value of the primary key for the record to delete in {table_name}: ")

        query = f"DELETE FROM {table_name} WHERE {primary_key_name} = %s"
        self.execute_query(query, (record_id,))
        print("Entity deleted successfully...")

    def update_ground(self):
        self.update_entity('ground')

    def update_matchdetails(self):
        self.update_entity('matchdetails')

    def update_user(self):
        self.update_entity('user')

    def update_seat(self):
        self.update_entity('seat')

    def update_ticketcost(self):
        self.update_entity('ticketcost')

    def update_ticket(self):
        self.update_entity('ticket')

    def update_entity(self, entity_name):
        try:
            # Get the primary key column name for the entity
            self.cursor.execute(f"SHOW KEYS FROM {entity_name} WHERE Key_name = 'PRIMARY'")
            primary_key_info = self.cursor.fetchone()
            if primary_key_info is None:
                print(f"No primary key found for {entity_name}.")
                return
            
            primary_key_column = primary_key_info[4]  # The fifth element contains the column name of the primary key

            # Get the primary key value from the user
            primary_key_value = input(f"Enter the primary key value of the record to update in {entity_name}: ").strip()

            # Get the columns of the entity
            self.cursor.execute(f"SHOW COLUMNS FROM {entity_name}")
            columns = [column[0] for column in self.cursor.fetchall()]
            print(f"Columns in {entity_name}: {columns}")

            # Get the column to update from the user
            column_to_update = input("Enter the column name you want to update: ").strip()

            if column_to_update not in columns:
                print("Error: Invalid column name.")
                return

            # Get the new value for the column to update
            new_value = input(f"Enter the new value for {column_to_update}: ").strip()

            # Construct and execute the update query
            query = f"UPDATE {entity_name} SET {column_to_update} = %s WHERE {primary_key_column} = %s"
            params = (new_value, primary_key_value)
            
            self.execute_query(query, params)
            print(f"{column_to_update} updated successfully.")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")




def main():
    ticket_booking = CricketTicketBooking()

    try:
        while True:
            print("1. Admin Login")
            print("2. User Login")
            print("3. Exit")

            choice = input("Enter your choice: \n")

            if choice == '1':
                if ticket_booking.admin_login():
                    admin_menu(ticket_booking)
            elif choice == '2':
                if ticket_booking.user_login():
                    user_menu(ticket_booking)
            elif choice == '3':
                print("Exiting Program...")
                break
            else:
                print("Invalid choice.")
    finally:
        if ticket_booking.cursor:
            ticket_booking.cursor.close()
        if ticket_booking.db_connection:
            ticket_booking.db_connection.close()
        


def admin_menu(ticket_booking):
    while True:
        print("\nAdmin Menu:")
        print("1. Add ground")
        print("2. Add matchdetails")
        print("3. Add user")
        print("4. Add Seat")
        print("5. Add Ticketcost")
        print("6. Add Ticket")
        print("7. View ground")
        print("8. View matchdetails")
        print("9. View user")
        print("10. View Seat")
        print("11. View Ticketcost")
        print("12. View Ticket")
        print("13. Update ground")
        print("14. Update matchdetails")
        print("15. Update user")
        print("16. Update Seat")
        print("17. Update Ticketcost")
        print("18. Update Ticket")
        print("19. Delete ground")
        print("20. Delete matchdetails")
        print("21. Delete user")
        print("22. Delete Seat")
        print("23. Delete Ticketcost")
        print("24. Delete ticket")
        print("25. Logout")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            ticket_booking.add_ground()
        elif choice == '2':
            ticket_booking.add_matchdetails()
        elif choice == '3':
            ticket_booking.add_user()
        elif choice == '4':
            ticket_booking.add_seat()
        elif choice == '5':
            ticket_booking.add_ticketcost()
        elif choice == '6':
            ticket_booking.add_ticket()
        elif choice == '7':
            print("\n")
            ticket_booking.view_entities("ground")
        elif choice == '8':
            print("\n")
            ticket_booking.view_entities("matchdetails")
        elif choice == '9':
            print("\n")
            ticket_booking.view_entities("user")
        elif choice == '10':
            print("\n")
            ticket_booking.view_entities("seat")
        elif choice == '11':
            print("\n")
            ticket_booking.view_entities("ticketcost")
        elif choice == '12':
            print("\n")
            ticket_booking.view_entities("ticket")
        elif choice == '13':
            ticket_booking.update_entity("ground")
        elif choice == '14':
            ticket_booking.update_entity("matchdetails")
        elif choice == '15':
            ticket_booking.update_entity("user")
        elif choice == '16':
            ticket_booking.update_entity("seat")
        elif choice == '17':
            ticket_booking.update_entity("ticketcost")
        elif choice == '18':
            ticket_booking.update_entity("ticket")
        elif choice == '19':
            ticket_booking.delete_entity("ground")
        elif choice == '20':
            ticket_booking.delete_entity("matchdetails")
        elif choice == '21':
            ticket_booking.delete_entity("user")
        elif choice == '22':
            ticket_booking.delete_entity("seat")
        elif choice == '23':
            ticket_booking.delete_entity("ticketcost")
        elif choice == '24':
            ticket_booking.delete_entity("ticket")
        elif choice == '25':
            print("Logging out.")
            break
        else:
            print("Invalid choice.")

def user_menu(ticket_booking):
    while True:
        print("\nUser Menu:")
        print("1. View Matches")
        print("2. View Grounds")
        print("3. View Seat")
        print("4. View Ticketcost")
        print("5. View Tickets")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            ticket_booking.view_entities("matchdetails")
        elif choice == '2':
            ticket_booking.view_entities("ground")
        elif choice == '3':
            print("\n")
            ticket_booking.view_entities("seat")
        elif choice == '4':
            print("\n")
            ticket_booking.view_entities("ticketcost")
        elif choice == '5':
            print("\n")
            ticket_booking.view_entities("ticket")
        elif choice == '6':
            print("Logging out.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
