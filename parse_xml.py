import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
name = tree.findtext("name").strip()
last_name = tree.findtext("last_name").strip()
print(f"Hi {name} {last_name}")
