class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") and person.get("wife") is not None:
            spouse = person["wife"]
            husband = person["name"]
            wife = Person.people[spouse]
            Person.people[husband].wife = wife

        if person.get("husband") and person.get("husband") is not None:
            spouse = person["husband"]
            wife = person["name"]
            husband = Person.people[spouse]
            Person.people[wife].husband = husband

    return persons
