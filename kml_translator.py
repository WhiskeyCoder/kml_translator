from xml.etree import ElementTree as ET
from deep_translator import GoogleTranslator
import os

def translate_kml(input_file_path, output_file_path):
    # Initialize the translator, can change output language by using language code and changing en
    translator = GoogleTranslator(source='auto', target='en')

    # Parse the KML file
    tree = ET.parse(input_file_path)
    root = tree.getroot()

    # Define a namespace dictionary for the KML namespace
    namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Find all elements that potentially contain text
    for element in root.findall('.//kml:name', namespaces) + root.findall('.//kml:description', namespaces):
        if element.text:
            try:
                # Translate the text and replace it in the element
                translated_text = translator.translate(element.text)
                element.text = translated_text
            except Exception as e:
                print(f"Error translating text: {e}")

    # Write the modified tree to a new file
    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

# Example usage
input_kml_file = 'File_To_Be_Translated.kml'  # Replace with your KML file path
output_kml_file = 'output_file.kml'  # Output file path
translate_kml(input_kml_file, output_kml_file)
