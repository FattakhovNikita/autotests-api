import xml.etree.ElementTree as ET

xml_data = """
<user>    
    <id>1</id>
    <first_name>Pablo</first_name>
    <last_name>Escobar</last_name>
    <email>pablo.escobar.com</email>
</user>
    """

root = ET.fromstring(xml_data)

print("User ID:", root.find('id').text)
print("User Name:", root.find('first_name').text, root.find('last_name').text)
print("User Email:", root.find('email').text)