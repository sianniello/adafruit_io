from datetime import datetime
from random import gauss, uniform
from time import sleep
import Adafruit_IO as af


IO_USERNAME = "steno87"
IO_KEY = "2383dd6dc0c74d3aa3d689bbcbf7d63d"
SLOT_TIME = 1
WAIT_TIME = 60

if __name__ == '__main__':
    aio = af.Client(IO_KEY)

    while True:
        rnd_temp = gauss(19, 1)
        rnd_humi = gauss(50, 10)
        rnd_pres = gauss(100000, 5)

        try:
            print("Sending request...")

            aio.send('Temperature', rnd_temp)
            aio.send('Humidity', rnd_humi)
            aio.send('Pressure', rnd_pres)

            timestamp = datetime.now().isoformat(timespec='minutes')
            print("Data sent. Timestamp: ", timestamp)

        except:
            timestamp = datetime.now().isoformat(timespec='minutes')
            print("Connection error! Timestamp: ", timestamp)
            slot_time = uniform(0, 1)
            sleep(WAIT_TIME)
        sleep(WAIT_TIME)
