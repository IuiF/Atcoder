#!/bin/bash

# Update the package list and upgrade the packages
sudo apt update && sudo apt upgrade -y

# Install curl
sudo apt install curl -y

# Install zsh and oh-my-zsh
sudo apt install zsh -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
cp .zshrc ~/

# Install gcc-9 and g++-9
sudo apt install gcc-9 g++-9 -y

# Install python3.11
sudo apt install python3.11 -y

# Install pypy
sudo apt install pypy -y

# Install pip and Packages
sudo apt install python3-pip -y
pip install --upgrade pip
pip install -r requirements.txt

# Install git and tree
sudo apt install git -y
sudo apt install tree -y

# Install AtCoder Libraries and other utilities
git clone https://github.com/atcoder/ac-library.git /lib/ac-library
pip install git+https://github.com/hinamimi/ac-library-python
pip install git+https://github.com/hinamimi/python-sortedcontainers

# CPLUS_INCLUDE_PATH
echo 'export CPLUS_INCLUDE_PATH=/lib/ac-library' >> ~/.zshrc

# Install nodejs and npm
sudo apt install nodejs -y
sudo apt install npm -y

# Install contest support applications
pip install online-judge-tools==11.5.1
npm install -g atcoder-cli@2.2.0

# setup applications
acc config default-task-choice all
cd `acc config-dir`
mkdir python
    cd python
    touch template.json
    touch main.py
    echo '{
"task":{
    "program": ["main.py"],
    "submit": "main.py"
    }
}' > template.json
acc config default-template python
