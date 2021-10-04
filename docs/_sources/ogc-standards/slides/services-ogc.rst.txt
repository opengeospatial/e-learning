Introduction to OGC Standards
=============================

What is a standard?
-------------------
- A **document**, established by **consensus** and **approved** by the OGC
  Membership, that provides rules and guidelines, aimed at the optimum degree
  of interoperability in a given context.
- Conveys:
   - Community requirements
   - Member requirements
   - Market trends
   - Technology trends

Open standards
------------------

1. **Freely and publicly available** – They are available free of charge and unencumbered by patents and other intellectual property.
2. **Non discriminatory** – They are available to anyone, any organization, any time, anywhere with no restrictions.
3. **No license fees** - There are no charges at any time for their use.
4. **Vendor neutral** - They are vendor neutral in terms of their content and implementation concept and do not favor any vendor over another.
5. **Data neutral** – The standards are independent of any data storage model or format.
6. **Based on Consensus** - They are defined, documented, and approved by a formal, member driven consensus process. The consensus group remains in charge of changes and no single entity controls the standard.

Standards list
-------------------------
http://www.opengeospatial.org/standards

.. image:: ../img/standards.jpg
   :width: 80%

Example of a rule in a standard
-------------------------------


For example, the following image provides a fragment of the OGC Web Map Service Interface Standard (WMS 1.3).

.. image:: ../img/standard-wms.jpg
   :width: 80%

Example of a rule in a standard
-------------------------------


.. image:: ../img/table8partwms.jpg 
   :width: 80%


- The table specifies the parameters that are to be performed in a GetMap request. 
- For example, the request must carry a *VERSION* parameter whose value must be *1.3.0*, and this is mandatory. 
- These parameters/values are the key/value pairs in an HTTP GET request.

Example of a rule in a standard
-------------------------------

The following request is an HTTP GET request for a map of Gipuzkoa, a province of the Basque Country based on the WMS standard rules

.. code-block:: properties

	http://b5m.gipuzkoa.net/ogc/wms/gipuzkoa_wms?service=wms&
	version=1.3.0&
	request=getmap&
	layers=udal_barrutiak_limites_municipales&
	styles=&
	crs=epsg:23030&
	bbox=530000,4740000,610000,4820000&
	width=600&
	height=600&
	format=image/png   

OGC services
------------

 .. OGC services are any software services that implement OGC interface standards. OGC services follows the Service Oriented Architecture (SOA) approach, using the publish/find/bind pattern for dynamic binding between service and clients and in a distributed environment. 

.. image:: ../img/soa.jpg
      :width: 80%




Types of standards
------------------


- Encodings - formats (e.g. KML, GML)
- Services - Defines operations (e.g. WFS, WMS)
- Common - (OWS Common)
- Libraries (e.g. GeoAPI)

Standards by purpose
---------------------

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

Type of OGC specifications 
----------------------
Implementation Specifications - Standards
   Basis for working software; detail the interface structure between software components
Abstract Specifications
   Conceptual foundation / reference model for specification development
Best Practices
   Describe use of specifications
Engineering Reports
   Results from the OGC Interoperability Program
Discussion Papers
   Forum for public review of concepts

Open Standard vs Open Source
--------------------------------------------------

- An "Open Standard" is not the same as "Open Source". 
- Open Standards are 
   - not software 
   - **rules** that software can implement
- "Open Source" refers to "Free and Open Source **Software**", 
   - which has been made available under a free software license  with the rights to run the program for any purpose, 
   - to study how the program works, to adapt it, and to redistribute copies, including modifications. 

