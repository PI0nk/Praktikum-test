import pandas as pd
import glob
import os
import numpy as np

filepaths = ['..\Widerstand','..\XRD']

def cleanString(string):
    clean = []
    for s in string:
        if s == '':
            continue
        else:
            clean.append(s.split('\n')[0])
    return clean

def returnArray(ftype,data,cols,rows):
    if ftype == 'uxd':
        delim = ' '
    else:
        delim = '\t'
        
    array = np.zeros((rows,cols))
    for i,line in enumerate(content):
        data = cleanString(line.split(delim))
        for j,ele in enumerate(data):
            array[i,j] = float(ele)
    return array

for filepath in filepaths:
    for name in os.listdir(filepath):
        if name.endswith('.xlsx') or name.endswith('.txt'):
            continue
        
        if '.UXD' in name:
            ftype = 'uxd'
        else:
            ftype = 'all'
    
        with open(filepath + '\\' + name,'r') as f:
            content = f.readlines()
            
            header = []
            columns = ''

            cols = 0
            rows = 0
            
            for i in range(0,len(content)):
                line = content[i]
                if ftype == 'uxd':
                    if line[0] in [';','_']:
                        header.append(line)
                    else:
                        content = content[i:]
                        
                        cols = len(cleanString(line.split(' ')))
                        rows = len(content)
                        
                        columns = ['2 theta','counts']

                        break
                if ftype == 'all':
                    if line[0] in ['#']:
                        header.append(line)
                    else:
                        content = content[i:]
                        
                        cols = len(cleanString(line.split('\t')))
                        rows = len(content)
                        
                        columns = cleanString(header[3].split('\t'))

                        break
            
            df = pd.DataFrame(returnArray(ftype,content,cols,rows),columns=columns)
            df.to_excel(filepath + '\\' + name.split('.')[0] + '.xlsx',index=False)
            
            f2 = open(filepath + '\\' + name.split('.')[0] + '.txt','w')
            for line in header:
                f2.write(line)


            
            
