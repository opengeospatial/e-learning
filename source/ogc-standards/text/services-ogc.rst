Introduction to OGC Standards
=============================

Definition of a Standard
------------------------

In the OGC context, a standard is an agreed specification of rules and guidelines about how to implement software interfaces and data encodings. Geospatial software vendors, developers and users collaborate in the OGC's consensus process to develop and agree on standards that enable information systems to exchange geospatial information and instructions for geoprocessing. OGC standards are open standards. 

Open Standards
------------------

The OGC defines Open standards as standards that are:

1. Freely and publicly available – They are available free of charge and unencumbered by patents and other intellectual property.
2. Non discriminatory – They are available to anyone, any organization, any time, anywhere with no restrictions.
3. No license fees - There are no charges at any time for their use.
4. Vendor neutral - They are vendor neutral in terms of their content and implementation concept and do not favor any vendor over another.
5. Data neutral – The standards are independent of any data storage model or format.
6. Based on Consensus - They are defined, documented, and approved by a formal, member driven consensus process. The consensus group remains in charge of changes and no single entity controls the standard.


An "Open Standard" is not the same as "Open Source". "Open Source" refers to "Free and Open Source Software", which has been made available under a free software license with the rights to run the program for any purpose, to study how the program works, to adapt it, and to redistribute copies, including modifications. These freedoms enable Open Source software development, a public, collaborative model that promotes early publishing and frequent releases. Most open source software products implement open standards, such as OGC standards. Some are also reference implementations of OGC. A reference implementation is an example of correct implementation of a standard, for use by developers that is free and publicly available for testing via a web service or download.




Example of a rule in a standard
-----------------------------------


For example, the following image provides a fragment of the OGC Web Map Service Interface Standard (WMS 1.3).

.. image:: ../img/standard-wms.jpg
   :width: 80%

The table specifies the parameters that are to be performed in a GetMap request. For example, the request must carry a *VERSION* parameter whose value must be *1.3.0*, and this is mandatory. These parameters as discussed above translate into key value pairs in a HTTP GET request.

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

OGC services are any software services that implement OGC interface standards. OGC services follows the Service Oriented Architecture (SOA) approach, using the publish/find/bind pattern for dynamic binding between service and clients and in a distributed environment. 

.. image:: ../img/soa.jpg
      :width: 80%
      
   
As shown, there are three essential kinds of operations performed by services:

**Publish operations** register data and services to a broker (such as registry, catalog or clearinghouse). A service provider contacts the service broker to publish, update or unpublish a service. A service provider typically publishes service metadata describing its capabilities and network address.

**Find operations**, used by service consumers (clients), access service brokers to discover specific service types or instances. Service consumers describe to a broker the kinds of services they are looking for. The broker responds by delivering the results that match the request. Service consumers typically use metadata about services stored by the broker to find services of interest.

**Bind operations** are used by service consumers (clients) when invoking a service. A service consumer typically uses service metadata provided by the broker to bind to a service provider. The service consumers can either use a proxy generator to generate the code that can bind to the service, or they can use the service description to implement the binding before accessing that service.


Types of Standards
------------------


**Encoding standards** provide rules that determine how to organize information, typically sent by a service provider or produced by an application. An encoding standard might specify how to organize information encoded in, for example a text file, binary or  XML. An encoding standard is often based on a conceptual model, and a conceptual model can be implemented in different kinds of encodings. The OGC Abstract Specification is a set of conceptual models. Conceptual models are often visualized using the Unified Modeling Language (UML).

**Interface Standards** provide rules that determine the operations between service providers and service requesters. For example, an interface to request maps to a map service provider.

Encodings and services can be categorized as follows based on the purpose.

+-------------------+--------------+-----------+
| Purpose           | Encoding     | Interface |
|                   | Standards    | Standards |
+===================+==============+===========+
| find and location | metadata     | catalog   |
| of data           |              | services  |
+-------------------+--------------+-----------+
| visualization     | image        | map       |
|                   |              | services  |
+-------------------+--------------+-----------+
| data access       | data models  | data      |
|                   | and encoding | services  |
+-------------------+--------------+-----------+

OWS Common
----------

The OGC Web Services Common `(OWS Common) <http://www.opengeospatial.org/standards/common>`_  provides guidance to OGC members who are developing OGC interface implementation standards. The purpose of OWS Common is to maintain consistency among OGC standards. OWS Common provides rules for specifying some of the parameters and data structures used in operation requests and responses. Each interface standard details additional aspects, including specifying all additional parameters and data structures needed in all operation requests and responses. The following is a list of some common aspects covered by OWS Common document:

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



