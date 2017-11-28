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

newPage = Document.Pages.AddNew()
newPage.Title = "New Page"

jsviz = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
jsviz.AutoConfigure()



jsviz.Title = "MyTitle"
jsviz.Visual.ShowTitle = True
jsviz.LegendVisible = False

# Create a new Content Repository (if needed)
cr = Document.CustomNodes.AddNewIfNeeded[ContentRepository]()


# Create a Linked Content Item
name = "JSVIZ"
url = "http://localhost:8888/spotfireFramework/externalLibs/jsviz/lib/JSViz/JSViz.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "visTimelineGraph2dCss"
url = "http://localhost:8888/spotfireFramework/externalLibs/visjs/vis-timeline-graph2d.min.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "visTimelineCss"
url = "http://localhost:8888/spotfireFramework/customLibs/visTimeline/visTimeline.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JVizIntrospectionJS"
url = "http://localhost:8888/spotfireFramework/externalLibs/jsviz/lib/JSViz/Introspection.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "visJS"
url = "http://localhost:8888/spotfireFramework/externalLibs/visjs/vis.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JQuery"
url = "http://localhost:8888/spotfireFramework/externalLibs/jquery/jquery-3.2.1.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "Platform"
url = "http://localhost:8888/spotfireFramework/externalLibs/platform.js-master/platform.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "visNamos"
url = "http://localhost:8888/spotfireFramework/customLibs/visTimeline/namosVisTimelineGroup.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

#============INCLUSIONS
# Add a Content Item to the Inclusion List
name = "JQuery"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Platform"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "visJS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "visNamos"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "visTimelineCss"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "visTimelineGraph2dCss"
jsviz.UrlInclusions.Add ( name )

