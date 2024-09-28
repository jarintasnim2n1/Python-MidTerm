
class Hall:
    def __init__(self, row, col, hall_no) -> None:
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        
        self.__seats[id] = []
        
        for i in range(self.__row):
            cl = []
            for j in range(self.__col):
                cl.append(0)
            self.__seats[id].append(cl) 

    def book_seats(self, id, seat_list):
        show = next((show for show in self.__show_list if show[0] == id), None)
        
        if (show):
            show_id = show[0]
            for seat in seat_list:
                if seat[0] >= self.__row or seat[1] >= self.__col:
                    print(f' Seat {seat} is not available.')
                else:
                    if (self.__seats[show_id][seat[0]][seat[1]] == 0):
                        self.__seats[show_id][seat[0]][seat[1]] = 1
                        print(f'Seat {seat}is booked for show {id}')
                    else:
                        print(f' Seat {seat} is already booked for show {id}.')
        else:
            print(f'show ID: {id} is not valid.') 
    
    def view_show_list(self):
        print("************")
        for show in self.__show_list:
            print(f"MOVIE Name: {show[1]}({show[0]}) Show ID: {show[0]} Time: {show[2]}")
        print("*************")  
             
    def view_available_seats(self, id):
        show = next((show for show in self.__show_list if show[0] == id), None)
        print("***********")
        if (show):
            show_id = show[0]
            for i in range(self.__row):
                for j in range(self.__col):
                    print(self.__seats[show_id][i][j], end=" ")
            
                print()
                    
        else:
            print(f'Show ID: {id} is not valid.')
        print("***********")           
            
                      
class Star_Cinema:
    __hall_list = []
    
    def __init__(self) -> None:
        pass
   
    def entry_hall(self, hall_obj):
        self.__hall_list.append(hall_obj)
        
    @property
    def Hall_list(self):
        return self.__hall_list
            
            
hall_obj = Hall(9, 11, 33)    
cinema = Star_Cinema() 
cinema.entry_hall(hall_obj)

hall_obj.entry_show(122, "The wild Robot", "27-9-2024  11:00PM") 
hall_obj.entry_show(233, "The Universal Theory", "20-6-2024  10:30PM") 
hall_obj.entry_show(344, "This Place Rules", "30-12-2022   12:00AM")  


def main():
    while True:
        
        print(" --> Here given some  queue <--")
        
        print("\n\t1. View all Show Today")
        print("\t2. View Available Seats")
        print("\t3. Book Ticket")
        print("\t4. Exit")
        
        n = int(input("ENTER OPTION: "))
        
        if n == 1:
            for hall_obj in cinema.Hall_list:
                hall_obj.view_show_list()
        elif n == 2:
            show_id = int(input("Enter Show Id: "))
            hall_obj.view_available_seats(show_id)
        elif n == 3:
            show_id = int(input("Enter Show Id: "))
            number_of_tickets = int(input("Enter Number of Tickets: "))
            tickets = []
            
            for i in range(number_of_tickets):
                row = int(input(f'Enter the Seat {i + 1} row: '))
                col = int(input(f'Enter the Seat {i + 1} col: '))
                tickets.append((row, col))

            hall_obj.book_seats(show_id, tickets)
        elif n == 4:
            break
        else:
            print("Please Enter a valid option.")
            
            
main()          