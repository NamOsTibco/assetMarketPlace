from Spotfire.Dxp.Application.Visuals import *
from System.Drawing import Size




newPage = Document.Pages.AddNew()
newPage.Title = "My Template X Page"

Document.ActivePageReference=newPage

htmlTextA = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlTextA.Title="htmlTextA"


htmlTextB = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlTextB.Title="htmlTextB"

htmlTextC = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
htmlTextC.Title="htmlTextC"


viz = Document.ActivePageReference.ActiveVisualReference
visualBounds=Document.ActivePageReference.GetVisualBounds(viz)
print viz.Title
print visualBounds

height=1390
width=1030
Document.Pages.VisualizationAreaSize.Size = Size(height,width)
fitToWindow=Document.Pages.VisualizationAreaSize.FitToWindow
Document.Pages.VisualizationAreaSize.FitToWindow = not fitToWindow



