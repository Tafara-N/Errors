"""
Convert a CSV file to JSON error:

The default or expected encoding in CSV is UTF-8.

So when we get an error like:

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd2 in position 7431: invalid continuation byte

It means that the file is not encoded in UTF-8 which is the expected encoding by the csv module.

To resolve this issue:

OPTION 1:
========
We can specify the correct correct encoding when reading the csv file.
If unsure about the encoding, we can try using the ISO-8859-1 (latin1) which is a
common encoding for extended ASCII text.

# Opening and reading the CSV file, we can try 'WINDOWS-1252' as well if this fails
with open("filename.csv", mode="r", encoding="ISO-8859-1" as file:
    ...
    ...
    ...

# Opening and writing to the JSON file
with open("file.json", mode='w', encoding='utf-8') as file:
    ...
    ...

OPTION 2:
========
Using 'iconv'

If unsure of the file encoding type, in the terminal, run:

file 'filename.csv'

Example Output:
----------------
file netflix_originals.csv                                               
netflix_originals.csv: CSV Non-ISO extended-ASCII text

Given that the file command indicates the CSV file is "CSV Non-ISO extended-ASCII text," 
it suggests that the file might be using an encoding other than 'UTF-8' or 'ISO-8859-1'. 

We can try converting the file using iconv with a more general encoding like 'WINDOWS-1252'
which is commonly used for extended ASCII text.

Convert the file to UTF-8:
===================

iconv -f WINDOWS-1252 -t UTF-8 netflix_originals.csv -o netflix_originals_utf8.csv

If 'WINDOWS-1252' fails, we can try 'ISO-8859-1'


Check the file encoding after:
======================
file netflix_originals_utf8.csv 
netflix_originals_utf8.csv: CSV Unicode text, UTF-8 text


Now we can be able to convert the json file to csv and vice versa

"""
