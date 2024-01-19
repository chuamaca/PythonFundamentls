#Uso de Librerias
from datetime import date, datetime, timedelta
hoy= date.today()
hoyhora=datetime.now()


print(hoy)
print(hoyhora.strftime('%d-%m-%Y %H:%m:%s'))

