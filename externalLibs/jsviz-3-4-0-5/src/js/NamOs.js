

//
// Main Drawing Method
//

function renderCore(sfdata){

    
	
	document.getElementById("js_chart").innerHTML = '<ul id="nav"><li  class="left"><a href="#">Home</a></li><li class="right"><a href="#">About</a></li><li class="left"><a href="#">Work</a></li><li class="right"><a onClick="hackSpotfirePro()">HACKSPOTIFREPRO</a></li></ul>';

}


function hackSpotfirePro() {
	//alert("TOTO");
	//var par = parent.document.getElementById(window.name);
	var viewport = parent.document.getElementsByClassName("Viewport");
	
	for (i = 0; i < viewport.length; i++) {
		viewport[i].style.color = "red";
		viewport[i].style.backgroundColor = "blue";
	}
	
	
	//viewport[0].style.color = "red";
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



