import json
layer = qgis.utils.iface.activeLayer()
f = layer.getFeatures(QgsFeatureRequest(0))
caps = layer.dataProvider().capabilities()

# Check whether we can modify the attribute table
if not caps & QgsVectorDataProvider.ChangeAttributeValues:
   exit 

# Get the column index by the field name string
i_reltags = layer.fieldNameIndex(u'F_relation')
i_ncnref = layer.fieldNameIndex(u'ncnref')

# Traverse the attribute table row by row, extracting the NCN route number when applicable
for f in layer.getFeatures():
    try:
        j = json.loads(f.attributes()[i_reltags])
    except:
        print "json conversion failure"
        continue
    reltags = j[0]["reltags"]
    if (reltags["network"] == 'ncn'):
        attrs = { i_ncnref : reltags["ref"] }
        layer.dataProvider().changeAttributeValues({ f.id() : attrs })
        print f.attributes()[i_ncnref]

