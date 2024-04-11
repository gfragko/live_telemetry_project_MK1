import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

def animate(i, dataList, ser):
    ser.write(b'g')                                     # Transmit the char 'g' to receive the Arduino data point
    arduinoData_string = ser.readline().decode('ascii') # Decode receive Arduino data as a formatted string

    try:
        arduinoData_float = float(arduinoData_string)   # Converting to float
        dataList.append(arduinoData_float)              # Adding to the list of data values we will plot

    except:
        pass

    dataList = dataList[-50:]                           # Setting the animation plot 'window' 
    ax.clear()                                          # Clear last data frame
    ax.plot(dataList)                                   # Plot new data frame
    
    ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
    ax.set_title("Arduino Data")                        # Set title of figure
    ax.set_ylabel("Value")                              # Set title of y axis 


dataList = []  
fig = plt.figure()                                      # Creating matplotlib plotting window
ax = fig.add_subplot(111)                               # Add subplot to main fig window
ser = serial.Serial("COM3", 9600)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(2)                                           # Time delay for Arduino Serial initialization 

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, ser), interval=100) 
plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed
ser.close()                                             # Close Serial connection when plot is closed