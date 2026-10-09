from lib.car import *
from lib.tyre import *

def test_car_has_tyres():
    car = Car()
    
    assert car.left.history[-1]['Pressure'] == 0
    assert car.right.history[-1]['Pressure'] == 0
    assert car.rear_left.history[-1]['Pressure'] == 0
    assert car.rear_right.history[-1]['Pressure'] == 0

def test_view_current_readings_of_all_tyres():
    car = Car()
    car.left= Tyre(30, 20, '09/10/2026')
    car.right = Tyre(10, 10, '09/10/2026')
    car.rear_left = Tyre(30, 20, '09/10/2026')
    car.rear_right = Tyre(10, 10, '09/10/2026')

    assert car.current_readings() == {
        'left' :
        {
        'Pressure': 30,
        'Depth': 20,
        'created_on': '09/10/2026'
        },
        'right':
        {
        'Pressure': 10,
        'Depth': 10,
        'created_on': '09/10/2026'
        },
        'rear_left':
        {
        'Pressure': 30,
        'Depth': 20,
        'created_on': '09/10/2026'
        },
        'rear_right':
        {
        'Pressure': 10,
        'Depth': 10,
        'created_on': '09/10/2026'
        }
    }

    def test_view_all_tyre_history():
        car = Car()
        car.left= Tyre(30, 20, '09/10/2026')
        car.right = Tyre(10, 10, '09/10/2026')
        car.rear_left = Tyre(30, 20, '09/10/2026')
        car.rear_right = Tyre(10, 10, '09/10/2026')



        assert car.view_all_history() == {
            'left' :
            [{'Pressure': 0,
            'Depth': 0,
            'created_on': 0} ,
            {
            'Pressure': 30,
            'Depth': 20,
            'created_on': '09/10/2026'
            }
            ],

            'right':
            [{'Pressure': 0,
            'Depth': 0,
            'created_on': 0} ,
            {
            'Pressure': 10,
            'Depth': 10,
            'created_on': '09/10/2026'
            }],

            'rear_left':
            [{'Pressure': 0,
            'Depth': 0,
            'created_on': 0} ,
            {
            'Pressure': 30,
            'Depth': 20,
            'created_on': '09/10/2026'
            }],

            'rear_right':
            [{'Pressure': 0,
            'Depth': 0,
            'created_on': 0} ,
            {
            'Pressure': 10,
            'Depth': 10,
            'created_on': '09/10/2026'
            }]
        }