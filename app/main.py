class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        persons.append(person_obj)

    for person in people:
        if "wife" in person and person["wife"] is not None:
            spouse = person["wife"]
            husband = person["name"]
            wife = Person.people[spouse]
            Person.people[husband].wife = wife

        if "husband" in person and person["husband"] is not None:
            spouse = person["husband"]
            wife = person["name"]
            husband = Person.people[spouse]
            Person.people[wife].husband = husband

    return persons
