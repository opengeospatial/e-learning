An Introduction to OGC API - Tiles
==================

Introduction
------------

The OGC API — Tiles standard defines building blocks for creating Web APIs that support the retrieval of geospatial information as tiles. Different forms of geospatial information are supported, such as tiles of vector features (“vector tiles”), coverages, maps (or imagery) and other types of geospatial information. Although it can be used independently, the OGC API — Tiles building blocks can be combined with other OGC API Standards and draft specifications for additional capabilities or increasing interoperability for specific types of data. The OGC API — Tiles standard references the OGC Two Dimensional Tile Matrix Set (TMS) and Tileset Metadata standard, which defines logical models and encodings for specifying tile matrix sets and describing tile sets. A tile matrix set is a tiling scheme that enables an application to partition and index space based on a set of regular grids defined for multiple scales in a Coordinate Reference System (CRS). 


.. note::  This tutorial module is not intended to be a replacement to the actual **OGC API - Tiles - Part 1: Core** standard. The tutorial intentionally focuses on a subset of capabilities in order to get the student started with using the standard. Please refer to the **OGC API - Tiles - Part 1: Core** standard for additional detail.


Background
--------------------

History
    The OGC API - Tiles standard is a successor to the OGC's Web Map Tile Service (WMTS) standard, focusing on simple reusable REST API building blocks which can be described using the OpenAPI specification. Whereas WMTS focused on map tiles, the OGC API — Tiles standard has been designed to support any form of tiled data.
Versions
    **OGC API - Tiles - Part 1: Core** version 1.0.0 is the current latest version
Test Suite
  Test suites are available for:
      - `OGC API - Tiles <https://github.com/opengeospatial/ets-ogcapi-tiles10>`_
Implementations
    Implementations can be found on the Compliance Database here <http://www.opengeospatial.org/resource/products/byspec>

Usage
^^^^^^

There are at least two ways to approach an implementation of the OGC API - Tiles Standard.

* Read the landing page, look for links, follow them and discover new links until the desired resource is found
* Read a Web API definition document that specifies a list of paths and path templates to resources.

Once you have discovered the relevant resources, then retrieve the list of available tiling schemes from the resource `.../{datasetRoot}/tileMatrixSets` to identify the tiling scheme of interest. Retrieve the details of the specific tiling scheme with `.../{datasetRoot}/tileMatrixSets/{tileMatrixSetId}.

Once you have identified a tiling scheme of interest, you can retrieve tile set metadata for that tiling scheme through `{datasetRoot}/tiles/{tileMatrixSetId}` and also retrieve individual tiles with `{datasetRoot}/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}`.

Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although the OGC API — Tiles Standard is designed as a building block that can be leveraged by (or with) other OGC API Standards adding precisions about specific types of data available as tiles (e.g., OGC API — Features standard, and OGC API — Maps and OGC API — Coverages candidate standards), the conformance classes defined in this Standard are still concrete enough to make it possible to support distributing and requesting various types of tiled data, including coverages, vector features and maps, by relying strictly on the content herein and in the OGC Two Dimensional Tile Matrix Set and Tile Set Metadata 2.0 standard.


Overview of Resources
----------------------------

**OGC API - Tiles - Part 1: Core** defines the resources listed in the following table.

======================================================================= ==========================================================================================================
**Resource name**                                                       **Common path**
======================================================================= ==========================================================================================================
Landing page                                                            {datasetRoot}/
Conformance declaration                                                 {datasetRoot}/conformance
Tiling Schemes                                                          {datasetRoot}/tileMatrixSets
Tiling Scheme (tile matrix set)                                         {datasetRoot}/tileMatrixSets/{tileMatrixSetId}
**Dataset Tiles**                                                      
*Dataset Feature Tiles*                                                
Dataset tileset list\ :sup:`1,2`                                        {datasetRoot}/tiles
Dataset tileset metadata\ :sup:`1,2` (in one tile matrix set\ :sup:`2`) {datasetRoot}/tiles/{tileMatrixSetId}
Dataset feature tile\ :sup:`1,3`                                        {datasetRoot}/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}
*Dataset Map tiles*                                                    
Map tileset list\ :sup:`2` (geospatial resources\ :sup:`1`)             {datasetRoot}/map/tiles
Map tileset metadata\ :sup:`2` (geospatial resources\ :sup:`1`)         {datasetRoot}/map/tiles/{tileMatrixSetId}
Map tile\ :sup:`1`                                                      {datasetRoot}/map/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}
**Geospatial data collections**\ :sup:`5`                              
Collections\ :sup:`5`                                                   {datasetRoot}/collections
Collection\ :sup:`5`                                                    {datasetRoot}/collections/{collectionId}
*Collection Feature Tiles*\ :sup:`3`                                   
Feature tileset list\ :sup:`2`                                          {datasetRoot}/collections/{collectionId}/tiles
Feature tileset metadata\ :sup:`2`                                      {datasetRoot}/collections/{collectionId}/tiles/{tileMatrixSetId}
Feature tile\ :sup:`3`                                                  {datasetRoot}/collections/{collectionId}/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}
*Collection Map tiles*                                                 
Map tileset list\ :sup:`2`                                              {datasetRoot}/collections/{collectionId}/map/tiles
Map tileset metadata\ :sup:`2`                                          {datasetRoot}/collections/{collectionId}/map/tiles/{tileMatrixSetId}
Map tile                                                                {datasetRoot}/collections/{collectionId}/map/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}
*Coverage tiles*                                                       
Coverage tileset list\ :sup:`2`                                         {datasetRoot}/collections/{collectionId}/coverage/tiles
Coverage tileset metadata\ :sup:`2`                                     {datasetRoot}/collections/{collectionId}/coverage/tiles/{tileMatrixSetId}
Coverage tile                                                           {datasetRoot}/collections/{collectionId}/coverage/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}
======================================================================= ==========================================================================================================


Example
-------

This `demonstration server <https://demo.ldproxy.net/zoomstack/>`_ publishes tiled feature data through an interface that conforms to OGC API - Tiles.

An example request that can be used to retrieve data, referenced to WebMercatorQuad, from the OS Zoomstack collection is https://demo.ldproxy.net/zoomstack/tiles/WebMercatorQuad/0/0/0?f=mvt

In this case the data is encoded in Mapbox Vector Tiles (MVT) format.

Once downloaded, a client application can then display or process the data.

.. image:: ../img/mvt_example.png
   :width: 40%
