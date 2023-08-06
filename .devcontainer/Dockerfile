
# Base image
FROM ubuntu:22.04

# Non-interactive mode and timezone
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

# User setup
ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${GROUPNAME} && \
    useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

# Basic utilities
RUN apt-get update && \
    apt-get install -y zsh time tzdata tree git curl

# Install compilers and interpreters
RUN apt-get update && \
    apt-get install -y gcc-9 g++-9 python3.11 python3-pip pypy3 nodejs npm

# Set alternatives
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 30 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 30 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.11 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30 && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 30

# Install Python libraries from requirements.txt
COPY requirements.txt /tmp/
RUN pip install -U pip && \
    pip install -r /tmp/requirements.txt

# Install AtCoder Libraries and other utilities
RUN git clone https://github.com/atcoder/ac-library.git /lib/ac-library
ENV CPLUS_INCLUDE_PATH /lib/ac-library
RUN pip install git+https://github.com/hinamimi/ac-library-python && \
    pip install git+https://github.com/hinamimi/python-sortedcontainers

# Install contest support applications
RUN pip install online-judge-tools==11.5.1
RUN npm install -g atcoder-cli@2.2.0

# Install Rust for AHC
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH $PATH:/home/root/.cargo/bin

# Set default shell to Z shell
SHELL ["/bin/zsh", "-c"]
CMD ["/bin/zsh"]
