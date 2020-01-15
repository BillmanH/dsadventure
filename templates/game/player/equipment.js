var equipment = {{ equipment | safe }}
function eqData(equipment) {

}

console.log(equipment)

var window_equipment = d3.select(".equipScreen")
    .append("svg")
    .attr("width", 400)
    .attr("height", weapons.length * 100)
    .attr("id", "screen")
    .attr("z-index", "1")
    .style("border", "1px solid black")

var equip_items = window_equipment.selectAll()
    .data(equipment)
    .enter()
    .append("g")
    .on("mouseover", function () {
        eq_tooltip.html(dictToHtml(d3.select(this).datum()))
        eq_tooltip.style("visibility", "visible");
    })
    .on("mousemove", function () {
        eq_tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX + 10) + "px");
    })
    .on("mouseout", function () {
        eq_tooltip.style("visibility", "hidden");
    })
    .on("click", function () {
    });

equip_items.append("rect")
    .attr("x", 5)
    .attr("y", function (d, i) { return (i * 100) + 5 })
    .attr("height", 90)
    .attr("width", 390)
    .attr("stroke", "black")

equip_items.append("text")
    .attr("x", 15)
    .attr("y", function (d, i) { return (i * 100) + 30 })
    .attr("fill", "white")
    .text(function (d) { return d.name })

