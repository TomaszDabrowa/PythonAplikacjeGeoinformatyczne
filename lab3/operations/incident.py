import time as czas

class Incident:
    # ZADANIE 2
    def __init__(self, id, description, priority, time, reporter, location):
        self.id = id
        self.description = description
        self.priority = priority
        self.time = time
        self.reporter = reporter
        self.location = location
        self.startTimeStamp = czas.time() 

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, priority: {self.priority}, time: {self.time}, reporter: {self.reporter}"
    
    # ZADANIE 4
    def showPriority(self):
        print(f"Incident priority: {self.priority}")

    def durationTime(self):
        tmp = czas.time() - self.startTimeStamp
        tmp /= 60
        tmp = round(tmp, 2)
        print(f"Czas, który minął od zgłoszenia: {tmp} min")

        
    