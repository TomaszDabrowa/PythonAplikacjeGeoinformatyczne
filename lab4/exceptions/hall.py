from seat import Seat

class Wyjatek(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Hall:
    seats = []
    
    def __init__(self):
        self.seats = [None] * 10
        for i in range(10):
            self.seats[i] = Seat(i)
        for i in range(10):
            self.seats[i] = Seat(i)

    def bookSeat(self, seatNumber, user):

        # check if specified user has already booked seat
        for i in range(10):
            osoba = self.seats[i].info["name"]
            if osoba == user.name:
                raise Wyjatek("You have already booked one seat. Cancel your reservation in order to book different seat")
                break
        
        # check if there are free seats
        free = False
        for i in range (10):
            osoba = self.seats[i].info["name"]
            if osoba == "":
                free = True
                break
        
        if free == False:
            raise Wyjatek("All of seats are booked")
        
        # check if selected seat is free
        if self.seats[seatNumber].info["name"] != "":
            raise Wyjatek("Selected seat is booked")
        
        # if all things are OK
        self.seats[seatNumber].info["name"] = user.name

    def cancelReservation(self, seatNumber, user):

        #check if it is correct user
        if self.seats[seatNumber].info["name"] != user.name:
            raise Wyjatek("You are not occupying that seat")
        
        self.seats[seatNumber].info["name"] = ""
