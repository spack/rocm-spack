# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class DamaskGrid(CMakePackage):
    """Grid solver for DAMASK"""

    homepage = "https://damask.mpie.de"
    url      = "https://damask.mpie.de/download/damask-3.0.0.tar.xz"

    maintainers = ['MarDiehl']

    version('3.0.0-alpha4', sha256='0bb8bde43b27d852b1fb6e359a7157354544557ad83d87987b03f5d629ce5493')
    version('3.0.0-alpha5', sha256='2d2b10901959c26a5bb5c52327cdafc7943bc1b36b77b515b0371221703249ae')

    depends_on('pkgconfig', type='build')
    depends_on('cmake@3.10:', type='build')
    depends_on('petsc+mpi+hdf5')
    depends_on('petsc@3.14.0:3.14,3.15.1:3.15', when='@3.0.0-alpha4')
    depends_on('petsc@3.14.0:3.14,3.15.1:3.16', when='@3.0.0-alpha5')
    depends_on('hdf5@1.10:+mpi+fortran')
    depends_on('fftw+mpi')

    patch('CMakeDebugRelease.patch', when='@3.0.0-alpha4')

    variant('build_type', default='DebugRelease',
            description='The build type to build',
            values=('Debug', 'Release', 'DebugRelease'))

    def patch(self):
        filter_file(' -lz ', ' -lz ${FFTW_LIBS} ', 'CMakeLists.txt')

    def cmake_args(self):
        return [self.define('DAMASK_SOLVER', 'grid'),
                self.define('FFTW_LIBS', self.spec['fftw:mpi'].libs.link_flags)]

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def execute(self):
        with working_dir(self.build_directory):
            damask_grid = Executable('src/DAMASK_grid')
            damask_grid('--help')
