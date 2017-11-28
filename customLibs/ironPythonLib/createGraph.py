import clr
clr.AddReference ( "SpotfirePS.Framework.JSVisualization, Version=1.0.0.0, Culture=neutral, PublicKeyToken=4d233badaf236513" )
#
# Import the JS Visualization classes
#
from SpotfirePS.Framework.JSVisualization import *
from SpotfirePS.Framework.JSVisualization.Core import *

#
# Import Spotfire objects required for manipulating Data Settings
#
from Spotfire.Dxp.Data import PersistentDataView
from Spotfire.Dxp.Data import DataColumn

# Baseurl when using locally
#baseUrl="http://localhost:8888/spotfireFramework/assetMarketPlace"

# Baseurl when using from cloud
baseUrl="https://s3-eu-west-1.amazonaws.com/asset-market-place-sources"

newPage = Document.Pages.AddNew()
newPage.Title = "Graph"

jsviz = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
jsviz.AutoConfigure()



jsviz.Title = "Graph"
jsviz.Visual.ShowTitle = True
jsviz.LegendVisible = False

# Create a new Content Repository (if needed)
cr = Document.CustomNodes.AddNewIfNeeded[ContentRepository]()


# Create a Linked Content Item
name = "JSVIZ"
url = baseUrl + "/externalLibs/jsviz/lib/JSViz/JSViz.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JVizIntrospectionJS"
url = baseUrl + "/externalLibs/jsviz/lib/JSViz/Introspection.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "NamOsCytoscapeJS"
url = baseUrl + "/customLibs/cytoscape/namosCytoscape.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JQuery"
url = baseUrl + "/externalLibs/jquery/jquery-3.2.1.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "CytoscapeMin"
url = baseUrl + "/externalLibs/cytoscape.js-master/dist/cytoscape.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "NamosCytoscapeCss"
url = baseUrl + "/customLibs/cytoscape/namosCytoscape.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

#============INCLUSIONS
# Add a Content Item to the Inclusion List
name = "JQuery"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "NamosCytoscapeCss"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "CytoscapeMin"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "NamOsCytoscapeJS"
jsviz.UrlInclusions.Add ( name )


# Add a Content Item to the Inclusion List
name = "JSVIZ"
jsviz.UrlInclusions.Add ( name )

