import datetime
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from typing import List


class Size(str, Enum):
    mini = "Mini"
    medium = "Medium"
    large = "Large"


@dataclass
class Car:
    model: str
    size: Size
    price: Decimal


@dataclass
class Rent:
    car: Car
    date_start: datetime.date
    date_end: datetime.date


@dataclass
class Garage:
    cars: List[Car]
    rents: List[Rent]

    def add_car(self, car: Car):
        self.cars.append(car)

    def filter_by_price(self, max_price: Decimal) -> List[Car]:
        return [
            car
            for car in self.cars
            if car.price <= max_price
        ]

    def filter_by_size(self, size: Size) -> List[Car]:
        return [
            car
            for car in self.cars
            if car.size == size
        ]

    def rent_car(self, car: Car, date_start: datetime.date, date_end: datetime.date) -> bool:
        assert car in self.cars
        for rent in self.rents:
            if rent.car == car:
                if date_start <= rent.date_start <= date_end:
                    return False
                if date_start <= rent.date_end <= date_end:
                    return False
        self.rents.append(Rent(
            car=car,
            date_start=date_start,
            date_end=date_end,
        ))
        return True


garage = Garage(
    cars=list(),
    rents=list(),
)

garage.add_car(
    car=Car(
        model="Toyota",
        size=Size.medium,
        price=Decimal(200),
    )
)

garage.add_car(
    car=Car(
        model="Mazda",
        size=Size.medium,
        price=Decimal(300),
    )
)

garage.add_car(
    car=Car(
        model="Lambo",
        size=Size.mini,
        price=Decimal(500),
    )
)

print(garage.cars)
print(garage.filter_by_size(Size.mini))
print(garage.filter_by_price(Decimal(300)))
some_car = garage.cars[0]
# первая бронь работает на сегодня
print(garage.rent_car(
    car=some_car,
    date_start=datetime.datetime.today(),
    date_end=datetime.datetime.today() + datetime.timedelta(days=3),
))
# вторая не работает, так как машина на эти дни занята
print(garage.rent_car(
    car=some_car,
    date_start=datetime.datetime.today(),
    date_end=datetime.datetime.today() + datetime.timedelta(days=3),
))
# третья работает, так как другие дни
print(garage.rent_car(
    car=some_car,
    date_start=datetime.datetime.today() + datetime.timedelta(days=4),
    date_end=datetime.datetime.today() + datetime.timedelta(days=5),
))