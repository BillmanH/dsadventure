{% include 'game/core/monsters/render_monsters.js' %}

function move_monsters(){
    d3.selectAll(".people,.alive")
        .transition()
                .attr("cx",function(d, i) { return (parseInt(d3.select(this).attr("cx")))+(coordshifter(3))})
                .attr("cy",function(d, i) { return (parseInt(d3.select(this).attr("cy")))+(coordshifter(3))})
}

