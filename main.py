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
phone_models = []
for row in result[1]['return']['row']:
    phone_model_d = {}
    phone_model_d["id"] = row.enum
    phone_model_d["model"] = row.name
    phone_models.append(phone_model_d)
print phone_models
