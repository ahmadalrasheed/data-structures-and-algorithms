from code_challenges.animal_shelter.animal_shelter import AnimalShelter, Dog, Cat, Lion
import pytest

# test enqueing dogs and cats to animal shelter
def test_AnimalShelter_have_values():
    #arrange
    Element1=Dog()
    Element2=Dog()
    Element3=Cat()
    Element4=Dog()
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)
    Expected=' dog->  dog->  cat->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected


# test enqueing another animal to animal shelter


def test_AnimalShelter_enqueue_another_animal():
    #arrange
    Element1=Dog()
    Element2=Dog()
    Element3=Cat()
    Element4=Lion()
    Element5=Lion()
    Element6=Dog()
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)
    animal_shelter.enqueue(Element5)
    animal_shelter.enqueue(Element6)
    Expected=' dog->  dog->  cat->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected

# test dequeing animal

def test_AnimalShelter_dequeue_cat():
    #arrange
    Element1=Dog()
    Element2=Dog()
    Element3=Cat()
    Element4=Dog()
    Element5=Dog()
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)
    animal_shelter.enqueue(Element5)


    # dequeue the cat
    animal_shelter.dequeue(Element3)

    Expected=' dog->  dog->  dog->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected

def test_AnimalShelter_dequeue_dog():
    #arrange
    Element1=Cat()
    Element2=Dog()
    Element3=Cat()
    Element4=Dog()
    Element5=Dog()
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)
    animal_shelter.enqueue(Element5)


    # dequeue the cat
    animal_shelter.dequeue(Element2)

    Expected=' cat->  cat->  dog->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected



def test_AnimalShelter_dequeue_two_dogs():
    #arrange
    Element1=Cat()
    Element2=Dog()
    Element3=Cat()
    Element4=Dog()
    Element5=Dog()
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)
    animal_shelter.enqueue(Element5)


    # dequeue the cat
    animal_shelter.dequeue(Element2)
    animal_shelter.dequeue(Element4)

    Expected=' cat->  cat->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected




def test_AnimalShelter_dequeue_first():
    #arrange
    Element1=Cat()
    Element2=Dog()
    Element3=Cat()

    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)


    # dequeue the cat
    animal_shelter.dequeue(Element1)


    Expected=' dog->  cat-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected


def test_AnimalShelter_dequeue_multiple_elements():
    #arrange
    Element1=Cat()
    Element2=Dog()
    Element3=Cat()
    Element4=Dog()

    animal_shelter=AnimalShelter()
    animal_shelter.enqueue(Element1)
    animal_shelter.enqueue(Element2)
    animal_shelter.enqueue(Element3)
    animal_shelter.enqueue(Element4)


    # dequeue the cat
    animal_shelter.dequeue(Element1)
    animal_shelter.dequeue(Element3)


    Expected=' dog->  dog-> '
    #act

    actual=animal_shelter.print_queue()

    # assert
    assert actual==Expected





def test_shelter_enqueue_value(animal_queue):
     # Arrange
    expected = "bog"

    # Act
    actual = animal_queue.front.value

    # Assert
    assert actual == expected




def test_shelter_enqueue_multiple(animal_queue):
     # Arrange
    expected_1 = "bog"
    expected_2 = "sog"

    # Act
    actual_1 = animal_queue.front.value
    actual_2 = animal_queue.front.next.value

    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2




def test_shelter_dequeue_empties_shelter(animal_queue):
    # Act
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")



@pytest.fixture
def animal_queue():
    shelter = AnimalShelter()

    bog = Dog("bog")
    sog = Dog("sog")
    log = Dog("log")
    hog = Dog("hog")

    mat = Cat("mat")
    pat = Cat("pat")
    fat = Cat("fat")
    nat = Cat("nat")

    shelter.enqueue(bog)
    shelter.enqueue(sog)
    shelter.enqueue(log)
    shelter.enqueue(hog)

    shelter.enqueue(mat)
    shelter.enqueue(pat)
    shelter.enqueue(fat)
    shelter.enqueue(nat)

    return shelter




