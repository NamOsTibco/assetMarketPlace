import clr
clr.AddReference ( "SpotfirePS.Framework.JSVisualization, Version=1.0.0.0, Culture=neutral, PublicKeyToken=4d233badaf236513" )
#
# Import the JS Visualization classes
#TODO clean unused import
from SpotfirePS.Framework.JSVisualization import *
from SpotfirePS.Framework.JSVisualization.Core import *
from SpotfirePS.Framework.JSVisualization.Common import *

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
url = baseUrl + "/externalLibs/jsviz/lib/JSViz/JSViz.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "visTimelineGraph2dCss"
url = baseUrl + "/externalLibs/visjs/vis-timeline-graph2d.min.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "visTimelineCss"
url = baseUrl + "/customLibs/visTimeline/visTimeline.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JVizIntrospectionJS"
url = baseUrl + "/externalLibs/jsviz/lib/JSViz/Introspection.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "visJS"
url = baseUrl + "/externalLibs/visjs/vis.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "JQuery"
url = baseUrl + "/externalLibs/jquery/jquery-3.2.1.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "Platform"
url = baseUrl + "/externalLibs/platform.js-master/platform.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference


# Create a Linked Content Item
name = "visNamos"
url = baseUrl + "/customLibs/visTimeline/namosVisTimelineGroup.js"
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



import clr
clr.AddReference('System.Data')
import System

# TODO clean unused imports

from System.Data import DataSet, DataTable, XmlReadMode
from Spotfire.Dxp.Data import DataType, DataTableSaveSettings
from System.IO import StringReader, StreamReader, StreamWriter, MemoryStream, SeekOrigin
from System.Threading import Thread
from Spotfire.Dxp.Data import IndexSet
from Spotfire.Dxp.Data import RowSelection
from Spotfire.Dxp.Data import DataValueCursor
from Spotfire.Dxp.Data import DataSelection
from Spotfire.Dxp.Data import DataPropertyClass
from Spotfire.Dxp.Data import Import
from System import DateTime
from System import DateTime, TimeSpan, DayOfWeek
from datetime import date
from System.Net import HttpWebRequest
import time
from Spotfire.Dxp.Data.Import import TextFileDataSource, TextDataReaderSettings

#
#
#Create Data source
#
#


clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer
from System.Net import WebClient

# Create a web client
client = WebClient()


# Download the results of that URL
results = client.DownloadString("http://localhost:8888/spotfireFramework/assetMarketPlace/customLibs/visTimeline/dxp/eventsGroup.csv")

# print these results
print results


stream = MemoryStream()
writer = StreamWriter(stream)
writer.Write(results)
writer.Flush()
stream.Seek(0, SeekOrigin.Begin)

readerSettings = TextDataReaderSettings()
readerSettings.Separator = ","
readerSettings.AddColumnNameRow(0)
readerSettings.SetDataType(0, DataType.String)
readerSettings.SetDataType(1, DataType.String)
readerSettings.SetDataType(2, DataType.DateTime)
readerSettings.SetDataType(3, DataType.DateTime)
readerSettings.SetDataType(4, DataType.String)
readerSettings.SetDataType(5, DataType.String)
readerSettings.SetDataType(6, DataType.String)

dSource = TextFileDataSource(stream, readerSettings)

if Document.Data.Tables.Contains("timelineEvents"):
                Document.Data.Tables["timelineEvents"].ReplaceData(dSource)
else:
                newTable = Document.Data.Tables.Add("timelineEvents", dSource)
                tableSettings = DataTableSaveSettings (newTable, False, False)
                Document.Data.SaveSettings.DataTableSettings.Add(tableSettings)
				
				
#
#
#Link Data Source
#
#TODO clean unused import
from Spotfire.Dxp.Data import DataManager

from Spotfire.Dxp.Data import PersistentDataView
from Spotfire.Dxp.Data import DataColumn
from Spotfire.Dxp.Data import DataType, DataColumnProperties
from System.Collections.Generic import List


# Empty the list of data configurations
jsviz.DataSettings.Clear ()
# Add a new data configuration
datatable = Document.Data.Tables["timelineEvents"]
datasettingname = jsviz.GetNextDataSettingName(
datatable.Name )
ds = DataSetting ( datasettingname )
ds.DataTable = datatable
ds.AutoConfigure ()
jsviz.DataSettings.Add ( ds )



# Set the Data Setting Name
ds.Name = "My timelineEvent"

# Set the Data Table
ds.DataTable = Document.Data.Tables["timelineEvents"]

# Set the Filtering Scheme
#datamanager = ds.Context.GetService[DataManager]()
#ds.Filtering = datamanager.Filterings.DefaultFilteringReference

# Clear the Limit data by list
#ds.LimitByMarkings.Clear ()
# Limit data by the Default Marking
#datamanager = ds.Context.GetService[DataManager]()
#defaultmarking = datamanager.Markings.DefaultMarkingReference
#mr = MarkingReference ( defaultmarking )
#ds.LimitByMarkings.Clear ()
#ds.LimitByMarkings.Add ( mr )


# Create a list of Group by columns
lstGroupByColumns = List[DataColumn]()


# Create a list of Column Expressions
lstColumnExpressions = List[str]()
lstColumnExpressions.Add ('[parentType]')
lstColumnExpressions.Add ('[parentId]')
lstColumnExpressions.Add ('[start]')
lstColumnExpressions.Add ('[end]')
lstColumnExpressions.Add ('[eventType]')
lstColumnExpressions.Add ('[desc]')
lstColumnExpressions.Add ('[singleEvent]')

# Create a new PersistentDataView object
vw1 = PersistentDataView ( "my view", lstColumnExpressions, lstGroupByColumns,ds.DataTable, ds.Filtering )
# Replace the current view with our new one
ds.View = vw1



