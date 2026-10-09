# Car and Tyre Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

car
- left_tyre = tyre()
- right_tyre = 
- rear_right = 
- rear_left = 

tyres
 - tyre pressure (current)
 - tyre depth (current)
 - history of the tyres
    - historic pressure readingfs
    - historic depth readings

- car.current_readings => {
    left tyre = {
        pressure: 30, 
        depth: 20mm,
        created_on: 01/01/2026
    }
    right tyre = {
        pressure: 30, 
        depth: 20mm,
        created_on: 01/01/2026
    }
}

- latest_reading()


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car                        │
│                            │
│ - current_readings()       │
│                            │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Tyre.                   │
│                         │
│ - pressure  -> get               │
│ - depth -> get               │
│ - history 
│ - add_reading(pressure or depth)
│                         │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:
    # User-facing properties:
    #   tyres (position of tyre object): many Tyre objects

    def __init__(self):
        # left_tyre = Tyre
        # right_tyre = Tyre
        # rear_left = Tyre
        # rear_right = Tyre

    def current_readings(self):
        # Parameters:
        #   none
        # Returns:
        #   a list of current readings for each position of tyre
        #   
        # Side-effects:
        #   none
        pass # No code here yet
    
    def view_all_history(self):
        # Parameters:
        #   none
        # Returns:
        #   historical readings for each position of tyre
        # Side-effects:
        #   none
        pass # No code here yet


class Tyre:
    # User-facing properties:
    #   history: list of dicts with presure, depth and time

    def __init__(self, pressure, depth):
        # Parameters:
        #   history: list of dicts
        # Side-effects:
        #   Sets the initial readings for pressure, depth and the current time
        pass # No code here yet

    def get_current(self):
        # Returns:
        #   returns current reading for both readings as ints
        # Side-effects:
        #   None
        pass # No code here yet
    
    def add_readings(self, pressure, depth, date):
        # Parameters:
        #   pressure: int
        #   depth: int
        #   date: string
        # Side-effects:
        #   adds pressure and depth and time readings given to the history

        # import datetime
        # now = datetime.now() -> 'y/m/d h:m'
    
    def view_history(self):
        # parameters:
        #   none
        # returns
        #   list of dicts containing all readings for that tyre
        # side effect:
        #   none

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a tyre pressure and depth
add_readings
"""
tyre = Tyre()
tyre.add(30, 20, '09/10/2026')
tyre.get_crrent == {
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
}
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python


"""
View history
returns history of readings
"""
tyre = Tyre()
tyre.add(30, 20, '09/10/2026')
tyre.view_history == [
    {
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
    }
]


"""
View history
returns history of readings
"""
car = Car()
car.left= Tyre()
car.right = Tyre()
car.rear_left = Tyre()
car.rear_right = Tyre()

assert car.left == Tyre()
assert car.right == Tyre()
assert car.rear_left == Tyre()
assert car.rear_right== Tyre()


"""
viewing current readings
"""
car = Car()
car.left= Tyre(30, 20, '09/10/2026')
car.right = Tyre(10, 10, '09/10/2026')
car.rear_left = Tyre(30, 20, '09/10/2026')
car.rear_right = Tyre(10, 10, '09/10/2026')

assert car.current_readings() == {
    'left' :
    {
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
    }
    'right':
    {
    'pressure': 10,
    'depth': 10,
    'created_on': '09/10/2026'
    }
    'rear_left':
    {
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
    }
    'rear_right':
    {
    'pressure': 10,
    'depth': 10,
    'created_on': '09/10/2026'
    }
}

"""
VIEW ALL HISTORY
"""
car = Car()
car.left= Tyre(30, 20, '09/10/2026')
car.right = Tyre(10, 10, '09/10/2026')
car.rear_left = Tyre(30, 20, '09/10/2026')
car.rear_right = Tyre(10, 10, '09/10/2026')

car.left.add_readings(100,100, '20/10/2027')
car.right.add_readings(100,100, '20/10/2027')
car.rear_left.add_readings(100,100, '20/10/2027')
car.rear_right.add_readings(100,100, '20/10/2027')


assert car.view_all_history() == {
    'left' :
    [{
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
    },
    {
    'pressure': 100,
    'depth': 100,
    'created_on': '20/10/2027'
    }],

    'right':
    [{
    'pressure': 10,
    'depth': 10,
    'created_on': '09/10/2026'
    },
    {
    'pressure': 100,
    'depth': 100,
    'created_on': '20/10/2027'
    }],

    'rear_left':
    [{
    'pressure': 30,
    'depth': 20,
    'created_on': '09/10/2026'
    },
    {
    'pressure': 100,
    'depth': 100,
    'created_on': '20/10/2027'
    }],

    'rear_right':
    [{
    'pressure': 10,
    'depth': 10,
    'created_on': '09/10/2026'
    },
    {
    'pressure': 100,
    'depth': 100,
    'created_on': '20/10/2027'
    }],
}
```
class Tyre():
    def init(pressure=0, depth=20)
    self.pressure = pressure

tyre = Tyre(depth=32)