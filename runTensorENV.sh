#!/bin/bash

# added by Anaconda2 installer
export PATH="/data/u934/service_imagerie/v_kapoor/anaconda2/bin:$PATH"

export FIJI_HOME=/data/u934/service_imagerie/v_kapoor/Fiji.app  # Replace with the path to your Fiji installationnnnnnn
export  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/u934/service_imagerie/v_kapoor/anaconda2/envs/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/u934/service_imagerie/v_kapoor/cuda/lib64/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/u934/service_imagerie/v_kapoor/Fiji.app/lib/linux64/

cd /data/u934/service_imagerie/v_kapoor/anaconda2/bin

#conda create -n tensorflowpy3pt5 pip python=3.5
#pip install --ignore-installed --upgrade (python3.5 version with GPU whl) 
source activate tensorflowpy3pt5

