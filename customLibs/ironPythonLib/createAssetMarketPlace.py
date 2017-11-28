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
baseUrl="https://s3-eu-west-1.amazonaws.com/asset-market-place-sources/assetMarketPlace"


newPage = Document.Pages.AddNew()
newPage.Title = "AssetMarketPlace"

jsviz = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
jsviz.AutoConfigure()



jsviz.Title = "AssetMarketPlace"
jsviz.Visual.ShowTitle = True
jsviz.LegendVisible = False

# Create a new Content Repository (if needed)
cr = Document.CustomNodes.AddNewIfNeeded[ContentRepository]()





# Create a Linked Content Item
name = "Asset Controller"
url = baseUrl + "/customLibs/NamOsMarketPlace/assetController.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "NamosMarketPlace HTML"
url = baseUrl + "/customLibs/NamOsMarketPlace/namos-rotating-card.html"
urlReference = UrlReference ( name, url, None, ContentType.HTML,False )
cr[name]= urlReference

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
name = "Bootstrap CSS"
url = baseUrl + "/bootstrap/bootstrap.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Angular"
url = baseUrl + "/externalLibs/angular/1.1.1/angular.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Namos Rotating Card CSS"
url = baseUrl + "/customLibs/NamOsMarketPlace/namos-rotating-card.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Bootstrap"
url = baseUrl + "/externalLibs/bootstrap/bootstrap.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "JQuery 3.2.1"
url = baseUrl + "/externalLibs/jquery/jquery-3.2.1.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Platform"
url = baseUrl + "/externalLibs/platform.js-master/platform.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "namosMarketPlace"
url = baseUrl + "/customLibs/NamOsMarketPlace/namosMarketPlace.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Bootstrap 3 CSS"
url = baseUrl + "/externalLibs/bootstrap/v3.0.2/bootstrap.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference


#============INCLUSIONS
# Add a Content Item to the Inclusion List
name = "JQuery 3.2.1"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Namos Rotating Card CSS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Bootstrap"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Angular"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Asset Controller"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "namosMarketPlace"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "NamosMarketPlace HTML"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Bootstrap 3 CSS"
jsviz.UrlInclusions.Add ( name )
