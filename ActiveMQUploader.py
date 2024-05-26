import requests

# Define the ActiveMQ server and queue details
activemq_host = 'https://sit-mq.istargv-au-aex.com:8162/api/message'
queue_name = 'destination=queue://AUSIEXOUT'


# Define the headers and authentication credentials
headers = {
    'Content-Type': 'application/xml'
}
auth = ('admin', 'adm1n')  # Replace with your actual username and password

file = open("ClientRequest.xml","r")
xml_message = ""
#Repeat for each message in the text file
for line in file:
    if line.find("</Message>") != -1:
        xml_message = xml_message+""+line
        # Send the XML message to the ActiveMQ queue using the REST API with authentication
        response = requests.post(f'{activemq_host}?{queue_name}', headers=headers, data=xml_message, auth=auth, verify=False)
        # Check the response
        if response.status_code == 200:
            print('XML message sent successfully.')
        else:
            print(f'Failed to send XML message. Status Code: {response.status_code}')
        xml_message = ""
    else:
        xml_message = xml_message+""+line


#It is good practice to close the file at the end to free up resources   
file.close()
