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
        .attr("x",0)
    .attr("y",weapons.length * 100)
    .attr("height",100)
    .attr("width",380)
    .style("border", "1px solid black")


