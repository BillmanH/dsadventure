console.log(target.id, "has died")
d3.select("#" + target.id)
    .classed("dead", true)
    .classed("alive", false)
    .attr("stroke", "red")
    .attr("fill", "red")
    .attr("damage", 0);

objectAlerts("#" + target.id, "A " + d3.select("#" + target.id).attr("name") + " was killed");

charData['attributes'].push("killed:" + d3.select("#" + target.id).attr("name"));
charData['attributes']

charData.kills += 1