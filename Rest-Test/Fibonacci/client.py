from zeep import Client

client = Client('http://localhost:7859/?wsdl')
result = client.service.Fibonnaci(10)
print(result)