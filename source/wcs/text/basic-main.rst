WCS - Introduction
==================

Introduction
------------
The OGC Web Coverage Service (WCS) supports electronic retrieval of geospatial data as “coverages.” Coverages are digital geospatial information representing space/time-varying phenomena, specifically spatio-temporal regular and irregular grids, point clouds, and general meshes. WCS offer the means to retrieve or query geographic coverages in a manner independent of the format in which the data is stored.



Background
--------------------

History

- WCS 2.0.0 was approved in October 2010
- WCS 2.0.1 was approved in July 2012
- WCS 2.1 was approved in June 2018

Versions

- 2.1 is the current latest version

Test Suite
  Test suites are available for:
      - `WCS 2.0 <https://github.com/opengeospatial/ets-wcs20>
Implementations
    Implementations can be found at the OGC database. here <http://www.opengeospatial.org/resource/products/byspec>


Relation to other OGC Standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- OGC Web Map Service Interface Standard (WMS): The WMS standard is more appropriate where a rendered map is required rather than the source vector data.
- OGC Web Map Tile Service Interface Standard (WMTS): The WMTS standard is a better fit where static rendered maps are required by highly scalable systems that issue many simultaneous requests.
- OGC Geography Markup Language (GML): This standard is used by WFS as the default encoding format for published data.

Usage of WCS
--------------------
The WCS standard enables access to coverages of any number of dimensions across a network. The standard uses a common vocabulary for coverage descriptions. The coverages can be retrieved in their native format or in a variety of formats, provided that the formats are supported by the WCS implementation.

The benefit of this is that WCS clients can request source data from multiple WCS servers, and then render the data for display on the client or process the data further as part of a workflow. The standard enables the data can be handled consistently with other data using a common geospatial coordinate reference system.

For coverage data such as satellite imagery, meteorological temperature forecasts, and similar raster data, it is most appropriate to use a WCS as the means of publishing the content on a network. Many products that implement the WCS standard support the publishing of images, sourced from flat-files, in formats such as GeoTIFF. Some of the products also support the publishing of images that are sourced from relational databases. In short, WCS is a good solution when you need to publish raw raster data or any other type of coverage dataset.


Overview of WCS Operations
--------------------
WCS is organized into a Core specification and a number of Extensions and Application Profiles. WCS Core specifies the following operations as mandatory and thus required to be supported by all servers:

* GetCapabilities: This operation allows a client to request information about the server’s capabilities and coverages offered.
* DescribeCoverage: This operation allows a client to request detailed metadata that describes selected coverages offered by a server.
* GetCoverage: This operation allows a client to request a coverage comprised of selected range properties at a selected set of spatio-temporal locations, expedited in some coverage encoding format.
Each extension or application profile may introduce additional operations to support a specific need in a community of interest.

Example Requests
----------------------------

An example **GetCapabilities** request that can be used to identify the coverages that are available from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcapabilities

An example **DescribeCoverage** request is shown below. Note that the response is a CoverageDescription XML document. This file would inform the client application about the structure of the coverage, for example dimensions if the coverage is gridded.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=DescribeCoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB

An example **GetCoverage** request that can be used to retrieve data from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB
