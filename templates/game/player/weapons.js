var weapons = {{ weapons | safe }}

console.log(weapons)

var window_eq = d3.select("body")
    .append("svg")
    .attr("width",400)
    .attr("height",weapons.length * 100)
    .attr("id","screen")
    .attr("z-index","1")
    .style("border", "1px solid black");


