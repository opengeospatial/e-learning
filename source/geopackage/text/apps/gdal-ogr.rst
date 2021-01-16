Using the GDAL/OGR library
==========================

There are alternative ways of accessing a GeoPackage, including through use of other prorgamming languages and libraries. One of the software libraries that offers this ability is the free and open source Geospatial Data Abstraction Layer (GDAL) and its vector toolkit, OGR. GDAL offers C, C++ and Python bindings that allow it to be imported into a variety of applications.

To build and install GDAL on Windows, Linux or Mac OS X, the source code can downloaded from `here <http://www.gdal.org/usergroup0.html>`_.

For a quick start, GDAL 1.11 is also installed during the installation of QGIS.

An example Python script for reading a GeoPackage using GDAL 1.11 is below. The source code has been adapted from `here <http://gdal.org/1.11/ogr/ogr_apitut.html>`_. When the program runs it prints out the values of feature properties.


.. code-block:: python


      import sys
      import ogr
      # First open a handle on the GeoPackage.
      ds = ogr.Open( "/home/ogckm/Downloads/states10.gpkg" )
      # If the file handle is null then exit
      if ds is None:
          print "Open failed.\n"
          sys.exit( 1 )
      # Select the dataset to retrieve from the GeoPackage and assign it to an layer instance called lyr.
      # The names of available datasets can be found in the gpkg_contents table.
      lyr = ds.GetLayerByName( "statesQGIS" )
      # Refresh the reader
      lyr.ResetReading()
      # for each feature in the layer, print the feature properties
      for feat in lyr:

          feat_defn = lyr.GetLayerDefn()
          # for each non-geometry feature property, print its value
          for i in range(feat_defn.GetFieldCount()):
              field_defn = feat_defn.GetFieldDefn(i)

              if field_defn.GetType() == ogr.OFTInteger:
                  print "%d" % feat.GetFieldAsInteger(i)
              elif field_defn.GetType() == ogr.OFTReal:
                  print "%.3f" % feat.GetFieldAsDouble(i)
              elif field_defn.GetType() == ogr.OFTString:
                  print "%s" % feat.GetFieldAsString(i)
              else:
                  print "%s" % feat.GetFieldAsString(i)
          # Confirm whether there is a geometry property
          geom = feat.GetGeometryRef()
          if geom is not None and geom.GetGeometryType() == ogr.wkbMultiPolygon:
              print "has a geometry property"
          print "\n"

      ds = None

Note that GDAL 2.0 uses a different set of classes for accessing vector data. We have used GDAL 1.11 in this example because it is currently included by default in Linux repositories and also comes bundled within QGIS.
