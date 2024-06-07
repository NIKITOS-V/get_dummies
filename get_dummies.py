import random
import pandas as pd

def create_data():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})

    return data


def get_dummies(data):
    new_list = [Object for List in data.values for Object in List]

    new_data = pd.DataFrame()

    for index, name in enumerate(set(new_list)):
        new_data.insert(index, name, [1 if Object == name else 0 for Object in new_list])

    return new_data


print(get_dummies(create_data()))
