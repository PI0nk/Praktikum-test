import pandas as pd
import numpy as np

url = "B 1.3\B1.3(1).xlsx"

df = pd.read_excel(url)

for _ in range(2):

    cleaned_df = pd.DataFrame()
    goodcols = []

    for col in df:
        c = df[col]

        if c.count() != 0:
            goodcols.append(col)
            cleaned_df = df[goodcols]
    
    df = cleaned_df.T

df = df.replace(np.math.nan, ' ')


output = open("{0}.txt".format(url),"wt")

colcount = df.shape[1]
titlestr = "\\begin(table){0}\n".format(["c |" for _ in range(colcount)]).replace("'", "").replace(",","").replace(" |]","]")
endstr = "\\end(table)"

output.write(titlestr)
for row in df.T:
    contentstr = "\t {0}".format(df.T[row][0])
    for ele in df.T[row][1:]:
        contentstr = "{0} & {1}".format(contentstr,ele)
    contentstr = contentstr + "\\\\\n"
    output.write(contentstr) 
output.write(endstr)
output.close()