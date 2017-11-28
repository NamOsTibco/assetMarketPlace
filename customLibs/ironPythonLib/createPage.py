from Spotfire.Dxp.Application.Visuals import BarChart
from Spotfire.Dxp.Data import DataTable, DataManager

newPage = Document.Pages.AddNew()
newPage.Title = "Script Create Page"


details = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()
details.Title="Script implementation"

details.HtmlContent += '<font size="3"> HERE IS THE IMPLEMENTATION <br/><br/><br/>'



details.HtmlContent += ' from Spotfire.Dxp.Application.Visuals import BarChart <br/>'
details.HtmlContent += 'from Spotfire.Dxp.Data import DataTable, DataManager<br/>'
details.HtmlContent += '<br/>'
details.HtmlContent += 'newPage = Document.Pages.AddNew() <br/>'
details.HtmlContent += 'newPage.Title = "Script Create Page"<br/>'
details.HtmlContent += '<br/>'
details.HtmlContent += '<br/>'
details.HtmlContent += 'details = Document.ActivePageReference.Visuals.AddNew[HtmlTextArea]()<br/>'
details.HtmlContent += 'details.Title="Script implementation"<br/>'
details.HtmlContent += 'details.HtmlContent = ""<br/></font>'

