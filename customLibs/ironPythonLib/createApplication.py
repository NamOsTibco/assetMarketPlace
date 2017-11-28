import clr
clr.AddReference ( "SpotfirePS.Framework.JSVisualization, Version=1.0.0.0, Culture=neutral, PublicKeyToken=4d233badaf236513" )
#
# Import the JS Visualization classes
#
from SpotfirePS.Framework.JSVisualization import *
from SpotfirePS.Framework.JSVisualization.Core import *

from Spotfire.Dxp.Application.Visuals import *

from Spotfire.Dxp.Application.Layout import *

#
# Import Spotfire objects required for manipulating Data Settings
#
from Spotfire.Dxp.Data import PersistentDataView
from Spotfire.Dxp.Data import DataColumn



#
# PAGE INTRO ====================================================================================
#

introPage = Document.Pages.AddNew()
introPage.Title = "Introduction"

jsviz = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
jsviz.AutoConfigure()



jsviz.Title = "Dash board presentation"
jsviz.Visual.ShowTitle = True
jsviz.LegendVisible = False

# Create a new Content Repository (if needed)
cr = Document.CustomNodes.AddNewIfNeeded[ContentRepository]()


# Create a Linked Content Item
name = "Application index HTML"
url = "http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/application/applicationIndexSpotfire.html"
urlReference = UrlReference ( name, url, None, ContentType.HTML,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "Bootstrap CSS"
url = "http://localhost:8888/spotfireFramework/externalLibs/bootstrap/bootstrap.css"
urlReference = UrlReference ( name, url, None, ContentType.CSS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "JSVIZ"
url = "http://localhost:8888/spotfireFramework/externalLibs/jsviz/lib/JSViz/JSViz.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "JQuery"
url = "http://localhost:8888/spotfireFramework/externalLibs/jquery/jquery-3.2.1.min.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

# Create a Linked Content Item
name = "JVizIntrospectionJS"
url = "http://localhost:8888/spotfireFramework/externalLibs/jsviz/lib/JSViz/Introspection.js"
urlReference = UrlReference ( name, url, None, ContentType.JS,False )
cr[name]= urlReference

#============INCLUSIONS
# Add a Content Item to the Inclusion List
name = "Application index HTML"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "Bootstrap CSS"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JQuery"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
jsviz.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
jsviz.UrlInclusions.Add ( name )







#
# PAGE 1 ====================================================================================
#


newPage = Document.Pages.AddNew()
newPage.Title = "Page 1"

Document.ActivePageReference=newPage

content = Document.ActivePageReference.Visuals.AddNew[BarChart]()
content.Title="Replace with your content"
content.AutoConfigure()

details = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
details.Title="Details"
details.HtmlContent =    '   <style>  \r\n   	.textAreaTitle {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 28px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	.textAreaContent {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 14px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	body {  \r\n   		margin : 0px !important;  \r\n   	}  \r\n     \r\n   </style>  \r\n     \r\n   <TABLE style="HEIGHT:100%" border="0"  cellspacing="0" cellpadding="0" width="100%">  \r\n      <TBODY style="background-color:#868e96">  \r\n   		<!-- TOP IMAGE -->  \r\n         <TR style="height:10%">  \r\n            <TD align="center" colspan="4">  \r\n   			<img width="100%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/application/images/summary1.jpg" alt="">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	  <tr style="height:20px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- SECTION ONE -->  \r\n   	  <TR class="textAreaTitle">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   			<img width="60%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/images/externalIcon/earth.png" alt="">  \r\n   		 </TD>  \r\n   		 <TD width="40%">  \r\n   			Title 1  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	  <TR class="textAreaContent">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="60%" colspan="2">  \r\n   			My text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy text  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- DOWN SPACER -->  \r\n   	  <tr style="height:90%">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n      </TBODY>  \r\n  </TABLE>  ' 
details.Visual.ShowTitle = False

# Menu

menu = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
menu.AutoConfigure()

menu.Title="menu"
menu.Visual.ShowTitle = False

# Create a Linked Content Item
name = "Application Menu HTML"
url = "http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/application/applicationMenu.html"
urlReference = UrlReference ( name, url, None, ContentType.HTML,False )
cr[name]= urlReference

# Add a Content Item to the Inclusion List
name = "Application Menu HTML"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JQuery"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
menu.UrlInclusions.Add ( name )


layout = LayoutDefinition()
layout.BeginStackedSection()
layout.Add(menu.Visual, 9)
layout.BeginSideBySideSection(91)
layout.Add(details.Visual, 30)
layout.Add(content.Visual, 70)
layout.EndSection()
layout.EndSection()
newPage.ApplyLayout(layout)

#
# PAGE 2 ====================================================================================
#


newPage = Document.Pages.AddNew()
newPage.Title = "Page 2"

Document.ActivePageReference=newPage

content = Document.ActivePageReference.Visuals.AddNew[HeatMap]()
content.Title="Replace with your content"
content.AutoConfigure()

details = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
details.Title="Details"
details.HtmlContent =  '   <style>  \r\n   	.textAreaTitle {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 28px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	.textAreaContent {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 14px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	body {  \r\n   		margin : 0px !important;  \r\n   	}  \r\n     \r\n   </style>  \r\n     \r\n   <TABLE style="HEIGHT:100%" border="0"  cellspacing="0" cellpadding="0" width="100%">  \r\n      <TBODY style="background-color:#868e96">  \r\n   		<!-- TOP IMAGE -->  \r\n         <TR style="height:10%">  \r\n            <TD align="center" colspan="4">  \r\n   			<img width="100%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/application/images/summary1.jpg" alt="">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	  <tr style="height:20px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- SECTION ONE -->  \r\n   	  <TR class="textAreaTitle">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   			<img width="60%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/images/externalIcon/earth.png" alt="">  \r\n   		 </TD>  \r\n   		 <TD width="40%">  \r\n   			Title 1  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	  <TR class="textAreaContent">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="60%" colspan="2">  \r\n   			My text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy text  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- DOWN SPACER -->  \r\n   	  <tr style="height:90%">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n      </TBODY>  \r\n  </TABLE>  ' 
details.Visual.ShowTitle = False

# Menu

menu = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
menu.AutoConfigure()

menu.Title="menu"
menu.Visual.ShowTitle = False



# Add a Content Item to the Inclusion List
name = "Application Menu HTML"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JQuery"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
menu.UrlInclusions.Add ( name )


# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
menu.UrlInclusions.Add ( name )


layout = LayoutDefinition()
layout.BeginStackedSection()
layout.Add(menu.Visual, 9)
layout.BeginSideBySideSection(91)
layout.Add(details.Visual, 30)
layout.Add(content.Visual, 70)
layout.EndSection()
layout.EndSection()
newPage.ApplyLayout(layout)

#
# PAGE 3 ====================================================================================
#


newPage = Document.Pages.AddNew()
newPage.Title = "Page 3"

Document.ActivePageReference=newPage

content = Document.ActivePageReference.Visuals.AddNew[PieChart]()
content.Title="Replace with your content"
content.AutoConfigure()

details = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
details.Title="Details"
details.HtmlContent =  '   <style>  \r\n   	.textAreaTitle {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 28px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	.textAreaContent {  \r\n   		padding-top : 10px;  \r\n   		color : white;  \r\n   		font-size: 14px;  \r\n   		font-family: Calibri;  \r\n   	}  \r\n   	  \r\n   	body {  \r\n   		margin : 0px !important;  \r\n   	}  \r\n     \r\n   </style>  \r\n     \r\n   <TABLE style="HEIGHT:100%" border="0"  cellspacing="0" cellpadding="0" width="100%">  \r\n      <TBODY style="background-color:#868e96">  \r\n   		<!-- TOP IMAGE -->  \r\n         <TR style="height:10%">  \r\n            <TD align="center" colspan="4">  \r\n   			<img width="100%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/application/images/summary1.jpg" alt="">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	  <tr style="height:20px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- SECTION ONE -->  \r\n   	  <TR class="textAreaTitle">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   			<img width="60%" src="http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/images/externalIcon/earth.png" alt="">  \r\n   		 </TD>  \r\n   		 <TD width="40%">  \r\n   			Title 1  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	  <TR class="textAreaContent">  \r\n            <TD width="20%">  \r\n   		 </TD>  \r\n   		 <TD width="60%" colspan="2">  \r\n   			My text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy textMy text,My text,My text,My textMy textMy text  \r\n   		 </TD>  \r\n   		 <TD width="20%">  \r\n   		 </TD>  \r\n         </TR>  \r\n   	    \r\n   	  <tr style="height:15px">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n   	    \r\n   	  <!-- DOWN SPACER -->  \r\n   	  <tr style="height:90%">  \r\n   		<td colspan="5">  \r\n   		</td>  \r\n   	  </tr>  \r\n      </TBODY>  \r\n  </TABLE>  ' 
details.Visual.ShowTitle = False

# Menu

menu = Document.ActivePageReference.Visuals.AddNew[JSVisualizationModel]()
menu.AutoConfigure()

menu.Title="menu"
menu.Visual.ShowTitle = False


# Add a Content Item to the Inclusion List
name = "Application Menu HTML"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JQuery"
menu.UrlInclusions.Add ( name )

# Add a Content Item to the Inclusion List
name = "JSVIZ"
menu.UrlInclusions.Add ( name )


# Add a Content Item to the Inclusion List
name = "JVizIntrospectionJS"
menu.UrlInclusions.Add ( name )


layout = LayoutDefinition()
layout.BeginStackedSection()
layout.Add(menu.Visual, 9)
layout.BeginSideBySideSection(91)
layout.Add(details.Visual, 30)
layout.Add(content.Visual, 70)
layout.EndSection()
layout.EndSection()
newPage.ApplyLayout(layout)

#
# Back to Page Intro ====================================================================================
#


Document.ActivePageReference=introPage