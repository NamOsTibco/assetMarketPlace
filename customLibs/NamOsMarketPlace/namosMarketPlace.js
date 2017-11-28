



function execScript(scriptUrl) {
	console.log("***************RUN EXECSCRIPT : BEGIN");
	var ScriptExecutionInfo = { "ScriptName": "execScript", "Arguments": [{ "Key": "scriptUrl", "Value": scriptUrl }] };
	Spotfire.modify ( "script", ScriptExecutionInfo );
	console.log("***************RUN EXECSCRIPT : END");
	
}



function renderCore(sfdata){
	
	console.log("***************RenderCore");
	
//	document.getElementById("js_chart").innerHTML = '<div id="visualization" style="width:100%"> <a href="javascript:execScript(\'http://localhost:8888/spotfireFramework/customLibs/ironPythonLib/createPage.py\')">New Page OK</a> <a href="javascript:execScript(\'http://localhost:8888/spotfireFramework/customLibs/ironPythonLib/createVisTimeline.py\')">New VisTimeLine</a></div>';


/*For Tester only*/
/*var xhr= new XMLHttpRequest();
xhr.open('GET', 'http://localhost:8888/spotfireFramework/customLibs/NamOsMarketPlace/namos-rotating-card.html', true);
xhr.onreadystatechange= function() {
	console.log("***************GET HTML CONTENT");
    if (this.readyState!==4) return;
    if (this.status!==200) return; // or whatever error handling you want
    document.getElementById('js_chart').innerHTML= this.responseText;
};
xhr.send();*/






	
	console.log("***************BEGIN MARKET PLACE");
	
	
	console.log("***************RUN IRON PYTHON : BEGIN");
	var ScriptExecutionInfo = { "ScriptName": "testIron", "Arguments": [{ "Key": "BY", "Value": "Namos" },{ "Key": "MESSAGE", "Value": "YOOOO" }] };
	Spotfire.modify ( "script", ScriptExecutionInfo );
	console.log("***************RUN IRON PYTHON : END");
	

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



