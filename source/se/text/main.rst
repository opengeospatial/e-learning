Symbology Encoding
==================

Geospatial data (vector and raster) have no intrinsic visual component. In order to see data, it must be styled. Styling specifies color, thickness, and other visible attributes used to render data on a map. The Symbology Encoding (SE) standard defines the language to formally encode the rules of how to portray features and coverages.

Encoding a style for a feature
------------------------------


The following code provides an example of how to encode a style for a feature

.. code-block:: xml
   :linenos:
	
      <?xml version="1.0" encoding="ISO-8859-1"?>
      <FeatureTypeStyle version="1.1.0" 
              xsi:schemaLocation="http://www.opengis.net/se FeatureStyle.xsd"
              xmlns="http://www.opengis.net/se" 
              xmlns:ogc="http://www.opengis.net/ogc"
              xmlns:xlink="http://www.w3.org/1999/xlink" 
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xmlns:oceansea="http://www.myurl.net/oceansea">
          <FeatureTypeName>oceansea:Foundation</FeatureTypeName>
          <Rule>
              <Name>main</Name>
              <PolygonSymbolizer uom="http://www.opengeospatial.org/sld/units/pixel">
                  <Fill>
                      <SvgParameter name="fill">#96C3F5</SvgParameter>
                  </Fill>
              </PolygonSymbolizer>
          </Rule>
      </FeatureTypeStyle>  

Explanation:

- **line 9** provides the name of the feature type. Note that the name has a base URL (http://www.myurl.net/oceansea) and a local name (Foundation) 

- **line 12-16** provide the details of how to portray the line of the polygon, which is color 96C3F5 (light blue)


The following is another example, with version 1.0.0 and provide the details of how to portray a circle (size and fill color) 

.. code-block:: xml
      
         
      <?xml version="1.0" encoding="ISO-8859-1"?>
      <StyledLayerDescriptor version="1.0.0"
          xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
          xmlns="http://www.opengis.net/sld"
          xmlns:ogc="http://www.opengis.net/ogc"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <NamedLayer>
              <Name>Simple point</Name>
              <UserStyle>
                  <Title>GeoServer SLD Cook Book: Simple point</Title>
                  <FeatureTypeStyle>
                      <Rule>
                          <PointSymbolizer>
                              <Graphic>
                                  <Mark>
                                      <WellKnownName>circle</WellKnownName>
                                      <Fill>
                                          <CssParameter name="fill">#FF0000</CssParameter>
                                      </Fill>
                                  </Mark>
                                  <Size>6</Size>
                              </Graphic>
                          </PointSymbolizer>
                      </Rule>
                  </FeatureTypeStyle>
              </UserStyle>
          </NamedLayer>
      </StyledLayerDescriptor>

