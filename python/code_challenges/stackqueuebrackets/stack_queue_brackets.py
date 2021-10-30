from data_structure.stack_and_queue.queue  import Queue
from data_structure.stack_and_queue.stack  import Stack

# from queue  import Queue
# from stack  import Stack


def validate_brackets(string):
    """
    Representing whether or not the brackets in the string are balanced.
    -----------------
    Arguments:
    string: string
    Return: boolean
    """

    brackets = {
    "paranthesis_open" : "(",
    "paranthesis_closed" : ")",

    "bracket_open" : "[",
    "bracket_closed" : "]",

    "curly_open" : "{",
    "curly_closed" : "}"
    }

    string_queue = Queue()
    queue_counter = 0
    string_stack = Stack()
    stack_counter = 0

    alternate = True
    validation = True

    for char in string:
        if (char in brackets.values()) and (alternate == True):
            string_queue.enqueue(char)
            alternate = False
            queue_counter += 1
            continue

        if (char in brackets.values()) and (alternate == False):
            string_stack.push(char)
            alternate = True
            stack_counter += 1
            continue

    queue_node = string_queue.front
    stack_node = string_stack.top


    while queue_node:

        validation = False

        if queue_node.value == brackets["paranthesis_open"]:
            expected_value = brackets["paranthesis_closed"]

        elif queue_node.value == brackets["bracket_open"]:
            expected_value = brackets["bracket_closed"]

        elif queue_node.value == brackets["curly_open"]:
            expected_value = brackets["curly_closed"]

        elif queue_node.value == brackets["paranthesis_closed"]:
            expected_value = brackets["paranthesis_open"]

        elif queue_node.value == brackets["bracket_closed"]:
            expected_value = brackets["bracket_open"]

        elif queue_node.value == brackets["curly_closed"]:
            expected_value = brackets["curly_open"]



        stack_node = string_stack.top

        while stack_node:
            if stack_node.value == expected_value:
                stack_node.value = ""
                validation = True

                break

            stack_node = stack_node.next


        queue_node = queue_node.next

    print(validation)
    return validation


