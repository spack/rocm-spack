# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RCrayon(RPackage):
    """Colored Terminal Output.

    Colored terminal output on terminals that support 'ANSI' color and
    highlight codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is
    automatically detected. Colors and highlighting can be combined and nested.
    New styles can also be created easily. This package was inspired by the
    'chalk' 'JavaScript' project."""

    cran = "crayon"

    version('1.4.2', sha256='ee34397f643e76e30588068d4c93bd3c9afd2193deacccacb3bffcadf141b857')
    version('1.4.1', sha256='08b6e42e748d096960b2f32b7ffe690c25742e29fe14c19d1834cd6ff43029c7')
    version('1.3.4', sha256='fc6e9bf990e9532c4fcf1a3d2ce22d8cf12d25a95e4779adfa17713ed836fa68')
    version('1.3.2', sha256='9a6b75d63c05fe64baf222f1921330ceb727924bcc5fc2753ff0528d42555e68')
