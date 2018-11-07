import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import seaborn as sb



# read protein confirmation data
filePath = "C:/MCP Project/adora2a/properties"
# filePath = "/Users/jwhittle/MCP/MCP_Analysis"
protein = "adrb2"
proteinFile = filePath + "/" + protein + "_properties_cleaned.csv"
print(proteinFile)

confData = pd.read_csv(proteinFile)
confData/describe()

confData.corr()

lrModel = smf.Logit(y, X).fit()
lrModel.summary