# Stem Cell Segmentation challenge resolver : StardistforCurie using 128-256 ray model using custom U-net


For overlapping cell segmentation using convex polygon approach developed by CSB Dresden for data generated at Institut Curie

[ORIGINAL CODE](https://github.com/mpicbg-csbd/stardist)

This package requires python3.5, so to enable Jupyter notebbok a selection between python 2 or 3.5 you have to do:


conda create -n tensorflowpy3pt5 pip python=3.5

pip install --ignore-installed --upgrade
(find the gpu supported python3.5 whl for kepler cluster )

conda install nb_conda

source activate tensorflowpy3pt5

After these commands the usual tensorflow import commands will run fine such as

import tensorflow as tf

import stardist as st

etc

Now you can start a jupyter kernel and select the tensorflowpy3pt5 kernel
