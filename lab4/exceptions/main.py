from user import User
from hall import Hall, Wyjatek
user = User("Tomasz")
print(f"Imię rezerwującego: {user.name}")

hall = Hall()



try:
    hall.bookSeat(1, user)
except Wyjatek as e:
    print("Error occured: ", e.message)
else:
    print("You have booked your seat successfully")

try:
    hall.bookSeat(1, user)
except Wyjatek as e:
    print("Error occured: ", e.message)
else:
    print("You have booked your seat successfully")

try:
    hall.cancelReservation(1, user)
except Wyjatek as e:
    print("Error occured: ", e.message)
else:
    print("You have cancelled your reservation successfully")

try:
    hall.cancelReservation(1, user)
except Wyjatek as e:
    print("Error occured: ", e.message)
else:
    print("You have cancelled your reservation successfully")  