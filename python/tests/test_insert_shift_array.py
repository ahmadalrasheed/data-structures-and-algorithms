
from code_challenges.insertShiftArray.insertShiftArray import insertShiftArray



def test_insert_Shift_Array():
    input_array=[1,2,3,4]
    predicted=insertShiftArray(input_array,99)
    actual=[1,2,99,3,4]
    assert predicted==actual

