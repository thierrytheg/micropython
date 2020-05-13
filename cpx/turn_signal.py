import neopixel
import board
import time
from adafruit_circuitplayground import cp
import audiobusio
import math
import array

def blank(LED):
    LED.fill((0,0,0))
    LED.show()

def full(LED):
    LED.fill((0,255,255))
    LED.show()

A2 = neopixel.NeoPixel(
    board.A3, 30, brightness=0.1, auto_write=True)

A4 = neopixel.NeoPixel(
    board.A4, 30, brightness=0.1, auto_write=True)


lapse=0.25

cp.detect_taps = 1


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
sensitivity = 500
input_ceiling = input_floor + sensitivity

peak = 0

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    
    if cp.button_a or magnitude>130:
        for n in range(5):
            full(A4)
            time.sleep(lapse)
            blank(A4)
            time.sleep(lapse)

    if cp.button_b or 100<magnitude<125:
        for n in range(5):
            full(A2)
            time.sleep(lapse)
            blank(A2)
            time.sleep(lapse)

    if cp.tapped:
        curr_folder="numbers\\"
        temp=str(int((round(cp.temperature,0))))
        cp.play_file(curr_folder+temp+ ".wav")

    else:
        pass

        

"""
import time
import array
import math
import board
import digitalio
from audioio import RawSample
from audioio import AudioOut
import audiobusio
import adafruit_binascii
from adafruit_circuitplayground import cp

def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return math.sqrt(
        sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
        / len(values)
    )

#FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 44100  # 8000 samples/second, recommended!

# Generate one period of sine wav.
length = 100

sine_wave = array.array("H", [0] * length)
direction=array.array("H", [0] * length)
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=SAMPLERATE, bit_depth=16)
x=0
while True:
    x=x+1
    print("recoding now")
    time.sleep(1)
    for i in range(length):
        sine_wave[i]=mic.record(sine_wave, length)
        #mag=normalized_rms(sine_wave)
        #direction[i]=int(mag)


    #print(sine_wave[n])
    print(x,sine_wave[5]/sine_wave[0])
    if 0.98<(sine_wave[5]/sine_wave[0])<1:
        cp.pixels[0]=(0,255,0)
        time.sleep(1)
        cp.pixels[0]=(0,0,0)
        print("LEFT")
    if (sine_wave[5]/sine_wave[0])>1.01:
        cp.pixels[9]=(0,255,0)
        time.sleep(1)
        cp.pixels[9]=(0,0,0)
        print("RIGHT")
    else:
        print("NO DIRECTION")

#    x=adafruit_binascii.hexlify(sine_wave)
#    print(sine_wave)
#    print(x)

#while True:
#    if mag>value:
#        do something
#    else:
#        break
#print(

#print(sine_wave[:5])
#sine_wave = array.array("H", [50])
#print(sine_wave)
#x=adafruit_binascii.hexlify(sine_wave)

#print(x.startswith('32'))


sine_wave=array.array('H', [10000,15000,20000,25000,30000])

# Enable the speaker

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

audio = AudioOut(board.SPEAKER)
sine_wave_sample = RawSample(sine_wave)

# A single sine wave sample is hundredths of a second long. If you set loop=False, it will play
# a single instance of the sample (a quick burst of sound) and then silence for the rest of the
# duration of the time.sleep(). If loop=True, it will play the single instance of the sample
# continuously for the duration of the time.sleep().
audio.play(sine_wave_sample, loop=True)  # Play the single sine_wave sample continuously...
time.sleep(1)  # for the duration of the sleep (in seconds)
audio.stop()  # and then stop.
"""
