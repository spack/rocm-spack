FROM public.ecr.aws/amazonlinux/amazonlinux:2.0.20201111.0
MAINTAINER Spack Maintainers <maintainers@spack.io>

ENV DOCKERFILE_BASE=centos            \
    DOCKERFILE_DISTRO=centos          \
    DOCKERFILE_DISTRO_VERSION=7       \
    SPACK_ROOT=/opt/spack             \
    DEBIAN_FRONTEND=noninteractive    \
    CURRENTLY_BUILDING_DOCKER_IMAGE=1 \
    container=docker

RUN yum update -y \
 && yum groupinstall -y "Development Tools" \
 && yum install -y \
        curl \
        findutils \
        gcc-c++ \
        gcc \
        gcc-gfortran \
        git \
        gnupg2 \
        hostname \
        iproute \
        make \
        patch \
        python3 \
        python3-pip \
        python3-setuptools \
        tcl \
        unzip \
        which \
 && pip3 install boto3 \
 && rm -rf /var/cache/yum \
 && yum clean all

COPY bin   $SPACK_ROOT/bin
COPY etc   $SPACK_ROOT/etc
COPY lib   $SPACK_ROOT/lib
COPY share $SPACK_ROOT/share
COPY var   $SPACK_ROOT/var
RUN mkdir -p $SPACK_ROOT/opt/spack

RUN ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
          /usr/local/bin/docker-shell \
 && ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
          /usr/local/bin/interactive-shell \
 && ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
          /usr/local/bin/spack-env

RUN mkdir -p /root/.spack \
 && cp $SPACK_ROOT/share/spack/docker/modules.yaml \
        /root/.spack/modules.yaml \
 && rm -rf /root/*.* /run/nologin $SPACK_ROOT/.git

# [WORKAROUND]
# https://superuser.com/questions/1241548/
#     xubuntu-16-04-ttyname-failed-inappropriate-ioctl-for-device#1253889
RUN [ -f ~/.profile ]                                               \
 && sed -i 's/mesg n/( tty -s \\&\\& mesg n || true )/g' ~/.profile \
 || true

WORKDIR /root
SHELL ["docker-shell"]

# TODO: add a command to Spack that (re)creates the package cache
RUN spack spec hdf5+mpi

ENTRYPOINT ["/bin/bash", "/opt/spack/share/spack/docker/entrypoint.bash"]
CMD ["interactive-shell"]
