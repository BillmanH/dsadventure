var widthPadding = 200
if(window.innerWidth <= 800){
     widthPadding=15;
   }
    var width = window.innerWidth-widthPadding,
        height = window.innerHeight-100,
        char_x = width /2,
        char_y = height / 2;
    var canvas = d3.select("body")
        .append("svg")
        .attr("width",width)
        .attr("height",height)
        .attr("id","screen")
        .attr("z-index","1")
        .style("border", "1px solid black");


