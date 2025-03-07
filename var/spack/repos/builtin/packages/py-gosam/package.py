# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGosam(Package):
    """The package GoSam allows for the automated calculation of
       one-loop amplitudes for multi-particle processes in renormalizable
       quantum field theories."""

    homepage = "https://github.com/gudrunhe/gosam"
    git      = "https://github.com/gudrunhe/gosam.git"

    tags = ['hep']

    extends('python')

    version('2.1.1', url="https://github.com/gudrunhe/gosam/releases/download/2.1.1/gosam-2.1.1-4b98559.tar.gz",
            sha256="4a2b9160d51e3532025b9579a4d17d0e0f8a755b8481aeb8271c1f58eb97ab01")
    version('2.0.4', sha256='faf621c70f66d9dffc16ac5cce66258067f39f686d722a4867eeb759fcde4f44',
            url='https://gosam.hepforge.org/downloads/?f=gosam-2.0.4-6d9f1cba.tar.gz')
    version('2.0.3', tag='v2.0.3', commit='4146ab23a06b7c57c10fb36df60758d34aa58387')

    depends_on('form', type='run')
    depends_on('qgraf', type='run')
    depends_on('gosam-contrib', type='link')
    depends_on('python@2.7.0:2.7', type=('build', 'run'), when='@:2.0.4')
    depends_on('python@3:', type=('build', 'run'), when='@2.1.1:')

    phases = ['build', 'install']

    def setup_run_environment(self, env):
        gosam_contrib_lib_dir = self.spec['gosam-contrib'].prefix.lib
        env.prepend_path('LD_LIBRARY_PATH', gosam_contrib_lib_dir)

    def build(self, spec, prefix):
        python('-s', 'setup.py', '--no-user-cfg', 'build')

    def install(self, spec, prefix):
        python('-s', 'setup.py', '--no-user-cfg', 'install', '--prefix=' + prefix)
