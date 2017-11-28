from Spotfire.Dxp.Application.Visuals import *
from System.Drawing import Size

from Spotfire.Dxp.Application.Layout import *





newPage = Document.Pages.AddNew()
newPage.Title = "My layout 3 Page"

Document.ActivePageReference=newPage

htmlText1 = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlText1.Title="htmlText1"



htmlText2 = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlText2.Title="htmlText2"


htmlText3 = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlText3.Title="htmlText3"


htmlText4 = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlText4.Title="htmlText4"


viz = Document.ActivePageReference.ActiveVisualReference
visualBounds=Document.ActivePageReference.GetVisualBounds(viz)
print viz.Title
print visualBounds



layout = LayoutDefinition()
layout.BeginSideBySideSection()
layout.Add(htmlText1.Visual, 70)
layout.BeginStackedSection(30)
layout.Add(htmlText2.Visual)
layout.Add(htmlText3.Visual)
layout.Add(htmlText4.Visual)
layout.EndSection()
layout.EndSection()
newPage.ApplyLayout(layout)



