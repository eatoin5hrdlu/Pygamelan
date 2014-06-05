
import wiisound
from wiisound import initWii
from wiisound import initMidiByName
import pygame
import pygame.midi
from time import sleep

#
# Initialize argparse
#
import argparse

parser = argparse.ArgumentParser(description='Demonstrate Python MIDI.')
parser.add_argument('device', help='MIDI output device name (or pattern). ')
parser.add_argument('-n', '--n', type=int, help='number of times to repeat')
args = parser.parse_args()

print "device " + args.device

midi_out = initMidiByName(args.device)

GRAND_PIANO = 1
midi_out.set_instrument(GRAND_PIANO)


wm = initWii("Nintendo RVL-CNT-01","00:1C:BE:29:75:7F")

# Test case (no bluetooth)
if (wm == None) :
	print "Working with no Wii"
        midi_out.note_on(72,127) # 74 is middle C, 127 is "how loud" - max is 127
        sleep(2.5)
        midi_out.note_off(72,127)
        sleep(.5)
	del midi_out
	pygame.midi.quit()
	exit()


s = wm.state['buttons']  # We initialize variable s (for state) to the buttons.

# Wii Input to Music Loop

while True:    
    if (wm.state != 0): #If a button is pushed, output a MIDI note
        midi_out.note_on(72,127) # 74 is middle C, 127 is "how loud" - max is 127
        sleep(.5)
        midi_out.note_off(72,127)
        sleep(.5)
    else:
        print "Not buttons have been pressed!"           


# Cleanup

del midi_out
pygame.midi.quit()

