#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 Ronald Sadlier - Oak Ridge National Laboratory
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import qitkat_swig as qitkat

class qa_ecc_golay2412_decode_bb(gr_unittest.TestCase):

  def setUp(self):
    self.tb = gr.top_block()

  def tearDown(self):
    self.tb = None

  def test_001(self):
    ''' 
        We got our Golay2412 encoding/decoding algorithm from a reputable source, so for now
        we can assume that it works correctly.
        
        TODO: Add our own tests for Golay2412
    '''
    self.tb.run()

if __name__ == '__main__':
    gr_unittest.run(qa_ecc_golay2412_decode_bb, "qa_ecc_golay2412_decode_bb.xml")
