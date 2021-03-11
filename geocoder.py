from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('apiKey').geocode(endereco).coordinates)