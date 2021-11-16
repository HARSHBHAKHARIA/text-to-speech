import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["ganesh"])
data = trends.interest_by_region()
data = data.sort_values(by="ganesh", ascending=False)
data = data.head(10)
#print(data)
data.reset_index().plot(x="geoName", y="ganesh", 
                        figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
