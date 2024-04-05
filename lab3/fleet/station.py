# ZADANIE 3

class Station:
    __slots__ = ['id', 'location', 'ambulance', 'driver', 'employee']
    __instances_count = 0
    
    def __init__(self, id, location, ambulance, driver, employee):
        self.id = id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__instances_count += 1
    
    def check_location(self, lokalizacja):
        if lokalizacja == "Bytom":
            print("Ambulance is in station")
        else:
            print("Ambulance is outside the station")
    