from fleet.ambulance import Ambulance
from operations import *
from personnel import *
from fleet.station import Station


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident(1, "Power outage in sector 4", 1, "12:30", "Tomasz Dąbrowa")
    incident2 = Incident(2, "Fire alarm in building 21", 2, "13:30", "Hugon Kołłątaj")
    queue += incident1
    queue += incident2

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")
    print(ambulance1)
    print(incident1)
    # ZADANIE 3
    station1 = Station(1, "Bytom", ambulance1, driver1, employee1)
    station2 = Station(2, "Chorzów", ambulance2, driver2, employee2)
    station1.check_location(ambulance1.location)


if __name__ == "__main__":
    run_application()