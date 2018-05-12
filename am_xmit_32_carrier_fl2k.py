#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Am Xmit Multi Carrier Fl2K
# Generated: Sat May 12 12:42:29 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class am_xmit_multi_carrier_fl2k(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Am Xmit Multi Carrier Fl2K")
        _icon_path = "/usr/local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.rf_sample_rate = rf_sample_rate = 8192e3
        self.fir_interp = fir_interp = 512
        self.fgain = fgain = 128
        self.af_sample_rate = af_sample_rate = 16e3

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=rf_sample_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=rf_sample_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_5 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_4 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_3 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_5 = blocks.wavfile_source("Jackbenny-390101Goodbye1938Hello1939.wav", True)
        self.blocks_wavfile_source_4 = blocks.wavfile_source("Jackbenny-390115JacksScreenGuildTheatrePerformance.wav", True)
        self.blocks_wavfile_source_3 = blocks.wavfile_source("Jackbenny-390122EncyclopediaBritannica.wav", True)
        self.blocks_wavfile_source_2 = blocks.wavfile_source("Jackbenny-390129BennyVsAllenFight.wav", True)
        self.blocks_wavfile_source_1 = blocks.wavfile_source("Jackbenny-390129JackChallengesFredToFight.wav", True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("Jackbenny-390205JackChallengesFredAllenToABoxingMatch.wav", True)
        self.blocks_multiply_xx_5 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_4 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_6 = blocks.multiply_const_vff((.045, ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 128)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "am_xmit_fl2k.dat", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_5 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_4 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_3 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_2 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_5 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 590.006e3, 1, 0)
        self.analog_sig_source_x_4 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 570.005e3, 1, 0)
        self.analog_sig_source_x_3 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 560.004e3, 1, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 550.003e3, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 540.002e3, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 530.001e3, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_multiply_xx_3, 1))    
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_multiply_xx_4, 1))    
        self.connect((self.analog_sig_source_x_5, 0), (self.blocks_multiply_xx_5, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_add_const_vxx_2, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_add_const_vxx_3, 0), (self.blocks_multiply_xx_3, 0))    
        self.connect((self.blocks_add_const_vxx_4, 0), (self.blocks_multiply_xx_4, 0))    
        self.connect((self.blocks_add_const_vxx_5, 0), (self.blocks_multiply_xx_5, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_6, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_xx_3, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.blocks_multiply_xx_4, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.blocks_multiply_xx_5, 0), (self.blocks_add_xx_0, 5))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_wavfile_source_1, 0), (self.low_pass_filter_1, 0))    
        self.connect((self.blocks_wavfile_source_2, 0), (self.low_pass_filter_2, 0))    
        self.connect((self.blocks_wavfile_source_3, 0), (self.low_pass_filter_3, 0))    
        self.connect((self.blocks_wavfile_source_4, 0), (self.low_pass_filter_4, 0))    
        self.connect((self.blocks_wavfile_source_5, 0), (self.low_pass_filter_5, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.low_pass_filter_2, 0), (self.blocks_add_const_vxx_2, 0))    
        self.connect((self.low_pass_filter_3, 0), (self.blocks_add_const_vxx_3, 0))    
        self.connect((self.low_pass_filter_4, 0), (self.blocks_add_const_vxx_4, 0))    
        self.connect((self.low_pass_filter_5, 0), (self.blocks_add_const_vxx_5, 0))    

# start manual block add
# block 6
	self.low_pass_filter_6 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
	self.blocks_wavfile_source_6 = blocks.wavfile_source("Jackbenny-390212LoveFindsAnnieHardy.wav", True)
        self.blocks_multiply_xx_6 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_6 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_6 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 600.006e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_6, 0), (self.blocks_multiply_xx_6, 1))    
        self.connect((self.blocks_add_const_vxx_6, 0), (self.blocks_multiply_xx_6, 0))    
        self.connect((self.blocks_multiply_xx_6, 0), (self.blocks_add_xx_0, 6))    
        self.connect((self.blocks_wavfile_source_6, 0), (self.low_pass_filter_6, 0))    
        self.connect((self.low_pass_filter_6, 0), (self.blocks_add_const_vxx_6, 0))    
# block 7
        self.low_pass_filter_7 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_7 = blocks.wavfile_source("Jackbenny-390219CarmichaelThePolarBear.wav", True)
        self.blocks_multiply_xx_7 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_7 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_7 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 620.005e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_7, 0), (self.blocks_multiply_xx_7, 1))
        self.connect((self.blocks_add_const_vxx_7, 0), (self.blocks_multiply_xx_7, 0))
        self.connect((self.blocks_multiply_xx_7, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_wavfile_source_7, 0), (self.low_pass_filter_7, 0))
        self.connect((self.low_pass_filter_7, 0), (self.blocks_add_const_vxx_7, 0))
# block 8
        self.low_pass_filter_8 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_8 = blocks.wavfile_source("Jackbenny-390226JesseJamespartOne.wav", True)
        self.blocks_multiply_xx_8 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_8 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_8 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 630.004e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_8, 0), (self.blocks_multiply_xx_8, 1))
        self.connect((self.blocks_add_const_vxx_8, 0), (self.blocks_multiply_xx_8, 0))
        self.connect((self.blocks_multiply_xx_8, 0), (self.blocks_add_xx_0, 8))
        self.connect((self.blocks_wavfile_source_8, 0), (self.low_pass_filter_8, 0))
        self.connect((self.low_pass_filter_8, 0), (self.blocks_add_const_vxx_8, 0))
# block 9
        self.low_pass_filter_9 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_9 = blocks.wavfile_source("Jackbenny-390305JesseJamespartTwo.wav", True)
        self.blocks_multiply_xx_9 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_9 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_9 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 640.003e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_9, 0), (self.blocks_multiply_xx_9, 1))
        self.connect((self.blocks_add_const_vxx_9, 0), (self.blocks_multiply_xx_9, 0))
        self.connect((self.blocks_multiply_xx_9, 0), (self.blocks_add_xx_0, 9))
        self.connect((self.blocks_wavfile_source_9, 0), (self.low_pass_filter_9, 0))
        self.connect((self.low_pass_filter_9, 0), (self.blocks_add_const_vxx_9, 0))
# block 10
        self.low_pass_filter_10 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_10 = blocks.wavfile_source("Jackbenny-390312CarmichaelThePolarBearIsSick.wav", True)
        self.blocks_multiply_xx_10 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_10 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_10 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 650.002e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_10, 0), (self.blocks_multiply_xx_10, 1))
        self.connect((self.blocks_add_const_vxx_10, 0), (self.blocks_multiply_xx_10, 0))
        self.connect((self.blocks_multiply_xx_10, 0), (self.blocks_add_xx_0, 10))
        self.connect((self.blocks_wavfile_source_10, 0), (self.low_pass_filter_10, 0))
        self.connect((self.low_pass_filter_10, 0), (self.blocks_add_const_vxx_10, 0))
# block 11
        self.low_pass_filter_11 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_11 = blocks.wavfile_source("Jackbenny-390319JackHasACold.wav", True)
        self.blocks_multiply_xx_11 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_11 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_11 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 660.002e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_11, 0), (self.blocks_multiply_xx_11, 1))
        self.connect((self.blocks_add_const_vxx_11, 0), (self.blocks_multiply_xx_11, 0))
        self.connect((self.blocks_multiply_xx_11, 0), (self.blocks_add_xx_0, 11))
        self.connect((self.blocks_wavfile_source_11, 0), (self.low_pass_filter_11, 0))
        self.connect((self.low_pass_filter_11, 0), (self.blocks_add_const_vxx_11, 0))
# block 12
        self.low_pass_filter_12 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_12 = blocks.wavfile_source("Jackbenny-390326GuestEdSullivan.wav", True)
        self.blocks_multiply_xx_12 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_12 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_12 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 670.001e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_12, 0), (self.blocks_multiply_xx_12, 1))
        self.connect((self.blocks_add_const_vxx_12, 0), (self.blocks_multiply_xx_12, 0))
        self.connect((self.blocks_multiply_xx_12, 0), (self.blocks_add_xx_0, 12))
        self.connect((self.blocks_wavfile_source_12, 0), (self.low_pass_filter_12, 0))
        self.connect((self.low_pass_filter_12, 0), (self.blocks_add_const_vxx_12, 0))
# block 13
        self.low_pass_filter_13 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_13 = blocks.wavfile_source("Jackbenny-390402AprilFools.wav", True)
        self.blocks_multiply_xx_13 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_13 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_13 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 690.000e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_13, 0), (self.blocks_multiply_xx_13, 1))
        self.connect((self.blocks_add_const_vxx_13, 0), (self.blocks_multiply_xx_13, 0))
        self.connect((self.blocks_multiply_xx_13, 0), (self.blocks_add_xx_0, 13))
        self.connect((self.blocks_wavfile_source_13, 0), (self.low_pass_filter_13, 0))
        self.connect((self.low_pass_filter_13, 0), (self.blocks_add_const_vxx_13, 0))
# block 14
        self.low_pass_filter_14 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_14 = blocks.wavfile_source("Jackbenny-390409FourGirlsInWhite.wav", True)
        self.blocks_multiply_xx_14 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_14 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_14 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 700.001e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_14, 0), (self.blocks_multiply_xx_14, 1))
        self.connect((self.blocks_add_const_vxx_14, 0), (self.blocks_multiply_xx_14, 0))
        self.connect((self.blocks_multiply_xx_14, 0), (self.blocks_add_xx_0, 14))
        self.connect((self.blocks_wavfile_source_14, 0), (self.low_pass_filter_14, 0))
        self.connect((self.low_pass_filter_14, 0), (self.blocks_add_const_vxx_14, 0))
# block 15
        self.low_pass_filter_15 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_15 = blocks.wavfile_source("Jackbenny-390416PhilShootsAMovieBehindJacksBack.wav", True)
        self.blocks_multiply_xx_15 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_15 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_15 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 710.002e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_15, 0), (self.blocks_multiply_xx_15, 1))
        self.connect((self.blocks_add_const_vxx_15, 0), (self.blocks_multiply_xx_15, 0))
        self.connect((self.blocks_multiply_xx_15, 0), (self.blocks_add_xx_0, 15))
        self.connect((self.blocks_wavfile_source_15, 0), (self.low_pass_filter_15, 0))
        self.connect((self.low_pass_filter_15, 0), (self.blocks_add_const_vxx_15, 0))
# block 16
        self.low_pass_filter_16 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_16 = blocks.wavfile_source("Jackbenny-390423GuestBinnieBarnesAndMarkSandrich.wav", True)
        self.blocks_multiply_xx_16 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_16 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_16 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 720.003e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_16, 0), (self.blocks_multiply_xx_16, 1))
        self.connect((self.blocks_add_const_vxx_16, 0), (self.blocks_multiply_xx_16, 0))
        self.connect((self.blocks_multiply_xx_16, 0), (self.blocks_add_xx_0, 16))
        self.connect((self.blocks_wavfile_source_16, 0), (self.low_pass_filter_16, 0))
        self.connect((self.low_pass_filter_16, 0), (self.blocks_add_const_vxx_16, 0))
# block 17
        self.low_pass_filter_17 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_17 = blocks.wavfile_source("Jackbenny-390430SeventhAnniversaryShow.wav", True)
        self.blocks_multiply_xx_17 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_17 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_17 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 730.004e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_17, 0), (self.blocks_multiply_xx_17, 1))
        self.connect((self.blocks_add_const_vxx_17, 0), (self.blocks_multiply_xx_17, 0))
        self.connect((self.blocks_multiply_xx_17, 0), (self.blocks_add_xx_0, 17))
        self.connect((self.blocks_wavfile_source_17, 0), (self.low_pass_filter_17, 0))
        self.connect((self.low_pass_filter_17, 0), (self.blocks_add_const_vxx_17, 0))
# block 18
        self.low_pass_filter_18 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_18 = blocks.wavfile_source("Jackbenny-390507TheKentuckyDerby.wav", True)
        self.blocks_multiply_xx_18 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_18 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_18 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 740.005e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_18, 0), (self.blocks_multiply_xx_18, 1))
        self.connect((self.blocks_add_const_vxx_18, 0), (self.blocks_multiply_xx_18, 0))
        self.connect((self.blocks_multiply_xx_18, 0), (self.blocks_add_xx_0, 18))
        self.connect((self.blocks_wavfile_source_18, 0), (self.low_pass_filter_18, 0))
        self.connect((self.low_pass_filter_18, 0), (self.blocks_add_const_vxx_18, 0))
# block 19
        self.low_pass_filter_19 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_19 = blocks.wavfile_source("Jackbenny-390514GungaDin.wav", True)
        self.blocks_multiply_xx_19 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_19 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_19 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 750.006e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_19, 0), (self.blocks_multiply_xx_19, 1))
        self.connect((self.blocks_add_const_vxx_19, 0), (self.blocks_multiply_xx_19, 0))
        self.connect((self.blocks_multiply_xx_19, 0), (self.blocks_add_xx_0, 19))
        self.connect((self.blocks_wavfile_source_19, 0), (self.low_pass_filter_19, 0))
        self.connect((self.low_pass_filter_19, 0), (self.blocks_add_const_vxx_19, 0))
# block 20
        self.low_pass_filter_20 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_20 = blocks.wavfile_source("Jackbenny-390521MoreGungaDin.wav", True)
        self.blocks_multiply_xx_20 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_20 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_20 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 760.005e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_20, 0), (self.blocks_multiply_xx_20, 1))
        self.connect((self.blocks_add_const_vxx_20, 0), (self.blocks_multiply_xx_20, 0))
        self.connect((self.blocks_multiply_xx_20, 0), (self.blocks_add_xx_0, 20))
        self.connect((self.blocks_wavfile_source_20, 0), (self.low_pass_filter_20, 0))
        self.connect((self.low_pass_filter_20, 0), (self.blocks_add_const_vxx_20, 0))
# block 21
        self.low_pass_filter_21 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_21 = blocks.wavfile_source("Jackbenny-390528AlexanderGrahamBell.wav", True)
        self.blocks_multiply_xx_21 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_21 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_21 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 770.004e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_21, 0), (self.blocks_multiply_xx_21, 1))
        self.connect((self.blocks_add_const_vxx_21, 0), (self.blocks_multiply_xx_21, 0))
        self.connect((self.blocks_multiply_xx_21, 0), (self.blocks_add_xx_0, 21))
        self.connect((self.blocks_wavfile_source_21, 0), (self.low_pass_filter_21, 0))
        self.connect((self.low_pass_filter_21, 0), (self.blocks_add_const_vxx_21, 0))
# block 22
        self.low_pass_filter_22 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_22 = blocks.wavfile_source("Jackbenny-390604PreviewOfHoundOfTheBaskervilles.wav", True)
        self.blocks_multiply_xx_22 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_22 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_22 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 780.003e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_22, 0), (self.blocks_multiply_xx_22, 1))
        self.connect((self.blocks_add_const_vxx_22, 0), (self.blocks_multiply_xx_22, 0))
        self.connect((self.blocks_multiply_xx_22, 0), (self.blocks_add_xx_0, 22))
        self.connect((self.blocks_wavfile_source_22, 0), (self.low_pass_filter_22, 0))
        self.connect((self.low_pass_filter_22, 0), (self.blocks_add_const_vxx_22, 0))
# block 23
        self.low_pass_filter_23 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_23 = blocks.wavfile_source("Jackbenny-390618FathersDayLeavingForWaukegan.wav", True)
        self.blocks_multiply_xx_23 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_23 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_23 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 790.002e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_23, 0), (self.blocks_multiply_xx_23, 1))
        self.connect((self.blocks_add_const_vxx_23, 0), (self.blocks_multiply_xx_23, 0))
        self.connect((self.blocks_multiply_xx_23, 0), (self.blocks_add_xx_0, 23))
        self.connect((self.blocks_wavfile_source_23, 0), (self.low_pass_filter_23, 0))
        self.connect((self.low_pass_filter_23, 0), (self.blocks_add_const_vxx_23, 0))
# block 24
        self.low_pass_filter_24 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_24 = blocks.wavfile_source("Jackbenny-390625LastShowOfTheSeasonFromWaukegan.wav", True)
        self.blocks_multiply_xx_24 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_24 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_24 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 800.001e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_24, 0), (self.blocks_multiply_xx_24, 1))
        self.connect((self.blocks_add_const_vxx_24, 0), (self.blocks_multiply_xx_24, 0))
        self.connect((self.blocks_multiply_xx_24, 0), (self.blocks_add_xx_0, 24))
        self.connect((self.blocks_wavfile_source_24, 0), (self.low_pass_filter_24, 0))
        self.connect((self.low_pass_filter_24, 0), (self.blocks_add_const_vxx_24, 0))
# block 25
        self.low_pass_filter_25 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_25 = blocks.wavfile_source("Jackbenny-391008DennisDaysFirstShow.wav", True)
        self.blocks_multiply_xx_25 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_25 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_25 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 810.000e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_25, 0), (self.blocks_multiply_xx_25, 1))
        self.connect((self.blocks_add_const_vxx_25, 0), (self.blocks_multiply_xx_25, 0))
        self.connect((self.blocks_multiply_xx_25, 0), (self.blocks_add_xx_0, 25))
        self.connect((self.blocks_wavfile_source_25, 0), (self.low_pass_filter_25, 0))
        self.connect((self.low_pass_filter_25, 0), (self.blocks_add_const_vxx_25, 0))
# block 26
        self.low_pass_filter_26 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_26 = blocks.wavfile_source("Jackbenny-391015DennissMotherInterferes.wav", True)
        self.blocks_multiply_xx_26 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_26 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_26 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 820.001e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_26, 0), (self.blocks_multiply_xx_26, 1))
        self.connect((self.blocks_add_const_vxx_26, 0), (self.blocks_multiply_xx_26, 0))
        self.connect((self.blocks_multiply_xx_26, 0), (self.blocks_add_xx_0, 26))
        self.connect((self.blocks_wavfile_source_26, 0), (self.low_pass_filter_26, 0))
        self.connect((self.low_pass_filter_26, 0), (self.blocks_add_const_vxx_26, 0))
# block 27
        self.low_pass_filter_27 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_27 = blocks.wavfile_source("Jackbenny-391022StanleyAndLivingstone.wav", True)
        self.blocks_multiply_xx_27 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_27 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_27 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 830.002e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_27, 0), (self.blocks_multiply_xx_27, 1))
        self.connect((self.blocks_add_const_vxx_27, 0), (self.blocks_multiply_xx_27, 0))
        self.connect((self.blocks_multiply_xx_27, 0), (self.blocks_add_xx_0, 27))
        self.connect((self.blocks_wavfile_source_27, 0), (self.low_pass_filter_27, 0))
        self.connect((self.low_pass_filter_27, 0), (self.blocks_add_const_vxx_27, 0))
# block 28
        self.low_pass_filter_28 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_28 = blocks.wavfile_source("Jackbenny-391029TheHalloweenMasqueradeParty.wav", True)
        self.blocks_multiply_xx_28 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_28 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_28 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 840.003e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_28, 0), (self.blocks_multiply_xx_28, 1))
        self.connect((self.blocks_add_const_vxx_28, 0), (self.blocks_multiply_xx_28, 0))
        self.connect((self.blocks_multiply_xx_28, 0), (self.blocks_add_xx_0, 28))
        self.connect((self.blocks_wavfile_source_28, 0), (self.low_pass_filter_28, 0))
        self.connect((self.low_pass_filter_28, 0), (self.blocks_add_const_vxx_28, 0))
# block 29
        self.low_pass_filter_29 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_29 = blocks.wavfile_source("Jackbenny-391105TheWomen.wav", True)
        self.blocks_multiply_xx_29 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_29 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_29 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 850.004e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_29, 0), (self.blocks_multiply_xx_29, 1))
        self.connect((self.blocks_add_const_vxx_29, 0), (self.blocks_multiply_xx_29, 0))
        self.connect((self.blocks_multiply_xx_29, 0), (self.blocks_add_xx_0, 29))
        self.connect((self.blocks_wavfile_source_29, 0), (self.low_pass_filter_29, 0))
        self.connect((self.low_pass_filter_29, 0), (self.blocks_add_const_vxx_29, 0))
# block 30
        self.low_pass_filter_30 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_30 = blocks.wavfile_source("Jackbenny-391112JacksToothache.wav", True)
        self.blocks_multiply_xx_30 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_30 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_30 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 860.005e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_30, 0), (self.blocks_multiply_xx_30, 1))
        self.connect((self.blocks_add_const_vxx_30, 0), (self.blocks_multiply_xx_30, 0))
        self.connect((self.blocks_multiply_xx_30, 0), (self.blocks_add_xx_0, 30))
        self.connect((self.blocks_wavfile_source_30, 0), (self.low_pass_filter_30, 0))
        self.connect((self.low_pass_filter_30, 0), (self.blocks_add_const_vxx_30, 0))
# block 31
        self.low_pass_filter_31 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
                fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_31 = blocks.wavfile_source("Jackbenny-391119MarysThanksgivingPoem.wav", True)
        self.blocks_multiply_xx_31 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_31 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_31 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 870.006e3, 1, 0)
# connections
        self.connect((self.analog_sig_source_x_31, 0), (self.blocks_multiply_xx_31, 1))
        self.connect((self.blocks_add_const_vxx_31, 0), (self.blocks_multiply_xx_31, 0))
        self.connect((self.blocks_multiply_xx_31, 0), (self.blocks_add_xx_0, 31))
        self.connect((self.blocks_wavfile_source_31, 0), (self.low_pass_filter_31, 0))
        self.connect((self.low_pass_filter_31, 0), (self.blocks_add_const_vxx_31, 0))


# end manual block add

    def get_rf_sample_rate(self):
        return self.rf_sample_rate

    def set_rf_sample_rate(self, rf_sample_rate):
        self.rf_sample_rate = rf_sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.rf_sample_rate)
        self.analog_sig_source_x_5.set_sampling_freq(self.rf_sample_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_3.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_4.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_5.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.rf_sample_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.rf_sample_rate)

    def get_fir_interp(self):
        return self.fir_interp

    def set_fir_interp(self, fir_interp):
        self.fir_interp = fir_interp

    def get_fgain(self):
        return self.fgain

    def set_fgain(self, fgain):
        self.fgain = fgain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_3.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_4.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_5.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))

    def get_af_sample_rate(self):
        return self.af_sample_rate

    def set_af_sample_rate(self, af_sample_rate):
        self.af_sample_rate = af_sample_rate


def main(top_block_cls=am_xmit_multi_carrier_fl2k, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
