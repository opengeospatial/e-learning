WCS - Operations
================

This section provides detailed information about the types of operations that a WFS server offers. The list includes operations offered by different configurations (formally referred to as conformance classes) of WFS servers.

.. list-table:: WCS Operations
   :widths: 30 80
   :header-rows: 1

   * - **Operation**
     - **Description**
   * - ``GetCapabilities``
     - Retrieves metadata about the service, including supported operations and parameters, and a list of the available coverages.
   * - ``DescribeCoverage``
     - Returns a description of the coverage offered or accepted by an instance of a WCS.
   * - ``GetCoverage``
     - Returns a selection of coverage instances from a data store published through the WCS.


The following are examples of requests that can be sent to operations offered by a WCS.


GetCapabilities
-------------

This example uses a demonstration server that implements the WCS standard. In this example, the requests are issued by a WCS Client application to invoke operations on a WCS server.

First the client application needs to find out what coverages are offered by the WCS, so the client application issues a **GetCapabilities** request.

The following table defines some of the parameters allowed in a WCS **GetCapabilities** KVP request. 

======================= ============== ==========================================================================================================================================================================================================
**Parameter**           **Mandatory** **Description**

                        **Optional**
======================= ============== ==========================================================================================================================================================================================================
REQUEST=GetCapabilities Mandatory      This parameter identifies the operation that is to be invoked by the request. 
SERVICE=WCS             Mandatory      This parameter is used to indicate which of the available service types, at a particular server, is being invoked. When invoking a web feature service, the value of the service parameter shall be "WCS".
VERSION                 Optional       This is used to indicate to which version of the WCS specification the request encoding conforms.
======================= ============== ==========================================================================================================================================================================================================

 

An example **GetCapabilities** request that can be used to identify the coverages that are available from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcapabilities

The names and identifiers of the available coverages are obtained from the capabilities document that is returned by the **GetCapabilities** response. Notice as well that the capabilities document identifies the image formats that are supported by the service.

DescribeCoverage
-------------

Having identified the available coverages, the next step in the interaction between a WCS client and server would be to retrieve a description of a coverage. This is achieved by invoking the **DescribeCoverage** operation.

The following table defines the parameters that are allowed in a **DescribeCoverage** KVP request.

======================== ============== ==========================================================================================================================================================================================================
**Parameter**            **Mandatory** **Description**

                         **Optional**
======================== ============== ==========================================================================================================================================================================================================
REQUEST=DescribeCoverage Mandatory      This parameter identifies the operation that is to be invoked by the request. 
SERVICE=WCS              Mandatory      This parameter is used to indicate which of the available service types, at a particular server, is being invoked. When invoking a web feature service, the value of the service parameter shall be "WCS".
VERSION                  Mandatory      This is used to indicate to which version of the WCS specification the request encoding conforms.
EXTENSION                Optional       Any ancillary information to be sent from the client to the server

 
COVERAGEID               Mandatory      The identifier of the coverage that is to be described in the response.
======================== ============== ==========================================================================================================================================================================================================

 

An example **DescribeCoverage** request is shown below. Note that the response is a CoverageDescription XML document. This file would inform the client application about the structure of the coverage, for example dimensions if the coverage is gridded.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=DescribeCoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB

GetCoverage
-------------

Having identified what coverage data is available, the next step in the interaction between a WCS client and server would be to retrieve the coverage data. This is achieved by invoking the **GetCoverage** operation.

The following table defines the parameters allowed in a WCS **GetCoverage** KVP request. 

=================== ============== ==========================================================================================================================================================================================================
**Parameter**       **Mandatory/** **Description**

                    **Optional**
=================== ============== ==========================================================================================================================================================================================================
REQUEST=GetCoverage Mandatory      This parameter identifies the operation that is to be invoked by the request. 
SERVICE=WCS         Mandatory      This parameter is used to indicate which of the available service types, at a particular server, is being invoked. When invoking a web feature service, the value of the service parameter shall be "WCS".
VERSION             Mandatory      This is used to indicate to which version of the WCS specification the request encoding conforms.
EXTENSION           Optional       Any ancillary information to be sent from the client to the server

 
COVERAGEID          Mandatory      The identifier of the coverage that is to be described in the response.
FORMAT              Optional       MIME type identifier of the format in which the coverage returned is encoded.
MEDIATYPE           Optional       If present, enforces a multi-part encoding.
DIMENSIONSUBSET     Optional       Subsetting specifications, one per subsetting dimension.
=================== ============== ==========================================================================================================================================================================================================

 

 An example **GetCoverage** request that can be used to retrieve data from the service is shown below.

http://ows.eox.at/cite/mapserver?service=wcs&version=2.0.1&request=getcoverage&coverageid=MER_FRS_1PNUPA20090701_124435_000005122080_00224_38354_6861_RGB

The **GetCoverage** request queries the server with a set of parameters describing the data to return. 

The data returned in the **GetCoverage** response can be rendered by a desktop Geographic Information System (GIS) or forwarded to an OGC Web Map Service (WMS) for rendering. Alternatively, it can be forwarded to an OGC Web Processing Service (WPS) for further processing.
