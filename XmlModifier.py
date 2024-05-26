import xml.etree.ElementTree as ET

def update_message_id_and_email(xml_content):
    ns = {'nri': 'http://www.nri.com/igv'}
    ET.register_namespace('', ns['nri'])
    
    root = ET.fromstring(xml_content)
    
    message_id_elem = root.find('.//nri:MessageId', ns)
    if message_id_elem is not None:
        original_message_id = message_id_elem.text
        new_message_id = original_message_id[:-2] + 'PR'
        message_id_elem.text = new_message_id
    
    additional_address_elem = root.find('.//nri:AdditionalAddress', ns)
    if additional_address_elem is not None:
        email_address_elem = additional_address_elem.find('.//nri:EmailAddress', ns)
        if email_address_elem is not None:
            is_primary_email_elem = email_address_elem.find('nri:IsPrimaryEmail', ns)
            if is_primary_email_elem is None:
                new_elem = ET.SubElement(email_address_elem, '{http://www.nri.com/igv}IsPrimaryEmail')
                new_elem.text = 'Y'

    return ET.tostring(root, encoding='utf-8', xml_declaration=True).decode('utf-8')

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        xml_data = file.read()
    
    xml_messages = xml_data.split('<?xml')[1:]
    xml_messages = ['<?xml' + message for message in xml_messages]
    
    updated_messages = []
    for xml_message in xml_messages:
        if xml_message.strip():
            updated_xml = update_message_id_and_email(xml_message)
            updated_messages.append(updated_xml)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        
        file.write('\n'.join(updated_messages))

if __name__ == "__main__":
    input_file_path = 'clientBOB.txt'
    output_file_path = 'outputfile.xml'

    process_file(input_file_path, output_file_path)
    print(f"Processed XML messages and saved to {output_file_path}")
