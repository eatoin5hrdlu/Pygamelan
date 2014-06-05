#!C:/Python27/python
'''
    File: wiisound
    Author: Peter Reintjes, Jeffrey Wubbenhorst
    Contents:  basic example showing how to play midi sounds using pygame.
    Requires:  this example was run in Python 2.7 with pygame 1.9.2 installed.
    Sources:  Jeff Kinne's example
  
	Get Cygwin for windows, install open-ssh, emacs,
	Windows: pybluez  "e.g. import bluetooth"
	pygame
	pygame_wiimote (separate)


'''
import sys, re

import bluetooth
#import cwiid

import pygame
import pygame.midi
from time import sleep

#
# Specify Wii Device
#

target_name = "Nintendo RVL-CNT-01" #We set our Bluetooth device name
target_address = "00:1C:BE:29:75:7F" #We set out Bluetooth device address


#
# Initialize Midi
#
def initMidiByName(pattern) :
	pygame.init()
	pygame.midi.init()
	for i in range(pygame.midi.get_count()) :
	        info = pygame.midi.get_device_info(i)
	        if ( re.search(pattern, info[1]) and info[3] == 1 ) :
			print "Pattern [" + pattern + "] matches device "+str(i)
			return pygame.midi.Output(i, 0)
	print "Couldn't find anything to match [" + pattern + "]"
	print "Choices are:"
	for i in range(pygame.midi.get_count()) :
	        info = pygame.midi.get_device_info(i)
	        if (info[3] == 1) :
	   		print "   "  + str(i) + "     " + info[1]

#
# Define the Midi sound example
#

def midiExample(midi_out):
    # Things to consider when using pygame.midi:
    #
    # 1) Initialize the midi module with a to pygame.midi.init().
    # 2) Create a midi.Output instance for the desired output device port.
    # 3) Select instruments with set_instrument() method calls.
    # 4) Play notes with note_on() and note_off() method calls.
    # 5) Call pygame.midi.Quit() when finished. Though the midi module tries
    #    to ensure that midi is properly shut down, it is best to do it
    #    explicitly. A try/finally statement is the safest way to do this.
    #
    instrument = GRAND_PIANO  #This sets the output channel

    try:
        midi_out.set_instrument(instrument)

        midi_out.note_on(72,127) # 74 is middle C, 127 is "how loud" - max is 127
        sleep(.5)
        midi_out.note_off(72,127)
        sleep(.5)

        midi_out.note_on(76,127) # E
        sleep(.5)
        midi_out.note_off(76,127)
        sleep(.5)
    finally:
        pass

def initWii(name, address) :
	try:
		nearby_devices = bluetooth.discover_devices()
	except IOError:
		return None

	for bdaddr in nearby_devices:
	    if name == bluetooth.lookup_name( bdaddr ):
	        target_address = bdaddr
	        break

	if target_address is not None:
	    print "found target bluetooth device with address ", target_address
	else:
	    print "could not find target bluetooth device nearby"
	    return None

	wiimote = cwiid.Wiimote()
	wiimote.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
	wiimote.led = 1
	return wiimote



