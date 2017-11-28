#Creates a BarChart visualization from a given datatable
from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Application.Visuals.Maps import *
from Spotfire.Dxp.Application.Layout import *

import clr

overviewPage = Document.Pages.AddNew()
overviewPage.Title = "Overview"

#gets a reference to the default data table
dataTable = Document.Data.Tables["GRMemberData-3"]
#dataTable = Document.Data.Tables.DefaultTableReference

#Creates a BarChart 
chartTop = overviewPage.Visuals.AddNew[BarChart]()

#Configure the BarChart 
chartTop.Data.DataTableReference = dataTable
chartTop.Title = "TOP 5 Regions"
chartTop.XAxis.Expression = "<[Region]>"
chartTop.YAxis.Expression = "UniqueCount([Id]) as [#Customers]"
chartTop.Legend.Visible = False
chartTop.Orientation = BarChartOrientation.Horizontal
chartTop.SortedBars = True
#print dir (chart)
#chartTop.XAxis.As(ScaleAxisBase).IndexedReversed = True
found = chartTop.TryGetFilterRules()
frc = clr.Reference[FilterRuleCollection]()
item = chartTop.TryGetFilterRules(frc)
#print frc.Value.Count

frc.AddTopNRule("UniqueCount([Id])", 5, False)


title = overviewPage.Visuals.AddNew[HtmlTextArea]()
title.Visual.ShowTitle = False
title.HtmlContent = '<TABLE style="HEIGHT: 100%" width="100%">'
title.HtmlContent += '<TBODY>'
title.HtmlContent += '<TR>'
title.HtmlContent += '	<TD align=center>'
title.HtmlContent += '		<FONT face="Trebuchet MS" size="6" color="#53585b"><b>Customer General Overview</b></FONT>'
title.HtmlContent += '</TD>'
title.HtmlContent += '</TR>'
title.HtmlContent += '</TBODY>'
title.HtmlContent += '</TABLE>'

kpiOne = overviewPage.Visuals.AddNew[HtmlTextArea]()
kpiOne.Visual.ShowTitle = False
kpiOne.HtmlContent = '<table width="100%" style="height: 100%;" align="center" cellpadding="10">'
kpiOne.HtmlContent += '<tbody>'
kpiOne.HtmlContent += '<tr>'
kpiOne.HtmlContent += '<td width="30%" align="center">'
kpiOne.HtmlContent += '		<font color="#660000" size="1"># Clients<br></font><font color="#40c0c0" size="2"><strong><font color="#26a2ed" size="6">8213</font></strong></font>'
kpiOne.HtmlContent += '</td>'
kpiOne.HtmlContent += '<td width="30%" align="center">'
kpiOne.HtmlContent += '	<font color="#660000" size="1"># Depenses totale moyenne<br></font><font color="#40c0c0" size="2"><strong><font color="#26a2ed" size="6">228,21 $</font></strong></font>'
kpiOne.HtmlContent += '</td>'
kpiOne.HtmlContent += '<td width="30%" align="center">'
kpiOne.HtmlContent += '	<font color="#660000" size="1"># Duree d adhesion moyenne<br></font><strong><font color="#26a2ed" size="6">76&nbsp;mois</font></strong></font>'
kpiOne.HtmlContent += '</td>'
kpiOne.HtmlContent += '</tr>'
kpiOne.HtmlContent += '</tbody></table>'



kpiTwo = overviewPage.Visuals.AddNew[HtmlTextArea]()
kpiTwo.Visual.ShowTitle = False
kpiTwo.HtmlContent = '<table width="100%" style="height: 100%;" align="center" cellpadding="10">'
kpiTwo.HtmlContent += '<tbody>'
kpiTwo.HtmlContent += '<tr>'
kpiTwo.HtmlContent += '<td width="30%" align="center">'
kpiTwo.HtmlContent += '		<font color="#660000" size="1"># Logins moyen<br></font><font color="#40c0c0" size="2"><strong><font color="#26a2ed" size="6">10</font></strong></font>'
kpiTwo.HtmlContent += '</td>'
kpiTwo.HtmlContent += '<td width="30%" align="center">'
kpiTwo.HtmlContent += '	<font color="#660000" size="1"># Jrs Derniere connexion<br></font><font color="#40c0c0" size="2"><strong><font color="#26a2ed" size="6">84</font></strong></font>'
kpiTwo.HtmlContent += '</td>'
kpiTwo.HtmlContent += '<td width="30%" align="center">'
kpiTwo.HtmlContent += '	<font color="#660000" size="1"># Taux d attribution<br></font><strong><font color="#26a2ed" size="6">31 %</font></strong></font>'
kpiTwo.HtmlContent += '</td>'
kpiTwo.HtmlContent += '</tr>'
kpiTwo.HtmlContent += '</tbody></table>'






#Creates a Chart 
pieChart = Application.Document.ActivePageReference.Visuals.AddNew[PieChart]()

#Configure the Chart 
pieChart.Data.DataTableReference = dataTable
pieChart.Title = "Gender Distribution"
pieChart.ColorAxis.Expression = "<[Gender]>"
pieChart.SectorSizeAxis.Expression = "UniqueCount([Id]) as [#Customers]"
pieChart.Legend.Visible = False
pieChart.VisualAttributes.LabelCategory=True
#pieChart.SortSectorsBySize = True


#Creates a Chart 
map = Application.Document.ActivePageReference.Visuals.AddNew(VisualTypeIdentifiers.MapChart2)
map.As[Maps.MapChart]().Layers.AddNewStandardTileLayer()
map= map.As[VisualContent]() #mymap is mapchart visual script param
map.AutoZoom=True
map.Legend.Visible = False
f=map.Layers.AddNewFeatureLayer(dataTable)
f[1].AutoConfigureLayerVisualization()
f[1].AutoConfigureGeocoding(True, True, True)
marker=map.Layers.AddNewMarkerLayer(dataTable)
marker[1].AutoConfigureLayerVisualization()
marker[1].AutoConfigureGeocoding(True, True, True)

layout = LayoutDefinition()
layout.BeginStackedSection()
layout.Add(title.Visual, 10)
layout.BeginSideBySideSection(20)
layout.Add(kpiOne.Visual, 50)
layout.Add(kpiTwo.Visual, 50)
layout.EndSection()
layout.BeginSideBySideSection(70)
layout.Add(chartTop.Visual, 25)
layout.Add(map.Visual, 50)
layout.Add(pieChart.Visual, 25)
layout.EndSection()
layout.EndSection()
overviewPage.ApplyLayout(layout)