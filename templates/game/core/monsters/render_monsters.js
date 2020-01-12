for(i=0;i<terrData['monsters'].length;i++){
    cord = get_rnd_coord()
    for(j=0;j<terrData['monsters'][i].length;j++){
       terrData['monsters'][i][j]['x'] = cord[0] + coordshifter(40)
       terrData['monsters'][i][j]['y'] = cord[1] + coordshifter(40)
    }
}

var monster_group = canvas.selectAll(".monstergroup")
            .data(terrData['monsters'])
            .enter()
            .append("g")
            .classed("pack",true)

monster_group.selectAll()
    .data(function(d){return d})
        .enter()
        .append("circle")
                    .style('z-index',-1)
                    .attr("cx",function(d){return d.x})
                    .attr("cy",function(d){return d.y})
                    .attr("name",function(d){return d.name})
                    .attr("id",function(d){return d.id})
                    .attr("move",function(d){return d.move})
                    .attr("perception",function(d){return d.perception})
                    .attr("attack_type",function(d){return d.attack_type})
                    .attr("damage",function(d){return d.damage})
                    .attr("health",function(d){return d.health})
                    .classed("circle", true)
                    .classed("alive", true)
                    .classed("monster", true)
                    .attr("r",function(d){return d.size})
                    .style("fill",function(d){return d.color})
                    .attr("stroke","black")
                    .on("mouseover", function(d){
                        terrain_tooltip.html(dictToHtml(d3.select(this).datum()))
                        return terrain_tooltip.style("visibility", "visible")
                        })
                    .on("mousemove", function(d){
                            return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
                        })
                    .on("mouseout", function(){
                        return terrain_tooltip.style("visibility", "hidden");
                    })
                    .on("click", function(d){
                        console.log(this,d);
                        charattack(this,d)
                    })

monster_group.selectAll("circle").each(function(d) {
      this.classList.add(d.name);
});

