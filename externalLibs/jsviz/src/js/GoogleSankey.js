/*
 Copyright (c) 2016 TIBCO Software Inc

 THIS SOFTWARE IS PROVIDED BY TIBCO SOFTWARE INC. ''AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
 SHALL TIBCO SOFTWARE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
 EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

//////////////////////////////////////////////////////////////////////////////
// #region Drawing Code
//

google.load('visualization', '1', {packages:['sankey']});

var _sankeychart = null;
var _sankeydata = null;
var _nodepadding = 10;

function drawSankey ()
{
    //
    // Set chart options.  For details of other options see: 
    // https://developers.google.com/chart/interactive/docs/gallery/sankey
    //
    var options = {
      width: window.innerWidth - 10,
	  height: window.innerHeight - 10,
	  sankey: { node: { nodePadding: _nodepadding } },
    };
    //
    // Instantiate and draw the chart, passing in the options.
    //
    _sankeychart = new google.visualization.Sankey(document.getElementById('js_chart'));

    _sankeychart.draw ( _sankeydata, options );
}

//
// Main Drawing Method
//

function renderCore(sfdata) 
{
    if (resizing) {
        return;
    }

    // Extract the columns
    var columns = sfdata.columns;

    // Extract the data array section
    var chartdata = sfdata.data;

    // Extract the config params section
    var config = sfdata.config;
	
	// Save the values from the config params
	_nodepadding = config.nodepadding;

    // Create a Google Data Table and populate from Spotfire JSON
    _sankeydata = new google.visualization.DataTable();

    _sankeydata.addColumn('string', 'From');
    _sankeydata.addColumn('string', 'To');
    _sankeydata.addColumn('number', 'Weight');

    for ( row = 0 ; row < chartdata.length ; row++ )
    {
        _sankeydata.addRow ( [ chartdata[row].items[0], chartdata[row].items[1], chartdata[row].items[2] ] );
    }

    // Draw the chart
    drawSankey ();

    wait ( sfdata.wait, sfdata.static );
 }

// 
// #endregion Drawing Code
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// #region Marking Code
//

// Mark an area.
function mark(event)
{    
    return false;
}

// Send marked area to Server or Pro Client.
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
    resizing = true;
    //
    // Confirm that the js_chart div exists AND the svg element exists
    //
    if (_sankeychart) {
        _sankeychart.clearChart ();
		drawSankey ();
    }
    resizing = false;
}

// 
// #endregion Resizing Code
//////////////////////////////////////////////////////////////////////////////
