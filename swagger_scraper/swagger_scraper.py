# def clean_str(s: str) -> str:
#     import re

#     return re.sub(r'\W+', '', s)

# from bs4 import BeautifulSoup
from kcu import request


soup = BeautifulSoup(
    request.request(
        'https://bittrex.github.io/api/v3'
    ).content,
    'lxml'
)

operations = soup.find_all('div', {'class':'operation panel'})
print(len(operations))

for operation in operations:
    try:
        operation_name = clean_str(operation.find('span', {'class':'operation-name'}).find('span', {'class':'operation-name'}).text)
        operation_path = operation.find('span', {'class':'operation-path'}).text.strip()
        operation_description = operation.find('section', {'class':'swagger-operation-description'}).find('p').text.strip()

        prop_groups = operation.find_all('div', {'class':'prop-row prop-group'})

        for prop_group in prop_groups:
            prop_name = clean_str(operation.find('div', {'class':'prop-title'}).text)
            prop_type = clean_str(operation.find('span', {'class':'json-property-type'}).text)


        import json

        print(
            json.dumps(
                {
                    'name':operation_name,
                    'path':operation_path,
                    'desc':operation_description
                },
                indent=4
            )
        )
    except:
        pass