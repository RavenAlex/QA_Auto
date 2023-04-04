import random

from data.data import Person, Color, Date, Value, Select
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(500, 2000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    path = rf'C:\test\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello world{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00",
    )
def generated_value():
    yield Value(
        value_name=["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option", "Another root option"]
    )

def generated_select():
    yield Select(
        select_one_name=["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
    )

