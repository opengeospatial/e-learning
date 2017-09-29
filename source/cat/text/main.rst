CSW
===

Introduction
------------
Catalogue services support the ability to publish and search collections of descriptive information (metadata) for data, services, and related information objects. Metadata in catalogues represent can be queried and presented for evaluation and further processing by both humans and software. Catalogue services are required to support the discovery and binding to registered information resources within an information community. 



History and Versions

  - CSW 2.0.2 `07-006r1  <http://portal.opengeospatial.org/files/?artifact_id=20555>`_ was released in 2007-02-23
  - CSW 3.0 (will be released in 2015-2016). It adds open search support.

Test suites exist for: 

      - `CSW 2.0.2 <https://github.com/opengeospatial/ets-csw202>`_ 
      - `CAT 3.0 <https://github.com/opengeospatial/ets-cat30>`_

Implementations can be found at the `OGC database <http://www.opengeospatial.org/resource/products/byspec>`_.

Usage
-----

Providers of resources (data and services), use catalogues to register metadata that conform to the provider’s choice of an information model.  Such models include descriptions of spatial references and thematic information. Client applications can then search for geospatial data and services in very efficient ways to discover services or data.

Usage examples:

-  `Technical Guidance to Implement INSPIRE Discovery Services <http://inspire.ec.europa.eu/documents/Network_Services/Technical_Guidance_Discovery_Services_v2.12.pdf>`_
- `GEOSS CSW <http://geossregistries.info/portaldeveloper.html>`_ 
- `Data.gov search via pycsw <https://gist.github.com/kalxas/5ab6237b4163b0fdc930>`_


Profiles
-----------

There are several profiles of OGC CSW. These include:

- `ISO 19115/19139 Metadata  <http://www.iso.org/iso/catalogue_detail.htm?csnumber=32557>`_ : This document specifies an application profile for ISO metadata with support for XML encoding per `ISO 19139 <http://www.iso.org/iso/catalogue_detail.htm?csnumber=32557>`_  and HTTP protocol binding. This CSW profile is widely implemented in Europe, such as in the Spatial Data Infrastructure for North Rhine Westphalia (federal state of Germany).
- `CSW-ebRIM Registry Service  <http://portal.opengeospatial.org/files/?artifact_id=31137>`_:  This profile applies the CSW interfaces to the OASIS ebXML registry information model (ebRIM 3.0) so as to provide a general and flexible web-based registry service that enables users—human or software agents—to locate, access, and make use of resources in an open, distributed system. It provides facilities for retrieving, storing, and managing many kinds of resource descriptions. An extension mechanism permits registry content to be tailored for more specialized application domains.
- CSW 39.50: The Z39.50 Protocol binding uses a message-based client server architecture implemented using the ANSI/NISO Z39.50 Application Service Definition and Protocol Specification. This protocol binding maps each of the general model operations to a corresponding service specified in the `ANSI/NISO/ISO standard  <http://lcweb.loc.gov/z3950/agency/document.html>`_. Much of the current work on this standard has to do with restructuring the catalogue standard so that there is a well defined, easy to implement core coupled with a well defined mechanism for expressing a variety of extensions (previously known as application profiles).

Relation to other OGC Standards
-------------------------------

Any implementation supporting any standard can be registered into a CSW registry. Usually the information retrieved from the GetCapabilities of services (e.g WFS, WMS) is most of the times harvested to populate or augment the description of the service record in the registry. The content model returned by the catalog is also based on a standard (e.g. ISO 19115.1939, Dublin Core or other)


Overview of CSW Operations
-----------------------

A CSW Server provides the following operations:

GetCapabilities
	Returns information about the server instance
DescribeRecord
	Returns the information models used by the server to return the metadata records
GetRecordById
	Retrieves the default representation of catalogue records using an identifier
GetRecords
	Searches for records given a set of criteria
GetDomain (Optional)
	Used to obtain the range of values of a metadata property
Harvest (Optional)
	Create/update metadata by asking the server to 'pull' metadata from somewhere  


Example
-------

Example of operations for  `PyCSW - CSW Data.gov <https://gist.github.com/kalxas/5ab6237b4163b0fdc930>`_

