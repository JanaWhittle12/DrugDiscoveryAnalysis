import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import seaborn as sb



# read protein confirmation data
filePath = "C:/MCP Project/properties"
# filePath = "/Users/jwhittle/MCP/MCP_Analysis"
protein = "adrb2"
proteinFile = filePath + "/" + protein + "_properties_cleaned.csv"
bindFile = filePath + "/" + protein + "_binding.csv"
# print(proteinFile, "  ", bindFile)

confData = pd.read_csv(proteinFile, index_col=0)
# print(confData.describe())
# print(confData.corr())
# confData = confData.copy()
confData['intercept'] = 1.0


bindData = pd.read_csv(bindFile, index_col=0)
# print(bindData.describe())
y = bindData[["ActiveBinding"]].copy()


lrModel = smf.Logit(y.astype(float), confData.astype(float))
result = lrModel.fit(method="powell")
print(result.summary())