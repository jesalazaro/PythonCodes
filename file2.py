import pickle

with open("files/programming_powers.pkl", "rb") as p_file:
    list1 = pickle.load(p_file)
    list2 = pickle.load(p_file)
    dict1 = pickle.load(p_file)

print(list1)
print(list2)
print(dict1)
