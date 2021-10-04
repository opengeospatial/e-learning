Understanding OGC Standards
=============================

What is a standard?
------------------------

In the OGC context, a standard is an agreed specification of rules and guidelines about how to implement software interfaces and data encodings. Geospatial software vendors, developers and users collaborate in the OGC's consensus process to develop and agree on standards that enable information systems to exchange geospatial information and instructions for geoprocessing. OGC standards are open standards.

Open Standards
--------------

Organizations like the OGC, the IETF, the World Wide Web Consortium (W3C) and others are open organizations in the sense that any individual or organization can participate, the topics of debate are largely public, decisions are democratic (usually by consensus), and specifications are free and readily available. An “open” process is necessary to arrive at an “open” standard. The openness that OGC promotes is part of this general progress.

Often the terms “open standards” and “open source” are confused or incorrectly taken to mean the same thing. The OGC standards are specifications developed in an open process. Open source is software made freely available under a license that allows the program to run for any purpose, to study how the program works, to adapt it, and to redistribute copies, including modifications. As a matter of policy, the OGC Board of Directors and staff don’t favor either proprietary software or open source software. From the OGC perspective, any developer who implements OGC standards in software or online services is doing the right thing. OGC cares about interoperability – the ability to share geospatial information.

Open Standards - the definition
-------------------------------

The OGC defines Open Standards as standards that are:

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
