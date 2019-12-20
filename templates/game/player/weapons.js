var weapons = {{ weapons | safe }}

console.log(weapons)

var window_weapons = d3.select("body")
    .append("svg")
    .attr("width",400)
    .attr("height",weapons.length * 100)
    .attr("id","screen")
    .attr("z-index","1")
    .style("border", "1px solid black");

window_weapons.selectAll()
    .data(weapons)
    .enter()
    .append("rect")
    .attr("x",5)
    .attr("y",function(d,i){return (i* 100)+5})
    .attr("height",90)
    .attr("width",390)
    .attr("stroke", "black")
    .attr("fill","black")
    .text(function(d){return d.name})
    .style("color","-internal-root-color")
