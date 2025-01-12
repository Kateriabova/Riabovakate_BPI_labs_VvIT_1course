def avada_kedavra(person, is_it_harry_potter=False):
    if is_it_harry_potter:
        return person
    person = ''
    return person

def expecto_patronum(name, list_of_the_potronus, is_it_death_eater=False):
    if is_it_death_eater:
        return None
    return list_of_the_potronus[len(name) % len(list_of_the_potronus)]

def expelliarmus(person, is_it_harry_potter=False):
    if is_it_harry_potter:
        person = []
    person = person.split()
    return person

