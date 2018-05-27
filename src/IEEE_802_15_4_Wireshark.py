#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: IEEE 802.15.4 to Wireshark
# Author: Scott Elliott
# Generated: Sat May 26 21:30:24 2018
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

def struct(data): return type('Struct', (object,), data)()
from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from math import sin, pi
from optparse import OptionParser
import epy_block_0
import foo
import ieee802_15_4
import math
import osmosdr
import pmt
import rftap
import sip
import sys
import time
from gnuradio import qtgui


class IEEE_802_15_4_Wireshark(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "IEEE 802.15.4 to Wireshark")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IEEE 802.15.4 to Wireshark")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "IEEE_802_15_4_Wireshark")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.ComFreqStruct = ComFreqStruct = struct({'Ch11': 2.405, 'Ch12': 2.410, 'Ch13': 2.415, 'Ch14': 2.420, 'Ch15': 2.425, 'Ch16': 2.430, 'Ch17': 2.435, 'Ch18': 2.440, 'Ch19': 2.445, 'Ch20': 2.450, 'Ch21': 2.455, 'Ch22': 2.460, 'Ch23': 2.465, 'Ch24': 2.470, 'Ch25': 2.475, 'Ch26': 2.480, })
        self.CH = CH = "Ch24"
        self.freq = freq = getattr(ComFreqStruct,CH) * 1000000000
        self.samp_rate = samp_rate = 4000000
        self.rx_gain = rx_gain = 25
        self.if_gain = if_gain = 20
        self.comm_freq_label = comm_freq_label = freq
        self.bb_gain = bb_gain = 20

        ##################################################
        # Blocks
        ##################################################
        self._rx_gain_range = Range(0, 50, 1, 25, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "rx_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 96, 0, 1, 1)
        for r in range(96, 97):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._if_gain_range = Range(0, 50, 1, 20, 200)
        self._if_gain_win = RangeWidget(self._if_gain_range, self.set_if_gain, 'if_gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_gain_win, 97, 0, 1, 1)
        for r in range(97, 98):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._bb_gain_range = Range(0, 50, 1, 20, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, 'BB', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win, 98, 0, 1, 1)
        for r in range(98, 99):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.00016, 1)
        self.rftap_rftap_encap_0 = rftap.rftap_encap(3, -1, 'wpan')
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate/2, #bw
        	"raw", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['Raw', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 7, 0, 1, 4)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Rx", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-0.5, 0.5)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.2, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['Raw DC Blocked R', 'Raw DC Blocked I', 'dqpsk R', 'dqpsk I', 'Sub i',
                  'Sub q', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "yellow", "blue", "cyan", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 5, 0, 1, 4)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_1_1 = qtgui.const_sink_c(
        	1024, #size
        	"Rx", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_1.set_update_time(0.1)
        self.qtgui_const_sink_x_1_1.set_y_axis(-0.4, 0.4)
        self.qtgui_const_sink_x_1_1.set_x_axis(-0.4, 0.4)
        self.qtgui_const_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.4, 0, "")
        self.qtgui_const_sink_x_1_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1_1.enable_grid(False)
        self.qtgui_const_sink_x_1_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_1_1.disable_legend()

        labels = ['Rx raw', 'DQPSK Soft', 'MPSK', 'Unbuf', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["Dark Blue", "red", "yellow", "cyan", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 4, 5, 0,
                  0, 0, 0, 0, 0]
        markers = [9, 7, 6, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_1_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'soapy=0,driver=lime' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(rx_gain, 0)
        self.osmosdr_source_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0.set_antenna('LNAH', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.ieee802_15_4_packet_sink_0 = ieee802_15_4.packet_sink(10)
        self.foo_wireshark_connector_0 = foo.wireshark_connector(195, False)
        self.epy_block_0 = epy_block_0.blk()
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(2, 0.000225, 0.5, 0.03, 0.0002)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self._comm_freq_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._comm_freq_label_formatter = None
        else:
          self._comm_freq_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._comm_freq_label_tool_bar.addWidget(Qt.QLabel('Com Freq:'+": "))
        self._comm_freq_label_label = Qt.QLabel(str(self._comm_freq_label_formatter(self.comm_freq_label)))
        self._comm_freq_label_tool_bar.addWidget(self._comm_freq_label_label)
        self.top_grid_layout.addWidget(self._comm_freq_label_tool_bar, 99, 1, 1, 1)
        for r in range(99, 100):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", '127.0.0.1', '52006', 10000, False)
        self.blocks_pdu_set_0 = blocks.pdu_set(pmt.to_pmt("nomfreq"), pmt.to_pmt(freq))
        self.blocks_message_debug_1_0 = blocks.message_debug()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/tmp/sensor.pcap', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)
        self._CH_options = ("Ch24", "Ch25", "Ch26", "Ch11", "Ch12", )
        self._CH_labels = ('24', '25', '26', '11', '12', )
        self._CH_group_box = Qt.QGroupBox('802.15.4 Channel')
        self._CH_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._CH_button_group = variable_chooser_button_group()
        self._CH_group_box.setLayout(self._CH_box)
        for i, label in enumerate(self._CH_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._CH_box.addWidget(radio_button)
        	self._CH_button_group.addButton(radio_button, i)
        self._CH_callback = lambda i: Qt.QMetaObject.invokeMethod(self._CH_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._CH_options.index(i)))
        self._CH_callback(self.CH)
        self._CH_button_group.buttonClicked[int].connect(
        	lambda i: self.set_CH(self._CH_options[i]))
        self.top_grid_layout.addWidget(self._CH_group_box, 99, 0, 1, 1)
        for r in range(99, 100):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_pdu_set_0, 'pdus'), (self.rftap_rftap_encap_0, 'in'))
        self.msg_connect((self.epy_block_0, 'out'), (self.blocks_pdu_set_0, 'pdus'))
        self.msg_connect((self.ieee802_15_4_packet_sink_0, 'out'), (self.blocks_message_debug_1_0, 'print_pdu'))
        self.msg_connect((self.ieee802_15_4_packet_sink_0, 'out'), (self.epy_block_0, 'in'))
        self.msg_connect((self.ieee802_15_4_packet_sink_0, 'out'), (self.foo_wireshark_connector_0, 'in'))
        self.msg_connect((self.rftap_rftap_encap_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_const_sink_x_1_1, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.ieee802_15_4_packet_sink_0, 0))
        self.connect((self.foo_wireshark_connector_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_sub_xx_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "IEEE_802_15_4_Wireshark")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ComFreqStruct(self):
        return self.ComFreqStruct

    def set_ComFreqStruct(self, ComFreqStruct):
        self.ComFreqStruct = ComFreqStruct
        self.set_freq(getattr(self.ComFreqStruct,self.CH) * 1000000000)

    def get_CH(self):
        return self.CH

    def set_CH(self, CH):
        self.CH = CH
        self.set_freq(getattr(self.ComFreqStruct,self.CH) * 1000000000)
        self._CH_callback(self.CH)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate/2)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.set_comm_freq_label(self._comm_freq_label_formatter(self.freq))
        self.blocks_pdu_set_0.set_val(pmt.to_pmt(self.freq))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.samp_rate/2)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.osmosdr_source_0.set_gain(self.rx_gain, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)

    def get_comm_freq_label(self):
        return self.comm_freq_label

    def set_comm_freq_label(self, comm_freq_label):
        self.comm_freq_label = comm_freq_label
        Qt.QMetaObject.invokeMethod(self._comm_freq_label_label, "setText", Qt.Q_ARG("QString", self.comm_freq_label))

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=IEEE_802_15_4_Wireshark, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
