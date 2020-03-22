import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_excel(r"C:\Users\gowtham\Desktop\Staff_data.xlsx")
profile = ProfileReport(df, title='Pandas Profiling Report', html={'style':{'full_width':True}})
profile.to_file(r"C:\Users\gowtham\Desktop\test.html")
print(profile)