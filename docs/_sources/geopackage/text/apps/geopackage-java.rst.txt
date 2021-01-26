The geopackage-java Library
==========================

There are several different ways to create and read a GeoPackage. Most of the implementing software products have their own unique way of supporting the handling of a GeoPackage. In this chapter we will show how a GeoPackage can be read using the free and open source GeoPackage Java library that can be found `here <https://github.com/ngageoint/geopackage-java>`_ . This library has been designed to closely abstract the tables of a GeoPackage. The library offers a Data Access Object (DAO) for each of the core tables found in a GeoPackage.

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

