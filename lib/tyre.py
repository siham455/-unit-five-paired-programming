class Tyre:
    # User-facing properties:
    #   history: list of dicts with presure, depth and time

    def __init__(self, pressure=0, depth=0, date=0):
        self.history = [{'Pressure' : pressure, 'Depth' : depth, 'created_on' : date }]

    def get_current(self):
        return self.history[-1]
        
    
    def add_readings(self, pressure, depth, date):
        reading = {'Pressure' : pressure, 'Depth' : depth, 'created_on' : date }
        self.history.append(reading)

    def view_history(self):
        return self.history
