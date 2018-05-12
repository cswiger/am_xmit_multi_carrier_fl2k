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
#        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
#        	self.GetWin(),
#        	title="Scope Plot",
#        	sample_rate=rf_sample_rate,
#        	v_scale=0,
#        	v_offset=0,
#        	t_scale=0,
#        	ac_couple=False,
#        	xy_mode=False,
#        	num_inputs=1,
#        	trig_mode=wxgui.TRIG_MODE_AUTO,
#        	y_axis_label="Counts",
#        )
#        self.Add(self.wxgui_scopesink2_0.win)
#        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
#        	self.GetWin(),
#        	baseband_freq=0,
#        	y_per_div=10,
#        	y_divs=10,
#        	ref_level=0,
#        	ref_scale=2.0,
#        	sample_rate=rf_sample_rate,
#        	fft_size=1024,
#        	fft_rate=15,
#        	average=False,
#        	avg_alpha=None,
#        	title="FFT Plot",
#        	peak_hold=False,
#        )
#        self.Add(self.wxgui_fftsink2_0.win)
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
        self.blocks_multiply_const_vxx_6 = blocks.multiply_const_vff((.2, ))
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
        self.analog_sig_source_x_5 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 850.006e3, 1, 0)
        self.analog_sig_source_x_4 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 830.005e3, 1, 0)
        self.analog_sig_source_x_3 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 810.004e3, 1, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 790.003e3, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(rf_sample_rate, analog.GR_SIN_WAVE, 770.002e3, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, 750.001e3, 1, 0)

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
#        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.wxgui_fftsink2_0, 0))    
#        self.connect((self.blocks_multiply_const_vxx_6, 0), (self.wxgui_scopesink2_0, 0))    
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
