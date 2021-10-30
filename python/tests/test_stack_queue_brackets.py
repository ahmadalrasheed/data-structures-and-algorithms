from code_challenges.stackqueuebrackets.stack_queue_brackets import validate_brackets


def test_validate_brackets_case_1():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}")

    #Assert
    assert actual == expected


def test_validate_brackets_case_2():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}(){}")

    #Assert
    assert actual == expected


def test_validate_brackets_case_3():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("()[[Extra Characters]]")

    #Assert
    assert actual == expected


def test_validate_brackets_case_4():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(){}[[]]")

    #Assert
    assert actual == expected



def test_validate_brackets_case_5():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}{Code}[Fellows](())")

    #Assert
    assert actual == expected


def test_validate_brackets_case_6():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("WILL([])()({)(})BE(())TRUE")

    #Assert
    assert actual == expected



def test_validate_brackets_case_7():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("[({}]")

    #Assert
    assert actual == expected


def test_validate_brackets_case_8():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(](")

    #Assert
    assert actual == expected


def test_validate_brackets_case_9():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("{(})")

    #Assert
    assert actual == expected

def test_validate_brackets_case_10():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(([{[()]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_11():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(([{[)(]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_12():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(([{)[(]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_13():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(([{)[(]}]})")

    #Assert
    assert actual == expected
