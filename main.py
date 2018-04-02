# Requires Python 2.7
from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor
import ssl

CUCM = 'cucm.yourdomain.com'
USERNAME = 'yourusername'
PASSWORD = 'yourpassword'

ssl._create_default_https_context = ssl._create_unverified_context
location = 'https://' + CUCM + ':8443/axl/'

tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/',
             'http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)

client = Client(WSDL,location=location,faults=False,plugins=[ImportDoctor(imp)],
                username=USERNAME,password=PASSWORD)
result = client.service.executeSQLQuery('select enum, name from typemodel')
phone_models = {}
        for row in result[1]['return']['row']:
            phone_models[row.enum] = row.name
print phone_models
