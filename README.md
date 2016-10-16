# riverhack
Aim: Produce a real-time updated flood warning map of the UK National Cycle Network.

Using: QGIS 2.8.6

Data available at https://hackpad.com/Our-Water-Quality-Hack-Data-94hn6S1RNLb

Cycle route data came from OpenStreetMap. An overpass-turbo.eu query extracts the aggregated National Cycle Network and Local Cycle Network trails, each with their own numbering scheme. Focus solely on the NCN routes, typically longer and more vulnerable to adverse conditions.

A PyQGIS script extracts the route number reference from each segment in the NCN. Each segment ("way") has an associated string of route information in JSON, which is parsed with a python library. In QGIS, add a blank attribute called 'ncnref' to the cycle route layer with Processing > Toolbox > Add Field to Attributes Table. Run "getattrs.py" while the cycle network layer is selected to populate this new attribute's column. (Some strings are malformatted due to being truncated, and are ignored.) With the route numbers available, use a QGIS filter query to partition the cycle network by route number (note that ncnref is a string, not an integer). Routes 5, 51, and 57 pass through Oxford.

The flood warning area boundaries shape file came from Simon Redding. The UK Environment Agency publishes flood warnings, information on which can be found at http://environment.data.gov.uk/flood-monitoring/doc/reference

Using QGIS, clip the cycle path segments to isolate those passing through a flood warning area. The operation Vector > Geoprocessing Tools > Clip will successfully identify those segments, however will not include any identifying information of which flood warning areas they overlap. Instead, perform a spatial join with Processing > Toolbox > Join Attributes by Location. This will clip those segments of the map that lie within flood warning areas, and transfer the flood warning area attributes to the new segment. Those NCN segments not passing through flood warning areas are isolated with the operation Vector > Geoprocessing Tools > Difference.

Thanks to Simon and MT for help aggregating the necessary data.
Thanks to Luis for the QGIS help, and for the conversion to resolve initial problems due to different coordinate systems used by the datasets (Cycle network WGS84, flood warning areas OSGB 1936 (Ordnance Survey National Grid)).
