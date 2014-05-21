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

class qa_quantum_manager_query(gr_unittest.TestCase):
  def setUp(self):
    self.tb = gr.top_block()

  def tearDown(self):
    self.tb = None

  # There aren't really any tests possible for this block.

if __name__ == '__main__':
    gr_unittest.run(qa_quantum_manager_query, "qa_quantum_manager_query.xml")
