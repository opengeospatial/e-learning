Using the SQLite Application
============================

Let's have a look at two example of GeoPackage files. Both files can be downloaded from `the ETS website <https://github.com/opengeospatial/ets-gpkg12/tree/master/src/test/resources/gpkg>`_. The files include:

* *states10.gpkg* which contains vector feature data of US states and their attributes
* *bluemarble.gpkg* which contains tile matrix sets of imagery.

To have a look at the structure of the files, download the files and open them using the basic SQLite3 command-line utility.

* on Windows SQLite3 has to be downloaded and installed from `here <https://sqlite.org/download.html>`_.
* on Ubuntu/Debian SQLite3 has to be installed using ``sudo apt-get install sqlite3`` or downloaded from `here <https://sqlite.org/download.html>`_.
* on Mac OS X, SQLite3 is pre-installed on newer versions and can be opened from the Terminal application  or downloaded from `here <https://sqlite.org/download.html>`_.

First run the following command ``sqlite3 states10.gpkg`` from the terminal to open the states10.gpkg GeoPackage.

Once the SQLite3 application is running, list the tables in the GeoPackage using the following command ``.tables``. Notice that the names of tables contained in the database are listed.

Now close the SQLite3 application by running the following command ``.quit``

Next, run the following command ``sqlite3 bluemarble.gpkg`` from the terminal to open the bluemarble.gpkg GeoPackage.

Once the SQLite3 application is running, list the tables in the GeoPackage using the following command ``.tables``. Notice that the tables are different from those that are in the states10.gpkg GeoPackage. This is because the states10.gpkg file contains vector features only, whereas the bluemarble.gpkg file contains tile matrix sets of imagery.

Now close the SQLite3 application by running the following command ``.quit``

A screenshot showing the steps and outputs is presented below.

.. image:: ../../img/sqlite3_list_tables.png
   :height: 327
   :width: 560


Most of the tables are optional and only required for specific types of datasets. That is why the bluemarble.gpkg database has some tables that are not in the states10.gpkg database.