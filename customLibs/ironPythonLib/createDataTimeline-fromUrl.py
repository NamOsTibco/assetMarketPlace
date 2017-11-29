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
