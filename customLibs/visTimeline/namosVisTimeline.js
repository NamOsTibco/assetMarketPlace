




function renderCore(sfdata){
	
	console.log("***************RenderCore");
	
	document.getElementById("js_chart").innerHTML = '<div id="visualization" style="width:100%"></div>';
	
	var container = document.getElementById('visualization');

	
	
	
  // note that months are zero-based in the JavaScript Date object
  /*var items = new vis.DataSet([
    {start: new Date(2010,7,23), content: '<div>Conversation</div><img src="http://localhost:8888/jsviz/src/namos/visTimeline/images/community-users-icon.png" style="width:32px; height:32px;">'},
    {start: new Date(2010,7,23,23,0,0), content: '<div>Mail from boss</div><img src="http://localhost:8888/jsviz/src/namos/visTimeline/images/mail-icon.png" style="width:32px; height:32px;">'},
    {start: new Date(2010,7,24,16,0,0), content: 'Report'},
    {start: new Date(2010,7,26), end: new Date(2010,8,2), content: 'Traject A'},
    {start: new Date(2010,7,28), content: '<div>Memo</div><img src="http://localhost:8888/jsviz/src/namos/visTimeline/images/notes-edit-icon.png" style="width:48px; height:48px;">'},
    {start: new Date(2010,7,29), content: '<div>Phone call</div><img src="http://localhost:8888/jsviz/src/namos/visTimeline/images/Hardware-Mobile-Phone-icon.png" style="width:32px; height:32px;">'},
    {start: new Date(2010,7,31), end: new Date(2010,8,3), content: 'Traject B'},
    {start: new Date(2010,8,4,12,0,0), content: '<div>Report</div><img src="http://localhost:8888/jsviz/src/namos/visTimeline/images/attachment-icon.png" style="width:32px; height:32px;">'}
  ]);*/
  
  var myEvents = [];
		
		
		
	//Parsing nodes
	var originalEvents = sfdata.data;
	console.log ("originalEvents : " + JSON.stringify(originalEvents, null, 2));
	console.log("***************originalEvents size : " + originalEvents.length);
	
	for (var i=0;i<originalEvents.length;i++) {
		var curEvent = originalEvents[i].items;
		console.log("******curEvent : " + JSON.stringify(curEvent, null, 2));
		//To refactor to parse less or to use prebuild data from spotfire
		var curEventValue = {  };
		curEventValue.start = curEvent[0];
		console.log("***************************curEvent end : " + curEvent[1]);
		
		if (curEvent[1] != "/Date(-62135568000000)/"){
			curEventValue.end = curEvent[1];
		}
		
		curEventValue.content = '<div>' + curEvent[3] +'</div><img  onerror="this.style.display=' + "'none'" + '" src="http://localhost:8888/spotfireFramework/customLibs/visTimeline/images/' + curEvent[2] + '.png" style="width:48px; height:48px;">';
		
		
		myEvents.push(curEventValue);
	}
	
	
	console.log ("**************************************************");
	console.log ("myEvents : " + JSON.stringify(myEvents, null, 2));

	var items = new vis.DataSet(myEvents);
	
	
  var options = {
    editable: true,
    margin: {
      item: 20,
      axis: 40
    }
  };

  var timeline = new vis.Timeline(container, items, options);
	

}


function hackSpotfirePro() {
	
	
	
	
	
}

// 
// #endregion Drawing Code
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// #region Marking Code
//

//
// This method receives the marking mode and marking rectangle coordinates
// on mouse-up when drawing a marking rectangle
//
function markModel(markMode, rectangle) {
}

// 
// #endregion Marking Code
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// #region Resizing Code
//

var resizing = false;

window.onresize = function (event) {
    // No resizing logic for now
}

// 
// #endregion Resizing Code
//////////////////////////////////////////////////////////////////////////////



