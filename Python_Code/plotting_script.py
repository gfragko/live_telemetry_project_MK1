import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

SERIAL_PORT = 'COM3'
BAUD_RATE = 115200

x_vals = []
sensorValue1_data = []
sensorValue2_data = []

def read_data():
    line = ser.readline().decode('utf-8').strip()
    sensorValues = line.split(', ')
    
    x_vals.append(float(sensorValues[0]))
    sensorValue1_data.append(int(sensorValues[1]))
    sensorValue2_data.append(int(sensorValues[2]))
    
    print(f'Time: {sensorValues[0]}, Sensor 1: {sensorValues[1]}, Sensor 2: {sensorValues[2]}')

def update_plot(frame):
    read_data()
    plt.cla()
    plt.plot(x_vals, sensorValue1_data, label = 'Sensor1')
    plt.plot(x_vals, sensorValue2_data, label = 'Sensor2')
    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.legend()
    
def on_close(event):
    with open('arduino_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Sensor1', 'Sensor2'])
        for x, s1 , s2 in zip(x_vals, sensorValue1_data, sensorValue2_data):
            writer.writerow([x, s1, s2]) 
            
            
fig, ax = plt.subplots()
fig.canvas.mpl_connect('close_event', on_close)

ani = animation.FuncAnimation(fig, update_plot, interval=10 )
plt.show()