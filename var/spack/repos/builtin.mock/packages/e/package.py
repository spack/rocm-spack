# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class E(Package):
    """Simple package with no dependencies"""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/e-1.0.tar.gz"

    version('1.0', '0123456789abcdef0123456789abcdef')
