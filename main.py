import pandas as pd
data = pd.read_csv("train.csv", names=('PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                                       'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'))
data_dict_list = []
str_map = {'male': 1, 'female': 0, }
for v in data.values:
    data_dict_list.append({'Survived': v[1], 'Pclass': v[2], 'Sex': str_map[v[4]], 'Age': v[5], 'SibSp': v[6], 'Parch': v[7]})
for i in data_dict_list:
    print(i)