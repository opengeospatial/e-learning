WMTS - Introduction
======================

Introduction
--------------------
The OGC `Web Map Tile Service Implementation Standard (WMTS) <http://www.opengeospatial.org/standards/wmts>`_ defines a set of interfaces for making web-based requests of map tiles of spatially referenced data using tile images with predefined content, extent, and resolution.

WMTS complements the OGC `Web Map Service interface standard (WMS) <http://www.opengeospatial.org/standards/wms>`_ for the web based distribution of cartographic maps. While WMS focuses on rendering custom maps and is an ideal solution for dynamic data or custom styled maps, particularly when combined with the OGC `Styled Layer Descriptor (SLD) standard <http://www.opengeospatial.org/standards/sld>`_, WMTS trades the flexibility of custom map rendering for the scalability made possible by serving static data (base maps) where the bounding box and scales have been constrained to discrete tiles. The fixed set of tiles allows for the implementation of a WMTS service using a web server that simply returns existing files. The fixed set of tiles also enables the use of standard network mechanisms for scalability such as distributed cache systems.


Example GetTile Request
--------------------------------------

TBD : Provide an example with a GetTle request against the reference implementation server

