dictc = {"country": ["Brazil", "Russia", "India", "china", "South Africa", "Colombia"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria", "Bogotá"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
        "population": [200.4, 143.5, 1252, 1357, 52.98, 49.65]}


import pandas as pd


brics = pd.DataFrame(dictc)
print(brics)
