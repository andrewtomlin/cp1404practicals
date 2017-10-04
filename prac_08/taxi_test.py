from prac_08.taxi import Taxi
from prac_08.unreliable_car import UnreliableCar


def main():
    """Taxi class tester"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
