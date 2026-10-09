from lib.tyre import *

def test_tyre_add_and_view_current_readings():
    tyre = Tyre()
    tyre.add_readings(30, 20, '09/10/2026')
    
    assert tyre.get_current() == {
        'Pressure': 30,
        'Depth': 20,
        'created_on': '09/10/2026'
    }

def test_view_history_of_tyre_readings():
    tyre = Tyre()
    tyre.add_readings(30, 20, '09/10/2026')
    assert tyre.view_history() == [
        {'Pressure': 0,
        'Depth': 0,
        'created_on': 0} ,

        {'Pressure': 30,
        'Depth': 20,
        'created_on': '09/10/2026'
        }
    ]

