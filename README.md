# am_xmit_multi_carrier_fl2k
FL2K AM Multi Carrier Transmitter

gnuradio-companion and extended python script for creating radio data files of multiple audio streams
on different AM carrier frequencies for later transmission by an fl2k dongle.

The grc script has the base method for 6 carriers. Adding more graphically would be unweildly so another
python script has more signal processing blocks added for a total of 32 carriers.   The fl2k does not have
a whole lot of output signal power to begin with and I thought going beyond 32 would be pushing it too thin. 

Another script stop.sh monitors the size of the output and kills the process when it reaches a set limit,
currently a half hour at 8192k samples per second which is around 15GB.

Creating the 15GB data file takes a few hours depending on your cpu number crunching ability, and a scope and fft
is displayed during the process to ensure the output stays in limits of +/- 1, which is scaled to 127/-128 
for the fl2k. 

# AM_Modulator
A hierarchical block to simplify massive audio channel setup in GRC itself without tedious editing of the script.
Assign each AM_Modulator block a unique wav file source (name needs to be in "quotes.wav") and a carrier frequency. 
Example graph am_xmit_hier_fl2k.grc .

# Audio files
The grc script takes mono single channel 16000 sample per second audio clips. The youtube demo was created with
the archive.org 1939 Jack Benny show which came in mp3 format and may be converted to the appropriate wav with:

$ madplay -o wave:- Jackbenny-390129BennyVsAllenFight.mp3 | sox - -r 16000 Jackbenny-390129BennyVsAllenFight.wav

A couple of the mp3 out of that collection are actually 2 channel and need to be mixed down to play at the right speed - they
will be obvious twice the size of the rest:

$ madplay -o wave:- Jackbenny-390528AlexanderGrahamBell.mp3 | sox - -r 16000 Jackbenny-390528AlexanderGrahamBell.wav remix 1,2

# Theory
the 16k sample per second audio as float data is interpolated by 512 to 8192000 samples per second rf rate with gain
in an interpolating fir filter, a constant added and mixed with the carrier oscillator, then all the channels are
added together, scaled to not saturate the sdr sink and converted to char byte data format and scaled by 128 and
saved to an output file for transmission by the fl2k, which actually uses 8196720 for an error of 4720 which is ok.

Transmit the finished multiplex with

$ fl2k_file -s 8192000 am_xmit_fl2k.dat

A bit of rf gain (minicircuits zhl-32a for 25db), a good antenna (loop) and receiver complete the setup.

