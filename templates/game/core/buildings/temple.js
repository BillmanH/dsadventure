var temple = canvas.selectAll("temple")
            .enter()
            .append("g")
            .classed("building",true)
            .classed("temple",true)

temple.selectAll()
        .enter()
        .append("rect")
                    .style('z-index',-1)
                    .attr("x",(width/2) + (60 * terrData['town']["buildings"].indexOf("temple")))
                    .attr("y",(width/2) + (60 * terrData['town']["buildings"].indexOf("temple")))
                    .attr("width",60)
                    .attr("height",60)
                    .attr("affect","bump")
                    .attr("affectText","** hit the great Temple")
                    .attr("name","temple")
                    .classed("terrain", true)
                    .classed("rect", true)
                    .attr("stroke","black")
                    .style("fill","black")
                    .on("mouseover", function(d){
                        return terrain_tooltip.style("visibility", "visible")
                            .html("The holly temple of "+terrData['town']['name']);
                        })
                    .on("mousemove", function(d){
                            return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
                        .html(d.name);
                        })
                    .on("mouseout", function(){
                        return terrain_tooltip.style("visibility", "hidden");
                    })