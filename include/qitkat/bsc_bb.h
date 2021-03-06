/* -*- c++ -*- */
/* 
 * Copyright 2014 Travis S. Humble - Oak Ridge National Laboratory
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_QITKAT_BSC_BB_H
#define INCLUDED_QITKAT_BSC_BB_H

#include <qitkat/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace qitkat {

    /*!
     * \brief A binary symmetric channel.
     * \ingroup qitkat
     *
     */
    class QITKAT_API bsc_bb : virtual public gr::sync_block {
     public:
      typedef boost::shared_ptr<bsc_bb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of qitkat::bsc_bb.
       *
       * To avoid accidental use of raw pointers, qitkat::bsc_bb's
       * constructor is in a private implementation
       * class. qitkat::bsc_bb::make is the public interface for
       * creating new instances.
       */
      static sptr make(float error_rate, unsigned int seed, unsigned char bit_mask);
    };

  } // namespace qitkat
} // namespace gr

#endif /* INCLUDED_QITKAT_BSC_BB_H */

