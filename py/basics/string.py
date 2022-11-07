
## https://www.w3schools.com/python/ref_string_split.asp

# string.split(separator, maxsplit)
# separator 	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator


mystring = '1  2    3     4'

mystring = '___  deutsche_telekom 13,965  (x100)'

mystring = '___ deutsche_börse 137,2 (x10)'

mystring.split(' ')

# >>>
' '.join(mystring.split())

mystring.split()

