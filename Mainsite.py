from flask import Flask, render_template, request, redirect, url_for
from pyduino import *
import time

app = Flask(__name__)

# initialize connection to Arduino
# if your arduino was running on a serial port other than '/dev/ttyACM0/'
# declare: a = Arduino(serial_port='/dev/ttyXXXX')
a = Arduino()
time.sleep(3)

# declare the pins we're using
LED_PIN1 = 3
LED_PIN2 = 10
LED_PIN3 = 6
ANALOG_PIN = 0

# initialize the digital pin as output
a.set_pin_mode(LED_PIN1, 'O')
a.set_pin_mode(LED_PIN2, 'O')

b = 0

print('Arduino initialized')

@app.route('/')
def home():
    return 'Homepage'

# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    # variables for template page (templates/index.html)
    author = "Shadow"


    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        if request.form['submit'] == 'Ctl On':
            print('Control ON')

            a.digital_write(LED_PIN3, 1)

        elif request.form['submit'] == 'Ctl Off':
            print('Control Off')

            a.digital_write(LED_PIN3, 0)

        # if we press the turn on button
        elif request.form['submit'] == 'LED On':
            print('TURN ON')

            # turn on LED on arduino
            a.digital_write(LED_PIN1, 1)

        # if we press the turn off button
        elif request.form['submit'] == 'LED Off':
            print('TURN OFF')

            # turn off LED on arduino
            a.digital_write(LED_PIN1, 0)

        elif request.form['submit'] == 'Sense Read':
            print('Measurement =', int(measure))

            # turn on LED on arduino
            a.analog_write(LED_PIN3, measure)

        elif request.form['submit'] == 'Power Max':
            print('Max!')

            # turn on LED on arduino
            a.analog_write(LED_PIN2, 255)

        elif request.form['submit'] == 'Power Half':
            print('Halfway.')

            # turn off LED on arduino
            a.analog_write(LED_PIN2, 127)

        elif request.form['submit'] == 'Power Off':
            print('Off...')

            # turn off LED on arduino
            a.analog_write(LED_PIN2, 0)

        else:
            pass

    # read in analog value from photoresistor
    readval = a.analog_read(ANALOG_PIN)
    print('Ready...')

    # the default page to display will be our template with our template variables
    return render_template('connect.html', author=author, value=100 * (readval / 1023.))

if __name__ == "__main__":
    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')