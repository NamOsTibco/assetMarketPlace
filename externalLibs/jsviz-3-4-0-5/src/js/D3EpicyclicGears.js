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

var svg = null;
var path = null;

function dir(object)
{
    stuff = [];

    for (s in object)
    {
        stuff.push(s);
    }

    stuff.sort ();

    return stuff;
}

Array.prototype.max = function()
{
    return Math.max.apply(null, this);
};

function renderCore(sfdata) 
{
    if (resizing) {
        return;
    }

    // Log entering renderCore
    log ( "Entering renderCore" );

    // Extract the columns
    var columns = sfdata.columns;

    // Extract the data array section
    var chartdata = sfdata.data;

    // count the marked rows in the data set, needed later for marking rendering logic
    var markedRows = 0;
    for (var i = 0; i < chartdata.length; i++) {
        if (chartdata[i].hints.marked) {
            markedRows = markedRows + 1;
        }
    }

    var margin = 
    {
        top: 10,
        right: 10,
        bottom: 10,
        left: 10
    };

    var width = window.innerWidth - margin.left - margin.right;
    var height = window.innerHeight - margin.top - margin.bottom;	
    var radius = 80;

    //
    // Replace the following code with actual Visualization code
    // This code just displays a summary of the data passed in to renderCore
    //
	
    drawGears ( width, height, radius );

    wait ( sfdata.wait, sfdata.static );
}

function drawGears ( width, height, radius )
{
    x = Math.sin(2 * Math.PI / 3),
    y = Math.cos(2 * Math.PI / 3);

    var offset = 0,
        speed = 4,
        start = Date.now ();

    svg = d3.select("body").append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(.55)")
      .append("g");

    var frame = svg.append("g")
      .datum({radius: Infinity});

    frame.append("g")
      .attr("class", "annulus")
      .datum({teeth: 80, radius: -radius * 5, annulus: true})
      .append("path")
      .attr("d", gear);

    frame.append("g")
      .attr("class", "sun")
      .datum({teeth: 16, radius: radius})
      .append("path")
      .attr("d", gear);

    frame.append("g")
      .attr("class", "planet")
      .attr("transform", "translate(0,-" + radius * 3 + ")")
      .datum({teeth: 32, radius: -radius * 2})
      .append("path")
      .attr("d", gear);

    frame.append("g")
      .attr("class", "planet")
      .attr("transform", "translate(" + -radius * 3 * x + "," + -radius * 3 * y + ")")
      .datum({teeth: 32, radius: -radius * 2})
      .append("path")
      .attr("d", gear);

    frame.append("g")
      .attr("class", "planet")
      .attr("transform", "translate(" + radius * 3 * x + "," + -radius * 3 * y + ")")
      .datum({teeth: 32, radius: -radius * 2})
      .append("path")
      .attr("d", gear);

    d3.selectAll("input[name=reference]")
      .data([radius * 5, Infinity, -radius])
      .on("change", function(radius1) {
        var radius0 = frame.datum().radius, angle = (Date.now() - start) * speed;
        frame.datum({radius: radius1});
        svg.attr("transform", "rotate(" + (offset += angle / radius0 - angle / radius1) + ")");
      });

    d3.selectAll("input[name=speed]")
      .on("change", function() { speed = +this.value; });

    function gear(d) {
        var n = d.teeth,

        r2 = Math.abs(d.radius),

        r0 = r2 - 8,
        r1 = r2 + 8,
        r3 = d.annulus ? (r3 = r0, r0 = r1, r1 = r3, r2 + 20) : 20,
        da = Math.PI / n,
        a0 = -Math.PI / 2 + (d.annulus ? Math.PI / n : 0),
        i = -1,
        path = ["M", r0 * Math.cos(a0), ",", r0 * Math.sin(a0)];

        while (++i < n) path.push(
            "A", r0, ",", r0, " 0 0,1 ", r0 * Math.cos(a0 += da), ",", r0 * Math.sin(a0),
            "L", r2 * Math.cos(a0), ",", r2 * Math.sin(a0),
            "L", r1 * Math.cos(a0 += da / 3), ",", r1 * Math.sin(a0),
            "A", r1, ",", r1, " 0 0,1 ", r1 * Math.cos(a0 += da / 3), ",", r1 * Math.sin(a0),
            "L", r2 * Math.cos(a0 += da / 3), ",", r2 * Math.sin(a0),
            "L", r0 * Math.cos(a0), ",", r0 * Math.sin(a0));

        path.push("M0,", -r3, "A", r3, ",", r3, " 0 0,0 0,", r3, "A", r3, ",", r3, " 0 0,0 0,", -r3, "Z");

        return path.join("");
    }

    d3.timer(function() {
        var angle = (Date.now() - start) * speed,
            transform = function(d) { return "rotate(" + angle / d.radius + ")"; };

        frame.selectAll("path").attr("transform", transform);
        frame.attr("transform", transform); // frame of reference
    });
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
function markModel(markMode, rectangle)
{
	// Implementation of logic to call markIndices or markIndices2 goes here
}

// 
// #endregion Marking Code
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// #region Resizing Code
//

var resizing = false;

//Handle window resizing event.
window.onresize = function(event) {
    resizing = true;
    if ($("#js_chart")) {
        svg = d3.select("svg");
        if (svg) {
            if (fetchedFirstPlotData) {
				d3.select("svg").remove();
                
				
				var margin = {
                    top: 10,
                    right: 10,
                    bottom: 10,
                    left: 10
                };
                var w = window.innerWidth - margin.left - margin.right;
                var h = window.innerHeight - margin.top - margin.bottom;
				var r = 80;
				
                svg.attr("width", w)
                    .attr("height", h);
				
				drawGears(w,h,r);
				svg = d3.select("svg");
            }
        }
    }
    resizing = false;

}

// 
// #endregion Resizing Code
//////////////////////////////////////////////////////////////////////////////
