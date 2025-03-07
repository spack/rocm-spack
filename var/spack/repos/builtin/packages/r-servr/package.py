# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RServr(RPackage):
    """A Simple HTTP Server to Serve Static Files or Dynamic Documents.

    Start an HTTP server in R to serve static files, or dynamic documents that
    can be converted to HTML files (e.g., R Markdown) under a given
    directory."""

    cran = "servr"

    version('0.24', sha256='d94e1d31802ce6bbab7a5838ff94cbca8cd998237d834ff25fedf7514f41a087')
    version('0.21', sha256='3fc0da063dd04b796a49ce62bf8e69d5854679520da90cc92ee3fc0a0b2ad389')

    depends_on('r@3.0.0:', type=('build', 'run'))
    depends_on('r-mime@0.2:', type=('build', 'run'))
    depends_on('r-httpuv@1.5.2:', type=('build', 'run'))
    depends_on('r-xfun', type=('build', 'run'))
    depends_on('r-jsonlite', type=('build', 'run'))
