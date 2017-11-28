from Spotfire.Dxp.Application.Visuals import BarChart
from Spotfire.Dxp.Data import DataTable, DataManager

newPage = Document.Pages.AddNew()
newPage.Title = "New Page"
myDataTable = Document.Data.Tables["World Bank Data"]

chart = newPage.Visuals.AddNew[BarChart]()
chart.Title = "Test Bar Chart1"
chart.XAxis.Expression = "[Country Name]"
chart.Data.DataTableReference = myDataTable
chart.YAxis.Expression = "ValueForMax([Year],[Population])"
chart.Legend.Visible = False
