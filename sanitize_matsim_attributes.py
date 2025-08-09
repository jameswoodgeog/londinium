import xml.etree.ElementTree as ET
import sys
import os

# Usage: python sanitize_matsim_attributes.py <input.xml> <output.xml>

def sanitize_keys(elem):
    # Sanitize attribute keys in-place
    for key in list(elem.attrib.keys()):
        if ':' in key:
            new_key = key.replace(':', '_')
            elem.attrib[new_key] = elem.attrib.pop(key)
    for child in elem:
        sanitize_keys(child)

def main(input_path, output_path):
    tree = ET.parse(input_path)
    root = tree.getroot()
    sanitize_keys(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sanitize_matsim_attributes.py <input.xml> <output.xml>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
