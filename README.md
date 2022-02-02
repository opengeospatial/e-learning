# E-Learning for OGC

## Introduction
This repository is used to share and plan E-Learning material related to OGC Standards.
The [wiki](https://github.com/opengeospatial/e-learning/wiki/Goal-and-Plan) provides more details.
The web page created from this material is available [here](http://opengeospatial.github.io/e-learning).

## Building the source

The source is build in rst format and available in GitHub: https://github.com/opengeospatial/e-learning

### Requirements
- To build it, [SPHINX] (http://sphinx-doc.org) is needed
- A [git client](https://git-scm.com) to clone the repository

### Process

   1. Clone the repository: git clone https://github.com/opengeospatial/e-learning.git
   2. Navigate to the e-learning folder with ```cd e-learning```
   3. Run ```make clean``` (optional, for clearing the previous built content)
   3. Run ```make ogc```
   4. Navigate to the build folder with ```cd build```
   5. Open the index.html file
