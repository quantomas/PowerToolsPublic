
### clean run
# tested on Python 3.6.3 64 bit

### tests

# https://www.pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
# https://stackoverflow.com/questions/14472650/python-3-encode-decode-vs-bytes-str
# https://www.pythonsheets.com/notes/python-unicode.html

tt = "\u00fcabc"
type(tt)

# str(tt, 'utf-8')

tt.encode('utf-8').decode('utf-8')

uu = tt.encode('utf-8')

type(uu)


encoded3 = str.encode(tt, 'utf-8')

print(encoded3)

type(encoded3)


vv = uu.decode('utf-8')

type(vv)

