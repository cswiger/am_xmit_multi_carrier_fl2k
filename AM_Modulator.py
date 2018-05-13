# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Am Modulator
# Author: cswiger
# Description: Am Modulator
# Generated: Sun May 13 12:05:00 2018
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes


class AM_Modulator(gr.hier_block2):

    def __init__(self, fgain=128, fir_interp=512, carrier_freq=530e3, rf_sample_rate=8192000, af_sample_rate=16000, filename="pgm1.wav"):
        gr.hier_block2.__init__(
            self, "Am Modulator",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fgain = fgain
        self.fir_interp = fir_interp
        self.carrier_freq = carrier_freq
        self.rf_sample_rate = rf_sample_rate
        self.af_sample_rate = af_sample_rate
        self.filename = filename

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(fir_interp, firdes.low_pass(
        	fgain, rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source(filename, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.analog_sig_source_x_0 = analog.sig_source_f(rf_sample_rate, analog.GR_COS_WAVE, carrier_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_const_vxx_0, 0))    

    def get_fgain(self):
        return self.fgain

    def set_fgain(self, fgain):
        self.fgain = fgain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))

    def get_fir_interp(self):
        return self.fir_interp

    def set_fir_interp(self, fir_interp):
        self.fir_interp = fir_interp

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_0.set_frequency(self.carrier_freq)

    def get_rf_sample_rate(self):
        return self.rf_sample_rate

    def set_rf_sample_rate(self, rf_sample_rate):
        self.rf_sample_rate = rf_sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.rf_sample_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.fgain, self.rf_sample_rate, 8e3, 4e3, firdes.WIN_HAMMING, 6.76))

    def get_af_sample_rate(self):
        return self.af_sample_rate

    def set_af_sample_rate(self, af_sample_rate):
        self.af_sample_rate = af_sample_rate

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
