class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        person_obj = Person.people.get(person.get("name"))

        if wife and wife is not None:
            person_obj.wife = Person.people.get(wife)

        if husband and husband is not None:
            person_obj.husband = Person.people.get(husband)

    return persons
