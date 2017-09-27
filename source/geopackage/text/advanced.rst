GeoPackage - Advanced
=====================

Introduction
------------

There are several different ways to create and read a GeoPackage. Most of the implementing software products have their own unique way of supporting the handling of a GeoPackage. In this chapter we will show how a GeoPackage can be read using the free and open source GeoPackage Java library that can be found `here <https://github.com/ngageoint/geopackage-java>`_ .

For ease of reference, we reproduce the GeoPackage schema overview below.

.. image:: ../img/geopackage-overview.png
   :height: 327
   :width: 560

The ``gpkg_spatial_ref_sys`` table contains coordinate reference system definitions that are used to reference vector and tile data in user tables to locations on the earth.

The ``gpkg_contents`` table provides a list of all geospatial contents in a GeoPackage to allow applications to identify and describe geospatial data that is available for access and/or update.

The ``gpkg_geometry_columns`` table specifies the type of geometry supported by user data tables containing features.

The ``gpkg_tile_matrix_set`` table provides records identifying each tile pyramid user data table contained in the GeoPackage.

The ``gpkg_tile_matrix`` table documents the structure of the tile matrix at each zoom level in each tiles table.

The ``gpkg_extensions`` table or updateable view in a GeoPackage is used to indicate that a particular extension applies to a GeoPackage, a table in a GeoPackage, or a column of a table in a GeoPackage.

The ``gpkg_data_columns`` table stores a minimal description of the schema of feature and tile matrix data tables that supplements the data available from the SQLite sqlite_master table and pragma table_info(table_name) SQL function.

The ``gpkg_data_column_constraints`` table contains data to specify restrictions on basic data type column values.

The ``gpkg_metadata`` table allows for metadata to be stored inside the GeoPackage.

The ``gpkg_metadata_reference`` table relates metadata records stored in the gpkg_metadata to feature and tile data stored in the GeoPackage.

Why does GeoPackage have these tables?
-------------------------------------

The GeoPackage standard implements the OGC OpenGIS® Simple Features Interface Standard (SFS) which provides a common way for applications to store and access feature data in relational or object-relational databases. The specific tables that play a key role in this are the ``gpkg_geometry_columns`` , ``gpkg_spatial_ref_sys``, ``gpkg_contents`` and a user-named table that contains the feature properties. Use of the SFS by GeoPackage allows implementations of the GeoPackage standard to make use of the large number of spatial reference systems available from registers such as the `EPSG Geodetic Parameter Registry  <https://www.epsg-registry.org/>`_. Use of the SFS by GeoPackage also makes GeoPackages interoperable with other formats that use the SFS, for example the OGC Geography Markup Language (GML). This means that data can be exchanged between a GeoPackage and other SFS-based formats with minimal or no information loss because the data models are based on a common feature model.

The GeoPackage standard adopts a tile-based pyramid structure for storing imagery and raster maps at multiple resolutions. An illustration of this structure is shown below. The specific tables that play a key role in storage of such data include ``gpkg_tile_matrix_set`` , ``gpkg_tile_matrix`` , ``gpkg_contents`` and a user-named table that contains the actual binary encoded tiles. This tile-based pyramid structure is particularly useful when handling a GeoPackage on small or constrained devices such as mobile phones, tablets or laptops because an appropriate resolution can be selected based on the zoom level and the device screen size.

.. image:: ../img/pyramid.png
   :height: 327
   :width: 560

Using the NGA GeoPackage Java library
-------------------------------------

The open source NGA GeoPackage Java library has been designed to closely abstract the tables of a GeoPackage. The library offers a Data Access Object (DAO) for each of the core tables found in a GeoPackage.

Features and tiles can be accessed from the DAO instances and queried to extract metadata or feature properties. The following code block presents an annotated example of a program that reads two separate GeoPackages, one containing vector features and another containing tiles of imagery. The source code has been adapted from the `GeoPackage Java library website <https://github.com/ngageoint/geopackage-java>`_ . Note that the example uses the states10.gpkg and bluemarble.gpkg sample files. Both files can be downloaded from `here <https://demo.luciad.com/GeoPackageData/>`_ .

.. code-block:: java


      package org.opengeospatial.GeoPackageDemo;

      import java.io.File;
      import java.util.List;
      import mil.nga.geopackage.GeoPackage;
      import mil.nga.geopackage.core.contents.ContentsDao;
      import mil.nga.geopackage.core.srs.SpatialReferenceSystemDao;
      import mil.nga.geopackage.extension.ExtensionsDao;
      import mil.nga.geopackage.features.columns.GeometryColumnsDao;
      import mil.nga.geopackage.features.user.FeatureDao;
      import mil.nga.geopackage.features.user.FeatureResultSet;
      import mil.nga.geopackage.features.user.FeatureRow;
      import mil.nga.geopackage.geom.GeoPackageGeometryData;
      import mil.nga.geopackage.io.GeoPackageTextOutput;
      import mil.nga.geopackage.manager.GeoPackageManager;
      import mil.nga.geopackage.metadata.MetadataDao;
      import mil.nga.geopackage.metadata.reference.MetadataReferenceDao;
      import mil.nga.geopackage.schema.columns.DataColumnsDao;
      import mil.nga.geopackage.schema.constraints.DataColumnConstraintsDao;
      import mil.nga.geopackage.tiles.matrix.TileMatrixDao;
      import mil.nga.geopackage.tiles.matrixset.TileMatrixSetDao;
      import mil.nga.geopackage.tiles.user.TileDao;
      import mil.nga.geopackage.tiles.user.TileResultSet;
      import mil.nga.geopackage.tiles.user.TileRow;
      import mil.nga.wkb.geom.Geometry;

      /**
       * GeoPackage demonstration
       *
       */
      public class App {

        /**
        * This method reads a GeoPackage file and prints out the contents to the console
        */
      	public void read(File geopackageFile) {

      		// Open a GeoPackage and create an handle to it
      		GeoPackage geoPackage = GeoPackageManager.open(geopackageFile);

      		// Create DAO instances of GeoPackage tables
      		SpatialReferenceSystemDao srsDao = geoPackage.getSpatialReferenceSystemDao(); //accesses gpkg_spatial_ref_sys
      		ContentsDao contentsDao = geoPackage.getContentsDao();   //accesses gpkg_contents
      		GeometryColumnsDao geomColumnsDao = geoPackage.getGeometryColumnsDao();  //accesses gpkg_geometry_columns
      		TileMatrixSetDao tileMatrixSetDao = geoPackage.getTileMatrixSetDao();  //accesses gpkg_tile_matrix_set
      		TileMatrixDao tileMatrixDao = geoPackage.getTileMatrixDao();   //accesses gpkg_tile_matrix
      		DataColumnsDao dataColumnsDao = geoPackage.getDataColumnsDao();  //accesses gpkg_data_columns
      		DataColumnConstraintsDao dataColumnConstraintsDao = geoPackage.getDataColumnConstraintsDao(); //accesses gpkg_data_columns_constraints
      		MetadataDao metadataDao = geoPackage.getMetadataDao(); //accesses gpkg_metadata
      		MetadataReferenceDao metadataReferenceDao = geoPackage.getMetadataReferenceDao();  //accesses gpkg_metadata_reference
      		ExtensionsDao extensionsDao = geoPackage.getExtensionsDao(); //accesses gpkg_extensions

      		// Feature and tile tables
      		List<String> features = geoPackage.getFeatureTables();
      		List<String> tiles = geoPackage.getTileTables();

      		// If there are any features print their properties (as represented by column names and values)
      		if (features.size() > 0) {
      			FeatureDao featureDao = geoPackage.getFeatureDao(features.get(0));
      			FeatureResultSet featureResultSet = featureDao.queryForAll();
      			try {
      				while (featureResultSet.moveToNext()) {
      					FeatureRow featureRow = featureResultSet.getRow();
      					String[] columnNames = featureRow.getColumnNames();
      					for(String columnName: columnNames)
      					{
      						if(featureRow.getColumn(columnName).isGeometry())
      							System.out.println(featureRow.getGeometry().toString());
      						else
      							System.out.println(featureRow.getColumn(columnName).getName()+"="+featureRow.getValue(columnName));
      					}


      				}
      			} finally {
      				featureResultSet.close();
      			}

      		}

      		// If there are any tiles in the GeoPackage, then print out information about the tile tables
      		if (tiles.size() > 0) {

      			TileDao tileDao = geoPackage.getTileDao(tiles.get(0));
      			TileResultSet tileResultSet = tileDao.queryForAll();

      			//Now print out descriptions of the tiles
      			StringBuilder output = new StringBuilder();
      			GeoPackageTextOutput textOutput = new GeoPackageTextOutput(
      					geoPackage);
      			output.append("\n\n");
      			output.append(textOutput.header());
      			output.append("\n\n");
      			output.append(textOutput.tileTable(geoPackage.getTileTables().get(0)));
      			System.out.println(output);
      		}

      		// Close the database when done
          System.out.println("Done!");
      		geoPackage.close();

      	}

      	/*
      	 * This is the main method. It creates an array of two GeoPackage files, one consisting of vector feature data and another consisting of imagery tile data.
      	 */
      	public static void main(String[] args) {

      		//Create an array of two GeoPackage files.
      		File[] existingGeoPackages = new File[2];
      		existingGeoPackages[0] = new File("/Users/Shared/states10.gpkg");
      		existingGeoPackages[1] = new File("/Users/Shared/bluemarble.gpkg");

      		//Pass each of the files in the array to the read() method for reading
      		App app = new App();
      		for(File existingGeoPackage: existingGeoPackages){
      			app.read(existingGeoPackage);
      		}

      	}

      }

When the program runs it prints out the feature and tile datasets, including feature properties and tile matrix descriptions.

To run this program, create a Maven project and add the following dependency to the configuration file of the Maven project. This will allow the library dependencies to be pulled in from the Maven Central Repository. A quick start guide for creating a Maven project can be found `here <https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html>`_.

.. code-block:: xml


      <dependency>
          <groupId>mil.nga.geopackage</groupId>
          <artifactId>geopackage</artifactId>
          <version>1.3.1</version>
      </dependency>



Using the GDAL/OGR library
-------------------------------------

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
