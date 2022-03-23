import mmap
import sys,subprocess,re
import pandas as pd
parm1=sys.argv[1]
sep=sys.argv[2]

a=subprocess.check_output("wc -l "+str(parm1),shell=True)
output=re.split('=|\n|"| |,',str(a))
total_line_count=int(output[0][2:])
count=0
col_count_list=[]
col_count_list_child=[]
if 1==1:
    with open(str(parm1), "r+b") as f:
    # memory-map the file, size 0 means whole file
       mm = mmap.mmap(f.fileno(), 0)
       start=0
       for i in range(total_line_count):
           count=count+1
           a=mm.readline()
           end=start+len(a)
           b=(str(a)[2:-3])
           c=b.split(sep) 
           col_count_list_child.append(start)
           col_count_list_child.append(end)
           col_count_list_child.append(len(c))
           col_count_list.append(col_count_list_child)
           col_count_list_child=[]
           
           start=end

    df = pd.DataFrame (col_count_list, columns = ['start','end','column_count'])
    print(df.head())
    col_count_list=[]
    common_col_count=df['column_count'].value_counts().idxmax()
    for i, row in df[df['column_count']!=common_col_count].iterrows():
        print(mm[row[0]:row[1]])
       
       
