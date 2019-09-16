//take imput paramerter from t and create an array of data objets for D3.

for(var i=0;i < terrData['town']['population'].length;i++){
    c = get_rnd_coord()
    terrData['town']['population'][i]['spawn_x'] = c[0]
    terrData['town']['population'][i]['spawn_y'] = c[1]
}
// (var i=0;i < terrData['town']['population'].length;i++) 
      
canvas.selectAll(".people")
    .data(terrData['town']['population'])
        .enter()
        .append("circle")
                    .style('z-index',-1)
                    .attr("cx",function(d){return d.spawn_x})
                    .attr("cy",function(d){return d.spawn_y})
                    .classed("person", true)
                    .classed("npc", true)
                    .classed("sprite", true)
                    .classed("friendly",true)
                    .classed("circle", true)
                    .attr("id", function(d){return d.name})
                    .attr("r",5)
                    .style("fill","#778899")
                    .style("stroke","black")
                    .on("mouseover", function(d){
                        return terrain_tooltip.style("visibility", "visible")
                            .html(d.name);
                        })
                    .on("mousemove", function(d){
                            return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
                        .html(d.name);
                        })
                    .on("mouseout", function(){
                        return terrain_tooltip.style("visibility", "hidden");
                    })
