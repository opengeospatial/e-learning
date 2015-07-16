Introduction to OGC Standards
=============================

Definition of a standard
------------------------

A standard is a formal agreement that provides the rules and guidelines between suppliers and consumers about how to implement a technology. For example, the following image provides a fragment WMS 1.3 standard.

.. image:: ../img/standard-wms.jpg
      :width: 50%

The table specifies the parameters which are to be performed in a *GetMap* request. For example, the request must carry a *VERSION* parameter whose value must be *1.3.0*, and is mandatory. These parameters as discussed before translate into key value pairs in a HTTP GET request.

The following request is an HTTP GET request for a map of Gipuzkoa, a province of the Basque Country ::

	http://b5m.gipuzkoa.net/ogc/wms/gipuzkoa_wms?service=wms&
	version=1.3.0&
	request=getmap&
	layers=udal_barrutiak_limites_municipales
	&styles=
	&crs=epsg:23030&
	bbox=530000,4740000,610000,4820000
	&width=600&
	height=600&
	format=image/png   

OGC Services
------------

OGC Services follows the Service Oriented Architecture approach, using the publish/find/bind pattern for dynamic binding between service providers and in a distributed environment. 

.. image:: ../img/soa.jpg
      :width: 70%
      
   
As shown, there are three essential kinds of operations performed by services:

Publish
   used to register data and services to a broker (such as registry, catalog or clearinghouse). A service provider contacts the service broker to publish, update or unpublish a service. A service provider typically publishes service metadata describing its capabilities and network address.

Find 
	used by service consumers to discover specific service types or instances. Service consumers describe the kinds of services they're looking for to the broker and the broker responds by delivering the results that match the request. Service consumers typically use metadata published to find services of interest.

Bind 
	used when a service consumer invokes a service. A service consumer typically uses service metadata provided by the broker to bind to a service provider. The service consumers can either use a proxy generator to generate the code that can bind to the service, or can use the service description to implement the binding before accessing that service.


Types of Standards
------------------

Two types of standards can be depicted

Encoding standards 
	Rules that determine how to organize information, typically sent by a service provider or produced by an application. For example, a text file, binary or XML. An encoding can be based on a conceptual model. For example, rules exit to convert from  `UML <http://www.uml.org>`_ models to XML encodings, such as GML.

Interface Standards 
	Rules that determine the operations between service providers and service requesters. For example, an interface to request maps to a map service provider.

Encodings and services can be categorized as follows based on the purpose.

+-------------------+--------------+-----------+-+
| Purpose           | Encoding     | Interface | |
|                   | Standards    | Standards | |
+===================+==============+===========+=+
| find and locating | metadata     | catalog   | |
| data and services |              | services  | |
+-------------------+--------------+-----------+-+
| visualization     | image        | map       | |
|                   |              | services  | |
+-------------------+--------------+-----------+-+
| data access       | data models  | data      | |
|                   | and encoding | services  | |
+-------------------+--------------+-----------+-+

OWS Common
----------

The OGC Web Services Common `OWS Common <http://www.opengeospatial.org/standards/common>`_  provides specifics that are common to Interface Implementation Standards. Each interface standard details additional aspects, including specifying all additional parameters and data structures needed in all operation requests and responses. The following is a list of some common aspects covered by OWS Common:

* GetCapabilities operation (request, parameters, response)
* Exception reports
* Operations parameters
   * Bounding box
   * Coordinate reference systems
   * Format parameters
   * Data descriptions
   * Multilingual text encoding
* Operation request and response encoding (HTTP GET and HTTP POST)
* Guidance for OWS Implementation Specifications



