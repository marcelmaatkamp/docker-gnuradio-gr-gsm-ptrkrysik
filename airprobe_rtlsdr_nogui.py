#!/usr/bin/python2
##################################################
# Gnuradio Python Flow Graph
# Title: Airprobe Rtlsdr
# Generated: Sun Feb 15 11:35:00 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import grgsm
import osmosdr
import pmt
import sip
import sys
import time

from distutils.version import StrictVersion
class airprobe_rtlsdr(gr.top_block):

    def __init__(self, fc=939.4e6, gain=30, samp_rate=2000000.052982, ppm=0):
        gr.top_block.__init__(self, "Airprobe Rtlsdr")

        ##################################################
        # Parameters
        ##################################################
        self.fc = fc
        self.gain = gain
        self.samp_rate = samp_rate
        self.ppm = ppm

        ##################################################
        # Variables
        ##################################################
        self.ppm_slider = ppm_slider = ppm
        self.g_slider = g_slider = gain
        self.fc_slider = fc_slider = fc
        self.SDCCH = SDCCH = 6
        self.SACCH = SACCH = 0x80
        self.RACH = RACH = 3
        self.PCH = PCH = 5
        self.CHANNEL_UNKNOWN = CHANNEL_UNKNOWN = 0
        self.CCCH = CCCH = 2
        self.BCCH = BCCH = 1
        self.AGCH = AGCH = 4

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(fc_slider, 0)
        self.rtlsdr_source_0.set_freq_corr(ppm_slider, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(g_slider, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(250e3, 0)
          
        self.gsm_universal_ctrl_chans_demapper_0 = grgsm.universal_ctrl_chans_demapper(0, ([2,6,12,16,22,26,32,36,42,46]), ([BCCH,CCCH,CCCH,CCCH,CCCH,CCCH,CCCH,CCCH,CCCH,CCCH]))
        self.gsm_receiver_0 = grgsm.receiver(4, ([0]), ([]))
        self.gsm_message_printer_1 = grgsm.message_printer(pmt.intern(""))
        self.gsm_input_0 = grgsm.gsm_input(
            ppm=0,
            osr=4,
            fc=fc,
            samp_rate_in=samp_rate,
        )
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        self.gsm_clock_offset_control_0 = grgsm.clock_offset_control(fc)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "rabbitmq", "4729", 10000)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.gsm_input_0, 0), (self.gsm_receiver_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.gsm_input_0, 0))

        ##################################################
        # Message Connections
        ##################################################
        self.msg_connect(self.gsm_receiver_0, "C0", self.gsm_universal_ctrl_chans_demapper_0, "bursts")
        self.msg_connect(self.gsm_clock_offset_control_0, "ppm", self.gsm_input_0, "ppm_in")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_universal_ctrl_chans_demapper_0, "bursts", self.gsm_control_channels_decoder_0, "bursts")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_receiver_0, "measurements", self.gsm_clock_offset_control_0, "measurements")

    def closeEvent(self, event):
        event.accept()

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.gsm_input_0.set_fc(self.fc)
        self.set_fc_slider(self.fc)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_g_slider(self.gain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.gsm_input_0.set_samp_rate_in(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.set_ppm_slider(self.ppm)

    def get_ppm_slider(self):
        return self.ppm_slider

    def set_ppm_slider(self, ppm_slider):
        self.ppm_slider = ppm_slider
        self.rtlsdr_source_0.set_freq_corr(self.ppm_slider, 0)

    def get_g_slider(self):
        return self.g_slider

    def set_g_slider(self, g_slider):
        self.g_slider = g_slider
        self.rtlsdr_source_0.set_gain(self.g_slider, 0)

    def get_fc_slider(self):
        return self.fc_slider

    def set_fc_slider(self, fc_slider):
        self.fc_slider = fc_slider
        self.rtlsdr_source_0.set_center_freq(self.fc_slider, 0)

    def get_SDCCH(self):
        return self.SDCCH

    def set_SDCCH(self, SDCCH):
        self.SDCCH = SDCCH

    def get_SACCH(self):
        return self.SACCH

    def set_SACCH(self, SACCH):
        self.SACCH = SACCH

    def get_RACH(self):
        return self.RACH

    def set_RACH(self, RACH):
        self.RACH = RACH

    def get_PCH(self):
        return self.PCH

    def set_PCH(self, PCH):
        self.PCH = PCH

    def get_CHANNEL_UNKNOWN(self):
        return self.CHANNEL_UNKNOWN

    def set_CHANNEL_UNKNOWN(self, CHANNEL_UNKNOWN):
        self.CHANNEL_UNKNOWN = CHANNEL_UNKNOWN

    def get_CCCH(self):
        return self.CCCH

    def set_CCCH(self, CCCH):
        self.CCCH = CCCH

    def get_BCCH(self):
        return self.BCCH

    def set_BCCH(self, BCCH):
        self.BCCH = BCCH

    def get_AGCH(self):
        return self.AGCH

    def set_AGCH(self, AGCH):
        self.AGCH = AGCH

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-f", "--fc", dest="fc", type="eng_float", default=eng_notation.num_to_str(939.4e6),
        help="Set fc [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set gain [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2000000.052982),
        help="Set samp_rate [default=%default]")
    parser.add_option("-p", "--ppm", dest="ppm", type="intx", default=0,
        help="Set ppm [default=%default]")
    (options, args) = parser.parse_args()
    tb = airprobe_rtlsdr(fc=options.fc, gain=options.gain, samp_rate=options.samp_rate, ppm=options.ppm)
    # tb.start()
    tb.run()
    def quitting():
        tb.stop()
        tb.wait()
    tb = None #to clean up Qt widgets
