class trip:

    def __init__(self, destination, starting_date, end_date, amount_of_trouser):
        self.destination = destination
        self.starting_date = starting_date
        self.end_date = end_date
        self.amount_of_trouser = amount_of_trouser

    def to_string(self):
        return(self.destination + self.starting_date + self.end_date + self.amount_of_trouser)