SE - Introduction
=================

Introduction
------------

Geospatial data (vector and raster) have no intrinsic visual component. In order to see data, it must be styled. Styling specifies color, thickness, and other visible attributes used to render data on a map. The Symbology Encoding (SE) standard defines the language to formally encode the rules of how to portray features and coverages.

History

  SE 1.1.0 was approved as a standard in July 2006.
  Previous use of symbology encoding was through version 1.0.0  of the Styled Layer Descriptor (SLD) standard. To allow parts that are not specific to SLD and Web Map Services (WMS) to be reused, SLD 1.0.0 was split up into the separate standards of SE 1.1.0 and SLD 1.1.0.

Versions

  1.1.0 is the current latest version

Test Suite

  There is currently no test suite available for this standard.

Implementations

  Implementations can be found at the `OGC implementation database <http://www.opengeospatial.org/resource/products/byspec>`_


Usage
-----

SE can be used through web services such as WMS. It can also be used independently of any web service. SE is used for styling the following map data:

  * Feature data
  * Coverage data

Relation to other OGC Standards
-------------------------------

SE can be used within an SLD. In fact the two standards originated from the same specification and although now separate, are kept consistent.

Both SE and SLD can be used together to instruct a WMS on how it should render a layer.

For styling and rendering three-dimensional (3D) visualizations, the OGC Keyhole Markup Language (KML) and City Geography Markup Language (CityGML) standards are more appropriate.

Example
-------


The following code provides an example of how to use SE 1.1.0 to style polygon features. The example wraps SE 1.1.0 content (identifiable in the example through the "se:" namespace prefix) inside SLD 1.1.0 content (identifiable through the "sld:" namespace prefix). Note that the SE namespace is <http://www.opengis.net/se> and the SLD namespace is <http://www.opengis.net/sld>.

.. code-block:: xml
   :linenos:

      <?xml version="1.0" encoding="ISO-8859-1"?>
      <sld:StyledLayerDescriptor version="1.1.0" xsi:schemaLocation="http://www.opengis.net/sld
      StyledLayerDescriptor.xsd" xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
      xmlns:se="http://www.opengis.net/se" xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <sld:NamedLayer>
       <se:Name>se_test_polygon</se:Name>
       <sld:UserStyle>
       <sld:IsDefault>1</sld:IsDefault>
       <se:FeatureTypeStyle>
       <se:Rule>
       <se:Name>main</se:Name>
       <se:PolygonSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
       <se:Geometry>
       <ogc:PropertyName>the_geom</ogc:PropertyName>
       </se:Geometry>
       <se:Fill>
       <se:SvgParameter name="fill">#0000FF</se:SvgParameter>
       </se:Fill>
       </se:PolygonSymbolizer>
       </se:Rule>
       </se:FeatureTypeStyle>
       </sld:UserStyle>
      </sld:NamedLayer>
      </sld:StyledLayerDescriptor>



Explanation:

- **line 13-20** provide the details of how to portray the polygon, that is with a blue fill color (#0000FF)
- **line 15** provides the name of the geometry attribute to apply the ``PolygonSymbolizer`` styling to.

Importing the example SLD/SE document above into a local instance of GeoServer and calling a GetMap request of the `tasmania_state_boudaries  <http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.3.0&request=GetMap&layers=topp:tasmania_state_boundaries&styles=se_test_polygon&bbox=-43.648056,143.83482400000003,-39.573891,148.47914100000003&width=768&height=673&srs=EPSG:4326&format=application/openlayers>`_ layer that references the SLD/SE document renders the layer as shown below.

.. image:: ../img/tasmania_state_boundaries_blue_2.png
   :height: 327
   :width: 560

The following is another example, with version 1.0.0. It provides the details of how to portray a star (size and fill color). Note that at version 1.0.0 the FeatureTypeStyle and its nested elements used the SLD namespace <http://www.opengis.net/sld>, in this example with an "sld:" namespace prefix.

.. code-block:: xml

      <?xml version="1.0" encoding="ISO-8859-1"?>
      <sld:StyledLayerDescriptor version="1.0.0"
          xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
          xmlns:sld="http://www.opengis.net/sld"
          xmlns:ogc="http://www.opengis.net/ogc"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <sld:NamedLayer>
              <sld:Name>Point star</sld:Name>
              <sld:UserStyle>
                  <sld:Title>Star symbol</sld:Title>
                  <sld:FeatureTypeStyle>
                      <sld:Rule>
                          <sld:PointSymbolizer>
                              <sld:Graphic>
                                  <sld:Mark>
                                      <sld:WellKnownName>star</sld:WellKnownName>
                                      <sld:Fill>
                                          <sld:CssParameter name="fill">#0000FF</sld:CssParameter>
                                      </sld:Fill>
                                  </sld:Mark>
                                  <sld:Size>10</sld:Size>
                              </sld:Graphic>
                          </sld:PointSymbolizer>
                      </sld:Rule>
                  </sld:FeatureTypeStyle>
              </sld:UserStyle>
          </sld:NamedLayer>
      </sld:StyledLayerDescriptor>


Resources
---------
- `GeoServer SLD Cookbook <http://docs.geoserver.org/stable/en/user/styling/sld/cookbook/>`_
- `Creative Commons 3.0 <http://creativecommons.org/licenses/by/3.0/>`_
