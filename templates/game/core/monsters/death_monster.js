console.log(target, "has died")
d3.select("#"+target.id)
    .classed("dead", true)
    .classed("alive", false)
    .attr("stroke","red")
    .attr("fill","red")
    .attr("damage",0)

objectAlerts("#"+target.id,target.name+" was killed")

