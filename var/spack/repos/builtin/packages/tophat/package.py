# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.boost import Boost


class Tophat(AutotoolsPackage):
    """Spliced read mapper for RNA-Seq."""

    homepage = "https://ccb.jhu.edu/software/tophat/index.shtml"
    url      = "https://github.com/infphilo/tophat/archive/v2.1.1.tar.gz"

    version('2.1.2', sha256='15016b82255dad085d4ee7d970e50f0e53a280d466335553d47790d8344ff4b1')
    version('2.1.1', sha256='991b1b7c840a5f5c4e9a15b2815983257d2b0748246af0b9094c7d07552b023e')

    depends_on('autoconf', type='build')
    # 2.1.1 only builds with automake@1.15.1.  There's a patch here:
    # https://github.com/spack/spack/pull/8244, which was incorporated
    # upstream in 2.1.2, which is known to build with 1.16.1 and 1.15.1.
    depends_on('automake',                        type='build')
    depends_on('automake@1.15.1', when='@:2.1.1', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('boost@1.47:')

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)
    depends_on('bowtie2', type='run')

    parallel = False

    def setup_build_environment(self, env):
        env.append_flags("CFLAGS", self.compiler.cxx98_flag)

    def configure_args(self):
        return ["--with-boost={0}".format(self.spec['boost'].prefix)]
