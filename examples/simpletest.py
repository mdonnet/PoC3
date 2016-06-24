import Adafruit_DHT
import time
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
while True:
    if humidity is not None and temperature is not None:
        time.sleep(1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print(time.strftime('%H:%M:%S')+'@'+'{0:0.1f}@{1:0.1f}'.format(temperature,humidity))  
    else:
        print(time.strftime('%H:%M:%S'),'ERROR LECTURA')
