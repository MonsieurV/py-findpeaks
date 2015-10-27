#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Yoan Tournade <yoan@ytotech.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
import unittest
import numpy as np
from detect_peaks import detect_peaks

class PythonPeakUtilsFindpeaksTestCase(unittest.TestCase):
    """ Test the PeakUtils package. """

    def test_octave_findpeaks_equal_matlab_findpeaks_minpeakheight_1(self):
        """ Check that Octave findpeaks mimics well the original MatLab findpeaks, with minpeakheight filter. """
        # Find peaks on this vector.
        vector = [ 0, 6, 25, 20, 15, 8, 15, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8,
            10, 3, 1, 20, 7, 3, 0 ]
        # 'MinPeakHeight', 22
        loc = detect_peaks(vector, mph=22)
        print(loc)
        self.assertEqual(
            loc.tolist(),
            [8-1])

    def test_octave_findpeaks_equal_matlab_findpeaks_minpeakheight_2(self):
        """ Check that Octave findpeaks mimics well the original MatLab findpeaks, with minpeakheight filter. """
        # Find peaks on this vector.
        vector = [
            0.000000000000001, 3.651411362475055, 4.347239816515587,
            3.229238311887470, 2.057044119108341, 4.289416174922050,
            4.623656294357088, 16.991500296151141, 23.710596923344340,
            5.194447742667983, 5.392090702263596
        ]
        # 'MinPeakHeight', 22
        loc = detect_peaks(vector, mph=22)
        print(loc)
        self.assertEqual(
            loc.tolist(),
            [9-1])

    def test_octave_findpeaks_equal_matlab_findpeaks_minpeakheight_3(self):
        """ Check that Octave findpeaks mimics well the original MatLab findpeaks, with minpeakheight filter. """
        # Find peaks on this vector.
        vector = [
            0.000000000000002, 4.304968393969253, 2.524429995956715,
            1.362350996472030, 8.651011827706597, 5.355103964053995,
            4.166135802128525, 7.111434648523146, 41.368426443580518,
            13.753049599045664, 11.652130301046128
        ]
        # 'MinPeakHeight', 22
        loc = detect_peaks(vector, mph=22, mpd=None)
        print(loc)
        self.assertEqual(
            loc.tolist(),
            [9-1])

    def test_octave_findpeaks_equal_matlab_findpeaks_minpeakheight_minpeakdistance(self):
        """ Check that Octave findpeaks mimics well the original MatLab findpeaks, with minpeakheight and minpeakdistance filter. """
        # Find peaks on this vector.
        vector = [
            0.199196234460946, 0.150971091401259, 0.066830193587158, -0.007815333052105, -0.044616654524390, -0.055795361348227, -0.076137152400651, -0.118170367279712, -0.163440493736020, -0.190516609994619, -0.176483713717207, -0.126265512667095,
            -0.085683530051180, -0.070626701579825, -0.056650272247038, -0.018164912522573, 0.042641790158567, 0.084300842806316, 0.091380642181674, 0.086612641403415, 0.076804338682254, 0.065114059315175, 0.061730123648466, 0.062054559470569,
            0.037808369894233, -0.007903466706924, -0.022105492056923, 0.022875099403569, 0.100256509561853, 0.161610966145234, 0.188078783724511, 0.179791428716887, 0.127483188979423, 0.037101235419981, -0.061551863605861, -0.134872789642774,
            -0.170882136762535, -0.180232519836007, -0.193873842670550, -0.220596208762850, -0.217710728542538, -0.154566709841264, -0.052288376793704, 0.024309953763214, 0.036995233638215, 0.027385387267975, 0.034756425571608, 0.044538621477845,
            0.048179094187324, 0.062762787751685, 0.093756722731978, 0.128746079656537, 0.140220257694886, 0.107177963642096, 0.064168137422344, 0.049034449543362, 0.043561872239351, 0.037112836659310, 0.049484512152412, 0.075511915362878,
            0.082621740035262, 0.059833540054286, 0.025160333364946, -0.011362411779154, -0.059885473889260, -0.116916348401991, -0.160033412094328, -0.186277401172449, -0.227970985597943, -0.293012110994312, -0.316846014874940, -0.235793951154457,
            -0.071213154358508, 0.087635348114046, 0.166528547043995, 0.156622093806762, 0.114536824444267, 0.098795472321648, 0.106794539180316, 0.123935062619566, 0.138240918685253, 0.120041711787775, 0.065711290699853, -0.020477124669418,
            -0.121124845572754, -0.163652703975820, -0.088146112206319, 0.062253992836015, 0.185115302006708, 0.251310089224804, 0.275507327595166, 0.240646546675415, 0.144130827133559, 0.028378284476590, -0.050543164088393, -0.082379193202235,
            -0.108933261445066, -0.149993661967355, -0.188079227296676, -0.184552832746794
        ]
        # 'MinPeakHeight', 0.05, 'MinPeakDistance', 10, 'MinPeakWidth', 0
        loc = detect_peaks(vector, mph=0.05, mpd=10)
        print(loc)
        self.assertEqual(
            loc.tolist(),
            [19-1, 31-1, 53-1, 75-1, 91-1])
