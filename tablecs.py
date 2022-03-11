import pandas as pd
import collections

from collections import Counter

ventasdf = pd.read_csv("SalesJan2009.xls")
#print(ventasdf)
cp = Counter(ventasdf["Country"])
print(cp.most_common(3))
cv = Counter(ventasdf["Payment_Type"])
print(cv.most_common(3))
