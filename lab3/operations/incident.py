class Incident:
    # ZADANIE 2
    def __init__(self, id, description, priority, time, reporter):
        self.id = id
        self.description = description
        self.priority = priority
        self.time = time
        self.reporter = reporter

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, priority: {self.priority}, time: {self.time}, reporter: {self.reporter}"