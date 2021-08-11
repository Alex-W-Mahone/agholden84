import serial
import matplotlib.pyplot as plt

plt.ion()  # ???? initial a figure
i = 0
arduinoSerialData = serial.Serial('com4', 9600)

arduinoSerialData.close()
arduinoSerialData.open()
data = float(arduinoSerialData.readline().decode().replace('\r', '').replace('\n', ''))  # first data will not be plotted

try:
    while True:
        data = float(arduinoSerialData.readline().decode().replace('\r', '').replace('\n', ''))
        i += 1
        plt.title('serial reader: ' + str(data), loc='left')
        plt.plot(i, data, '.g')
        plt.show(block=False)
        plt.pause(0.001)

except KeyboardInterrupt:
    arduinoSerialData.close()
    print("serial connection closed")
