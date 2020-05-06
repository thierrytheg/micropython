from adafruit_circuitplayground import cp
import time
import random
import board
import audiocore
import array
"""
#fft
https://github.com/Tschucker/CircuitPython_FFT/blob/master/examples/fft_simpletest.py
"""

"""
#play from array
#PLAY FILE FROM ARRAY
FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!
 
# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)        
    print((sine_wave[i],))
cp.stop_tone()
cp._speaker_enable.value = True
audio = cp._audio_out(board.SPEAKER)
sine_wave_sample = audiocore.RawSample(sine_wave)
audio.play(sine_wave_sample,loop=1)
"""
"""
#play file from object
cp.stop_tone()
cp._speaker_enable.value = True
with cp._audio_out(board.SPEAKER) as audio:
    wavefile = audiocore.WaveFile(open('left.wav', "rb"))
    audio.play(wavefile)
    while audio.playing:
        pass
cp._speaker_enable.value = False
"""
"""
#plot acceleromator
while True:
    x, y, z = cp.acceleration
    print(x,y,z)
    print((x, y, z),)
    time.sleep(1)
"""
"""
#Pad A touched
cp.adjust_touch_threshold(200)
while True:
    if cp.touch_A1:
        print('Touched pad A1')
"""
"""
#detect whether button A or B has been pressed
while True:
    if cp.button_a:
        print("Button A pressed!")
    if cp.button_b:
        print("Button B pressed!")
"""
"""
#detect taps
cp.detect_taps = 1
while True:
  if cp.tapped:
    print("Single tap detected!")
"""
"""
#detect light
while True:
    lum=cp.light
    print(lum)
    print((lum,))
    time.sleep(1)
"""
"""
#turn on LED
for n in range(0,10,1):
    cp.pixels.brightness = random.random()
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    cp.pixels[n] = (r, g, b)
    time.sleep(1)
"""
"""
#play wavfile
cp.play_file("jemaine-ohno.wav")
"""
"""
#play tone for hal second
cp.play_tone(100, 0.5)
"""
"""
#turn on/off Red light
while True:
    cp.red_led = True
    time.sleep(0.5)
    cp.red_led = False
    time.sleep(0.5)
"""
"""
#detect shake
while True:
    if cp.shake(shake_threshold=10):
        print("Shake detected!")
"""
"""
#produce a tone pressing buttons
while True:
    if cp.button_a:
        cp.start_tone(500)
    elif cp.button_b:
        cp.start_tone(294)
    else:
        cp.stop_tone()
"""
"""
#switch
while True:
    print("Slide switch:", cp.switch)
    time.sleep(0.1)
"""
"""
#temperature
while True:
    temperature_c = round(cp.temperature,1)
    temperature_f = round(temperature_c * 1.8 + 32,1)
    print("Temperature celsius:", temperature_c)
    print("Temperature fahrenheit:", temperature_f)
    time.sleep(1)
"""
"""
#play tone when pad touched
while True:
    if cp.touch_A1:
        print("Touched pad A1")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_A2:
        print("Touched pad A2")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_A3:
        print("Touched pad A3")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_A4:
        print("Touched pad A4")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_A5:
        print("Touched pad A5")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_A6:
        print("Touched pad A6")
        cp.play_tone(random.randint(0,1000), 0.5)
    if cp.touch_TX:
        print("Touched pad TX")
        cp.play_tone(random.randint(0,1000), 0.5)
    else:
        cp.stop_tone()
"""
"""
#which button has been pressed
while True:
    print(cp.were_pressed)
    time.sleep(1)
"""
"""
#turn LED on when switched to left
while True:
    if not cp.switch:
        # If the switch is to the right, it returns False!
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        continue
    R = 0
    G = 0
    B = 0
    x, y, z = cp.acceleration
    print((x, y, z))
    cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))
"""
"""
#IR receiver
# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
try:
    pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
except AttributeError:
    raise NotImplementedError(
        "This example does not work with Circuit Playground Bluefruti!"
    )
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()
while True:
    cp.red_led = True
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted
        continue
    print("Infrared code received: ", received_code)
    if received_code == [66, 84, 78, 65]:
        print("Button A signal")
        cp.pixels.fill((100, 0, 155))
    if received_code == [66, 84, 78, 64]:
        print("Button B Signal")
        cp.pixels.fill((210, 45, 0))
"""
"""
#IR Transmitter
# Create a 'pulseio' output, to send infrared signals from the IR transmitter
try:
    pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
except AttributeError:
    raise NotImplementedError(
        "This example does not work with Circuit Playground Bluefruit!"
    )
pulseout = pulseio.PulseOut(pwm)  # pylint: disable=no-member
# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(
    header=[9500, 4500], one=[550, 550], zero=[550, 1700], trail=0
)
while True:
    if cp.button_a:
        print("Button A pressed! \n")
        cp.red_led = True
        encoder.transmit(pulseout, [66, 84, 78, 65])
        cp.red_led = False
        # wait so the receiver can get the full message
        time.sleep(0.2)
    if cp.button_b:
        print("Button B pressed! \n")
        cp.red_led = True
        encoder.transmit(pulseout, [66, 84, 78, 64])
        cp.red_led = False
        time.sleep(0.2)
"""
"""
#Sound Meter
import array
import math
import board
import audiobusio
from adafruit_circuitplayground import cp
def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))
def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / (input_max - input_min)
    return output_min + math.pow(normalized_input_value, 0.630957) * (
        output_max - output_min
    )
def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return math.sqrt(
        sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
        / len(values)
    )
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16
)
samples = array.array("H", [0] * 160)
mic.record(samples, len(samples))
input_floor = normalized_rms(samples) + 10
# Lower number means more sensitive - more LEDs will light up with less sound.
sensitivity = 50
input_ceiling = input_floor + sensitivity
peak = 0
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print((magnitude,))
    c = log_scale(
        constrain(magnitude, input_floor, input_ceiling),
        input_floor,
        input_ceiling,
        0,
        10,
    )
    cp.pixels.fill((0, 0, 0))
    for i in range(10):
        if i < c:
            cp.pixels[i] = (i * (255 // 10), 50, 0)
        if c >= peak:
            peak = min(c, 10 - 1)
        elif peak > 0:
            peak = peak - 1
        if peak > 0:
            cp.pixels[int(peak)] = (80, 0, 255)
    cp.pixels.show()
    time.sleep(1)
"""
"""
#convert temperature to led logts
cp.pixels.auto_write = False
cp.pixels.brightness = 0.3
# Set these based on your ambient temperature in Celsius for best results!
minimum_temp = 20
maximum_temp = 30
def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)
while True:
    peak = scale_range(cp.temperature)
    print(cp.temperature)
    print(int(peak))
    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(1)
"""
