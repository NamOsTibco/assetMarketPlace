import clr
clr.AddReference('System.Data')
import System
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


dataSet = DataSet()
dataTable = DataTable("timelineEvents")
dataTable.Columns.Add("parentType", System.String)
dataTable.Columns.Add("parentId", System.String)
dataTable.Columns.Add("start", System.DateTime)
dataTable.Columns.Add("end", System.DateTime)
dataTable.Columns.Add("eventType", System.String)
dataTable.Columns.Add("desc", System.String)
dataTable.Columns.Add("singleEvent", System.String)
dataSet.Tables.Add(dataTable)


dt = dataTable.NewRow()
dt["parentType"] = "Case"
dt["parentId"] = "28081"
dt["start"] = "2017-08-28T15:47:01.572Z"
dt["end"] = "2017-08-28T15:47:01.572Z"
dt["eventType"] = "CASE_STARTER"
dt["desc"] = "Enter Customer Onboarding Data"
dt["singleEvent"] = "TRUE" 
dataTable.Rows.Add(dt)

textData = "parentType\tparentId\tstart\tend\teventType\tdesc\tsingleEvent\r\n"
for row in dataTable.Rows:
                textData +=  row["parentType"] + "\t" + str(row["parentId"]) + "\t" + str(row["start"]) + "\t" + str(row["end"]) + "\t" + str(row["eventType"]) + "\t" + str(row["desc"]) + "\t" + row["singleEvent"] + "\r\n"



print textData

stream = MemoryStream()
writer = StreamWriter(stream)
writer.Write(textData)
writer.Flush()
stream.Seek(0, SeekOrigin.Begin)

readerSettings = TextDataReaderSettings()
readerSettings.Separator = "\t"
readerSettings.AddColumnNameRow(0)
readerSettings.SetDataType(0, DataType.String)
readerSettings.SetDataType(1, DataType.String)
readerSettings.SetDataType(2, DataType.Date)
readerSettings.SetDataType(3, DataType.Date)
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