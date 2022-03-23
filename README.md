Capture errored records that error with ‘pandas.errors.ParserError: Error tokenizing data. C error: Expected j fields in line j, saw k’

When reading a csv file using pandas, we may encounter error scenarios if column separator is present in the data values as well. Pandas will error in the lines of ‘pandas.errors.ParserError: Error tokenizing data. C error: Expected j fields in line j, saw k’. You will be able to load the files by using on_bad_lines='skip'. When you need to capture the errored records, following approach can be used.

1)	Read each line and find columns by splitting the text using separator value
2)	Use mmap to keep track of column count as well as the byte position of the line for faster access later.
3)	If the column count is not same as the most common column count present in the file then report back the corresponding row.

Call- 
Python3 Find_no_of_coumns_issue.py     file_name     separator 

Filename- is the directory/file name to be parsed for tokenize errors and to report back corresponding rows
Separator – column separator

