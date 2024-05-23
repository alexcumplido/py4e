# XLM:  eXtensible Markup Language
# Parsing XML
import xml.etree.ElementTree as ET
data = '''
<person> 
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

xsd_schema = '''
  <xs:complexType name="person">
    <xs:sequence>
      <xs:element name="lastname" type="xs:string"/>
      <xs:element name="age" type="xs:integer"/>
      <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
  </xs:complexType>

'''
xsd_person = '''
  <person>
    <name>Chuck</name>
    <age>32</age>
    <dateborn>2001-04-17</dateborn>
  </person>
'''

tree = ET.fromstring(data)
print(tree)
print('Name:', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))

# Looping through nodes

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
    
for item in lst:
    print(f"Name: {item.find('name').text}")
    print(f"If: {item.find('id').text}")
    print(f"Attribute: {item.get('x')}")

# JavaScript Object Notation (JSON)
# Parsing JSON

import json
json_data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
info = json.loads(json_data)
print(f"User count: {len(info)}")

for item in info:
    print(f"Name: {item['name']}")
    print(f"Id: {item['id']}")
    print(f"Attribute: {item['x']}")