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

    // Extract the config section
    var config = sfdata.config;	

    // count the marked rows in the data set, needed later for marking rendering logic
    var markedRows = 0;
    for (var i = 0; i < chartdata.length; i++) 
    {
        if (chartdata[i].hints.marked) 
        {
            markedRows = markedRows + 1;
        }
    }

    var width = window.innerWidth;
    var height = window.innerHeight;
    //
    // Create Tooltip DIV
    //
    $( "body" ).append( '<div id="tooltip"></div>' );	
    //
    // Create formatted data object from Spotfire data
    //
    var text = "";

    text += "[";

    for (var i = 0; i < chartdata.length; i++)
    {
        var _items = chartdata[i].items;
        var _debits = _items[0];
        var _credits= _items[1];
        var _amount = _items[2];

        // Get the row index component from the Spotfire JSON information
        text += "{\"DebitAccountClass\":\"" + _debits + "\",\"CreditAccountClass\":\"" + _credits + "\",\"Amount\":" + _amount + ",\"index\":" + chartdata[i].hints.index + "},"
    }

    text = text.substring(0, text.length - 1); //Remove last comma

    text += "]";

    var data = JSON.parse(text);
    var mpr = chordMpr(data);

    mpr
      .addValuesToMap('DebitAccountClass')
      .setFilter(function (row, a, b) {
        return (row.DebitAccountClass === a.name && row.CreditAccountClass === b.name)
      })
      .setAccessor(function (recs, a, b) {
        if (!recs[0]) return 0;
        //return +recs[0].count;
        return recs[0].DebitAccountClass === a.name ? +recs[0].Amount : +recs[0].index;
      });

    drawChords(mpr.getMatrix(), mpr.getMap());

    wait ( sfdata.wait, sfdata.static );

    //
    //  DRAW THE CHORD DIAGRAM
    //
    function drawChords (matrix, mmap)
    {
        var w = 700, h = 525, r1 = h / 2, r0 = r1 - 50;

        var fill = d3.scale.ordinal()
          .domain(d3.range(28))
          .range(["#FF6600","#F5EDE3","#E1D4C0","#CDBFAC","#6699FF","#154890","#CCCCCC","#62AED4","#FF6600","#FFCC33","#FF6600","#FFCC33","#EEF66C","#FF6600","#F5EDE3","#E1D4C0","#CDBFAC","#6699FF","#fdd5d5","#CCCCCC","#62AED4","#FF6600","#FFCC33","#EEF66C","#FF6600","#FFCC33","#EEF66C","#EEF66C"]);

        var chord = d3.layout.chord()
          .padding(.02)
          .sortSubgroups(d3.descending)
          .sortChords(d3.descending);

        var arc = d3.svg.arc()
          .innerRadius(r0)
          .outerRadius(r0 + 20);

        var svg =d3.select("#js_chart").selectAll("*").remove()

        svg = d3.select("#js_chart").append("svg")
          .attr("width", w)
          .attr("height", h)
          .append("svg:g")
          .attr("id", "circle")
          .attr("transform", "translate(" + w / 2 + "," + h / 2 + ")");

        svg.append("circle")
          .attr("r", r0 + 20);

        $("svg").css({top: 100, left: 200, position:'absolute'});	

        var rdr = chordRdr(matrix, mmap);
        chord.matrix(matrix);

        var g = svg.selectAll("g.group")
          .data(chord.groups())
          .enter().append("svg:g")
          .attr("class", "group")
          .on("mouseover", mouseover)
          .on("mouseout", function (d) { d3.select("#tooltip").style("visibility", "hidden") });

        g.append("svg:path")
          .style("stroke", "black")
          .style("fill", function(d) { return fill(d.index); })
          .attr("d", arc);

        g.append("svg:text")
          .each(function(d) { d.angle = (d.startAngle + d.endAngle) / 2; })
          .attr("dy", ".35em")
          .style("font-family", "helvetica, arial, sans-serif")
          .style("font-size", "10px")
          .attr("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
          .attr("transform", function(d) {
             return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")"
                              + "translate(" + (r0 + 26) + ")"
                              + (d.angle > Math.PI ? "rotate(180)" : "");
             })
          .text(function(d) { return rdr(d).gname; });

        var chordPaths = svg.selectAll("path.chord")
          .data(chord.chords())
          .enter().append("svg:path")
          .attr("class", "chord")
          .style("stroke", function(d) { return d3.rgb(fill(d.target.index)).darker(); })
          .style("fill", function(d) { return fill(d.target.index); })
          .attr("d", d3.svg.chord().radius(r0))
          .on("mouseover", function (d) {
            d3.select("#tooltip")
              .style("visibility", "visible")
              .html(chordTip(rdr(d)))
              .style("top", function () { return (d3.event.pageY - 50)+"px"})
              .style("left", function () { return (d3.event.pageX - 50)+"px";})
            })
          .on("mouseout", function (d) { d3.select("#tooltip").style("visibility", "hidden") });

        function chordTip (d)
        {
            var  q = d3.format(",.3r")
            var returnString= d.sname + " --> " + d.tname + " : " +  q(d.svalue) + "<br/>"

            if (d.tname!= d.sname )
            {
                returnString=returnString+ d.tname + " --> " + d.sname + " : " +  q(d.tvalue) + "<br/>"
            }

            return  returnString
        }

        function groupTip (d)
        {
            var p = d3.format(".1%"), q = d3.format(",.3r")
            return " Total " + d.gname + " : " + q(d.gvalue) + "<br/>"
        }

        function mouseover(d, i)
        {
            d3.select("#tooltip")
              .style("visibility", "visible")
              .html(groupTip(rdr(d)))
              .style("top", function () { return (d3.event.pageY - 10)+"px"})
              .style("left", function () { return (d3.event.pageX - 100)+"px";})

            chordPaths.classed("fade", function(p) {
                return p.source.index != i
                    && p.target.index != i;
            });
        }
    } // drawChords
} // renderCore

// 
// #endregion Drawing Code
//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////
// #region Resizing Code
//

var resizing = false;

window.onresize = function (event) {
}

// 
// #endregion Resizing Code
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

