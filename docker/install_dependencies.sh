#!/bin/bash

set -euxo pipefail

apt-get update
apt update
apt install --no-install-recommends \
  vim \
  git \
  openssh-client \
  libopenni-dev \
  apt-utils \
  python-pip \
  python-dev \

apt-get install \
  libgtk2.0-dev \
  libsm6 \
  libxrender1 \
  libfontconfig1 \
  python-tk

pip install --upgrade pip==9.0.3
pip install -U setuptools

apt-get -y install ipython ipython-notebook libglib2.0-0
pip install \
  numpy \
  jupyter \
  opencv-python \
  scipy \
  pandas \
  torch==1.0.0 \
  torchvision \
  matplotlib  \
  scikit-image
