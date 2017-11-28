
#For logging
from Spotfire.Dxp.Application.Visuals import HtmlTextArea
from datetime import datetime
logMarker = "LOG END"
def getLogArea():
	try:
		pageID = System.Guid(Document.Properties["LogPageGUID"])
		page = clr.Reference[Page]()
		bFoundPage = Document.Pages.TryGetPage(pageID, page)
		logAreaID = System.Guid(Document.Properties["LogVisualGUID"])
		visual = clr.Reference[Visual]()
		bFoundLogArea = page.Visuals.TryGetVisual(logAreaID, visual)
		if bFoundPage and bFoundLogArea:						
			return visual
		else:			
			raise("Not found")
	except:
		for page in Document.Pages:
			if page.Title == Document.Properties["LogPageTitle"]:
				print "Got log page"
				try:
					Document.Properties["LogPageGUID"] = page.Id.ToString()
				except:
					pass
				for vis in page.Visuals: 
					if vis.Title == Document.Properties["LogVisualTitle"]:
						print "got log vis"
						try:
							Document.Properties["LogVisualGUID"] = vis.Id.ToString()
						except:
							pass
						return vis
	return None
logArea = getLogArea()
print logArea
def appendLogMessage(message):
	try:	
		html = str(logArea.As[HtmlTextArea]().HtmlContent)
		if html == None or html == "None" or html == "" : html = logMarker
		print "html" + html
		logArea.As[HtmlTextArea]().HtmlContent = str.replace(html, logMarker, datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + message + "<BR>" + logMarker)
		print message
	except:
		pass
#End of logging 