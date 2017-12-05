




function renderCore(sfdata){
	
	console.log("££££££££££££££££ " + platform);
	console.log("£££££££££££££££SSSSS£ ");
	
	var imagePath = "https://s3-eu-west-1.amazonaws.com/asset-market-place-sources/customLibs/visTimeline/images";
	
	

	
	
	
	
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
  
  var names = [];
		
		
		
	//Parsing nodes
	var originalEvents = sfdata.data;
	console.log ("originalEvents : " + JSON.stringify(originalEvents, null, 2));
	console.log("***************originalEvents size : " + originalEvents.length);
	
	for (var i=0;i<originalEvents.length;i++) {
		var curEvent = originalEvents[i].items;
		console.log("******curEvent : " + JSON.stringify(curEvent, null, 2));
		//To refactor to parse less or to use prebuild data from spotfire
		var curEventValue = {  };
		//Group Name
		var curGroup = curEvent[1];
		if (names.indexOf(curGroup)==-1) {
			names.push(curGroup);
		}
		curEventValue.group = curGroup;
		
		//Start
		curEventValue.start = curEvent[2];
		console.log("***************************curEvent end : " + curEvent[3]);
		
		
		//End
		if ((!curEvent[6])&&(curEvent[3] != "/Date(-62135568000000)/")){
			curEventValue.end = curEvent[3];
		}
		
		//type
		var className = curEvent[4] ;
		curEventValue.className = className;
		
		var imageName = className;
		
		var description = curEvent[5]
		//Adding tooltip
		curEventValue.title = description;
		
		var singleEvent = curEvent[6];
		if (singleEvent) {
				curEventValue.content = '<div class="icon icon-' + imageName + ' icon"  style="-webkit-mask: url(' + imagePath + '/' + imageName + '.svg) no-repeat 50% 50%;mask: url(images/' + imageName + '.svg) no-repeat 50% 50%;"></div>';
			
		} else  {
				curEventValue.content = '<div class="' + className + '"><div class="iconSmall icon-' + imageName + ' icon"  style="-webkit-mask: url(' + imagePath + '/' + imageName + '.svg) no-repeat 50% 50%;mask: url(images/' + imageName + '.svg) no-repeat 50% 50%; margin-right:4px"></div><span style="margin-bottom:10px">' + description + '</span></div>';
		}
		
		
		
		myEvents.push(curEventValue);
	}
	
	
	console.log ("**************************************************");
	console.log ("myEvents : " + JSON.stringify(myEvents, null, 2));

	var items = new vis.DataSet(myEvents);
	
	
	var groups = new vis.DataSet();
    for (var g = 0; g < names.length; g++) {
	  groups.add({id: g, content: names[g]});
    }
	
	
  var options = {
    editable: false,
    margin: {
      item: 20,
      axis: 40
    },
	tooltip: {
      followMouse: true,
      overflowMethod: 'cap'
    }
  };

 // var timeline = new vis.Timeline(container, items, options);
  
  var timeline = new vis.Timeline(container);
  timeline.setOptions(options);
 // timeline.setGroups(groups);
  timeline.setItems(items);
	

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



