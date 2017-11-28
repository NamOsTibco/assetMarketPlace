

//
// Main Drawing Method
//


/*ORGINAL


function drawGraph(){
	console.log("Run DrawGraph");
      var cy =cytoscape({
	  container: document.getElementById('cy'),

	  layout: {
		name: 'cose',
		padding: 10
	  },

	  style: cytoscape.stylesheet()
		.selector('node')
		  .css({
			'shape': 'data(faveShape)',
			'width': 'mapData(weight, 40, 80, 20, 60)',
			'content': 'data(name)',
			'text-valign': 'center',
			'text-outline-width': 2,
			'text-outline-color': 'data(faveColor)',
			'background-color': 'data(faveColor)',
			'color': '#fff'
		  })
		.selector(':selected')
		  .css({
			'border-width': 3,
			'border-color': '#333'
		  })
		.selector('edge')
		  .css({
			'curve-style': 'bezier',
			'opacity': 0.666,
			'width': 'mapData(strength, 70, 100, 2, 6)',
			'target-arrow-shape': 'triangle',
			'source-arrow-shape': 'circle',
			'line-color': 'data(faveColor)',
			'source-arrow-color': 'data(faveColor)',
			'target-arrow-color': 'data(faveColor)'
		  })
		.selector('edge.questionable')
		  .css({
			'line-style': 'dotted',
			'target-arrow-shape': 'diamond'
		  })
		.selector('.faded')
		  .css({
			'opacity': 0.25,
			'text-opacity': 0
		  }),

	  elements: {
		nodes: [
		  { data: { id: 'j', name: 'Jerry', weight: 65, faveColor: '#6FB1FC', faveShape: 'triangle' } },
		  { data: { id: 'e', name: 'Elaine', weight: 45, faveColor: '#EDA1ED', faveShape: 'ellipse' } },
		  { data: { id: 'k', name: 'Kramer', weight: 75, faveColor: '#86B342', faveShape: 'octagon' } },
		  { data: { id: 'g', name: 'George', weight: 70, faveColor: '#F5A45D', faveShape: 'rectangle' } }
		],
		edges: [
		  { data: { source: 'j', target: 'e', faveColor: '#6FB1FC', strength: 90 } },
		  { data: { source: 'j', target: 'k', faveColor: '#6FB1FC', strength: 70 } },
		  { data: { source: 'j', target: 'g', faveColor: '#6FB1FC', strength: 80 } },

		  { data: { source: 'e', target: 'j', faveColor: '#EDA1ED', strength: 95 } },
		  { data: { source: 'e', target: 'k', faveColor: '#EDA1ED', strength: 60 }, classes: 'questionable' },

		  { data: { source: 'k', target: 'j', faveColor: '#86B342', strength: 100 } },
		  { data: { source: 'k', target: 'e', faveColor: '#86B342', strength: 100 } },
		  { data: { source: 'k', target: 'g', faveColor: '#86B342', strength: 100 } },

		  { data: { source: 'g', target: 'j', faveColor: '#F5A45D', strength: 90 } }
		]
	  },

	  ready: function(){
		window.cy = this;
	  }
	});
}
*/




function drawGraph(myElements){
	console.log("******************Run DrawGraph !!!");
      var cy =cytoscape({
	  container: document.getElementById('cy'),

	  layout: {
		name: 'cose',
		padding: 10
	  },

	  style: cytoscape.stylesheet()
		.selector('node')
		  .css({
			'shape': 'data(faveShape)',
			'width': 'mapData(weight, 40, 80, 20, 60)',
			'content': 'data(name)',
			'text-valign': 'center',
			'text-outline-width': 2,
			'text-outline-color': 'data(faveColor)',
			'background-color': 'data(faveColor)',
			'color': '#fff'
		  })
		.selector(':selected')
		  .css({
			'border-width': 3,
			'border-color': '#333'
		  })
		.selector('edge')
		  .css({
			'curve-style': 'bezier',
			'opacity': 0.666,
			'width': 'mapData(strength, 70, 100, 2, 6)',
			'target-arrow-shape': 'triangle',
			'source-arrow-shape': 'circle',
			'line-color': 'data(faveColor)',
			'source-arrow-color': 'data(faveColor)',
			'target-arrow-color': 'data(faveColor)'
		  })
		.selector('edge.questionable')
		  .css({
			'line-style': 'dotted',
			'target-arrow-shape': 'diamond'
		  })
		.selector('.faded')
		  .css({
			'opacity': 0.25,
			'text-opacity': 0
		  }),

	  elements: myElements,

	  ready: function(){
		window.cy = this;
	  }
	});
}


function renderCore(sfdata){
	
	//console.log ("SFDATA : " + JSON.stringify(sfdata, null, 2));
		
		
	/*elements: {
		nodes: [
		  { data: { id: 'j', name: 'Jerry', weight: 65, faveColor: '#6FB1FC', faveShape: 'triangle' } },

		],
		edges: [
		  { data: { source: 'j', target: 'e', faveColor: '#6FB1FC', strength: 90 } },
		]
	  }*/
		
		
		var myElements = { nodes: [],edges: []};
		
		
		
		//Parsing nodes
		var originalNodes = sfdata.data;
		console.log ("originalNodes : " + JSON.stringify(originalNodes, null, 2));
		console.log("***************originalNodes size : " + originalNodes.length);
		
		for (var i=0;i<originalNodes.length;i++) {
			var curNode = originalNodes[i].items;
			console.log("******curNode : " + JSON.stringify(curNode, null, 2));
			//To refactor to parse less or to use prebuild data from spotfire
			var curNodeValue = { data: { } };
			curNodeValue.data.id = curNode[0];
			curNodeValue.data.name = curNode[1];
			curNodeValue.data.weight = curNode[2];
			curNodeValue.data.faveColor = curNode[3];
			curNodeValue.data.faveShape = curNode[4];
			
			myElements.nodes.push(curNodeValue);
		}
		
		
		console.log ("**************************************************");
		console.log ("elements : " + JSON.stringify(myElements, null, 2));
		
		//Parsing deges
		var originalEdges = sfdata.additionalTables[0].data;
		console.log ("originalEdges : " + JSON.stringify(originalEdges, null, 2));
		console.log("***************originalEdges size : " + originalEdges.length);
		
		for (var i=0;i<originalEdges.length;i++) {
			var curEdge = originalEdges[i].items;
			console.log("******curEdge : " + JSON.stringify(curEdge, null, 2));
			//To refactor to parse less or to use prebuild data from spotfire
			var curEdgeValue = { data: { } };
			curEdgeValue.data.source = curEdge[0];
			curEdgeValue.data.target = curEdge[1];
			curEdgeValue.data.faveColor = curEdge[2];
			curEdgeValue.data.strength = curEdge[3];
			
			myElements.edges.push(curEdgeValue);
		}
		
		
		console.log ("**************************************************");
		console.log ("elements : " + JSON.stringify(myElements, null, 2));

    
	
	document.getElementById("js_chart").innerHTML = '<div id="cy"></div>';
	
	drawGraph(myElements);


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



