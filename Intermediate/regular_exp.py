import re
mystr=''' Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 703 243 9787
Fax: +1 703 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii '''

## findall gives specfic matched string object
## search returns match object
## split gives list of previous  and next  sentences of given words
'''
pat=re.compile(r"fass")   # r - raw string prints /n
matches=pat.finditer(mystr)
for match in matches:
    print(match)
'''
## span gives index
'''
findall, search, split, sub, finditer
patt = re.compile(r'fass')
patt = re.compile(r'.adm')
patt = re.compile(r'^Tata')
patt = re.compile(r'iin$')
patt = re.compile(r'ai{2}')
patt = re.compile(r'(ai){1}')
patt = re.compile(r'ai{1}|Fax')


Special Sequences
patt = re.compile(r'Fax\b')
patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')
'''

patt = re.compile(r'\d{5}-\d{4}')

## + is special char so req \ before it
pat=re.compile(r"\+1 \d{3} \d{3} \d{4}")   # . is metachar -- any char
matches=pat.finditer(mystr)
for match in matches:
    print(match)

## TASK 


