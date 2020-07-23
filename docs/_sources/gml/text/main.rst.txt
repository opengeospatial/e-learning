GML - Introduction
=====================

Introduction
------------
The Geography Markup Language (GML) is a way of writing geographic information in Extensible Markup Language (XML) to facilitate the transport and storage of geographic information. It can be thought of as an XML grammar for the description of application schemas that describe the structure of concepts in a particular domain or given context.

Some of the key concepts used by GML to model the geographic phenomena include:

* Feature: abstraction of real world phenomena; it is a geographic feature if it is associated with a location relative to the Earth.
* Property: The state of a feature is defined by a set of properties, where each property may be thought of as a {name, type, value} triple.
* Feature collection: A collection of features, that may itself be regarded as a feature

The term feature can be used to refer to a type of feature or an instance of a feature. An example of a feature type is a 'River', whereas an example of a feature instance is the 'Hudson River'. For clarity, this section of the course will quality the term with either 'type' or 'instance' wherever possible.

One of the benefits of using GML is that the feature types can be described in an application schema, written in XML Schema Definition (XSD), that allows software to validate whether a document complies with the application schema. This reduces the risk of information loss when different software products exchange geospatial data. An XSD document that describes a GML application schema reuses geometries and other standardized concepts from official OGC GML schemas (see http://schemas.opengis.net).


Background
------------

History
  GML 1.0 was approved as an OGC standard in May 2000.
  GML 2.0 was approved as an OGC standard in February 2001.
  GML 3.0 was approved as an OGC standard in December 2002.
  GML 3.1.1 was approved as an OGC standard in February 2004.
  GML 3.2.1 was approved as an OGC standard in August 2007.
  GML 3.2.2 was approved as an OGC standard in December 2016.

Versions
  GML 3.3 builds on GML 3.2 and extends it with additional schema components and requirements.
Test Suite
  A test suite exist in the `OGC repository. <https://github.com/opengeospatial/ets-gml32>`_
Implementations
   Implementations can be found at the OGC database. `here <http://www.ogc.org/resource/products/byspec>`_


Usage
------------

GML is used for the exchange or storage of, amongst other uses:

* Vector feature data
* Coverage data
* Topologic complexes
* Coordinate reference systems
* Temporal reference systems
* Dictionaries

Example
------------

Like any other XML document, a GML document consists of a hierarchical arrangement of XML elements specified using tags. A tag in an XML can be identified by the '<' and '>' characters.  A tag is considered a start tag if it only consists of a name between the  '<' and '>' characters. A tag is considered an end tag if it begins with the characters '</'. A tag that has the '/>' characters as a suffix is considered a self-closing tag; such an tag does not require an end tag to define an element.

Here's an example element that has both a start tag and an end tag: <Name>New York</Name>

In the example above the start tag is <Name> and the end tag is </Name>

Here's an example of a self-closing tag <Name value=”New York”/>

GML allows for elements to be nested in other elements. That is, GML allows for elements to be contained inside other elements. The practice of placing objects inside other objects is known as nesting. For example, in the following listing the <gml:featureMember> element nests the <tiger:poi> element which in turn nests the <tiger:the_geom> element. Notice as well that  the <tiger:poi> element nests the <tiger:NAME> element.

.. code-block:: xml
  :linenos:


   <gml:featureMember xmlns:gml="http://www.opengis.net/gml" xmlns:tiger="http://www.census.gov">
   <tiger:poi gml:id="poi.1">
   <tiger:the_geom>
   <gml:Point srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2">
   <gml:pos>40.689167 -74.044444</gml:pos>
   </gml:Point>
   </tiger:the_geom>
   <tiger:NAME>Statue of Liberty</tiger:NAME>
   </tiger:poi>
   </gml:featureMember>

In the example above, the text xmlns:gml="http://www.opengis.net/gml" is a declaration that the namespace 'http://www.opengis.net/gml' shall be represented with the prefix 'gml' within the declaring element and its nested elements. This makes it possible to qualify a tag with the 'gml' prefix. Namespaces make it possible for applications to distinguish between elements that have the same name but have different types. Imagine for instance, two elements named 'poi', one referring to a person-of-interest and the other to a place-of-interest. An application reading the listing above would determine that the 'poi' element shown above is from the  namespace 'http://www.census.gov' and thus it describes a place-of-interest.

In the example above, the tiger:the_geom element represents a property of a feature. This property is formed of a GML Point geometry which is represented by the gml:Point element. Note that the star tag of this gml:Point element includes an srsName attribute. The value of the srsName attribute references the Coordinate Reference System (CRS) that applies to the coordinates of the GML Point. In this case the code “urn:ogc:def:crs:EPSG::4326” references the World Geodetic System 1984 (WGS84) datum as registered in the EPSG database (see http://www.epsg-registry.org/export.htm?gml=urn:ogc:def:crs:EPSG::4326). The srsDimension specifies the number of dimensions represented by the CRS and the positions in the GML Point.

The positions or coordinates of the GML Point are represented by the gml:pos element. Notice that there are only two numbers in this example, that is because this example declares in the srsDimension attribute that it uses two-dimensional coordinates. If the example included three-dimensional (3D) coordinates, then the srsDimension attribute would have had a value of 3 and there would have been three numbers in the gml:pos element. A typical use case for 3D coordinates is the representation of coordinates as latitude, longitude and elevation.

In the example above there is only one non-geometry property shown, namely the tiger:NAME element. Any number of properties can be included in an feature type, provided they are defined in an application schema that is used by the XML document.

Now let's consider a situation where we would like to represent a linear feature such as a road. The following listing presents an example of a linear feature.


.. code-block:: xml
  :linenos:

   <ogr:featureMember xmlns:ogr="http://ogr.maptools.org/" xmlns:gml="http://www.opengis.net/gml">
   <ogr:roads gml:id="roads.1">
   <ogr:geometryProperty>
   <gml:LineString srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2"><gml:posList>54.9906466 -2.5773558 54.9908714 -2.5767192 54.9909405 -2.5764712 54.9909618 -2.5764044 54.9909743 -2.5761903 54.9909482 -2.5760361 54.990899 -2.575843 54.9908284 -2.5757244 54.9905421 -2.5754333</gml:posList></gml:LineString>
   </ogr:geometryProperty>
   <ogr:osm_id>146830031</ogr:osm_id>
   <ogr:highway>residential</ogr:highway>
   <ogr:name>Hadrian's Crescent</ogr:name>
   </ogr:roads>
   </ogr:featureMember>


Notice that in the example above, the spatial property is called ogr:geometryProperty and that the property is formed of a gml:LineString geometry. The CRS is “urn:ogc:def:crs:EPSG::4326” as in the previous example and the positions along the LineString are presented as 2D coordinates. The example above has three non-geometry properties, namely ogr:osm_id,  ogr:highway and  ogr:name. The coordinates of the vertices of the line are presented by the gml:posList element as a space-delimited array of numbers.

In situations where we would like to represent an areal feature such as a soccer field, we use a geometry property called gml:Polygon. This type of geometry property nests a gml:exterior element, which in turn nests a gml:LinearRing geometry. Notice in the example below that the first coordinate in the gml:posList element is equivalent to the last coordinate in the same gml:posList. Notice as well that the coordinates are presented by the gml:posList element as a space-delimited array of numbers.

.. code-block:: xml
  :linenos:

  <ogr:featureMember xmlns:ogr="http://ogr.maptools.org/" xmlns:gml="http://www.opengis.net/gml">
  <ogr:landcover gml:id="landcover.1">
  <ogr:geometryProperty><gml:Polygon srsName="urn:ogc:def:crs:EPSG::4326" srsDimension="2"><gml:exterior><gml:LinearRing><gml:posList>51.556272 -0.2803943 51.5562758 -0.2787397 51.5556539 -0.278736 51.5556501 -0.2803906 51.556272 -0.2803943</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ogr:geometryProperty>
  <ogr:osm_id>116539074</ogr:osm_id>
  <ogr:layer>4</ogr:layer>
  <ogr:sport>soccer</ogr:sport>
  <ogr:leisure>pitch</ogr:leisure>
  <ogr:surface>grass</ogr:surface>
  <ogr:lit>yes</ogr:lit>
  <ogr:name>Wembley Stadium Soccer Field</ogr:name>
  </ogr:landcover>
  </ogr:featureMember>

Note that any hollow areas within this feature could be represented using gml:interior elements inside the gml:exterior element. In this case, it is a soccer pitch so it does not have any hollow areas!
