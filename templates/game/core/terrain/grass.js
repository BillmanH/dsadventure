{% include 'game/core/terrain/render_scatter.js' %}

ter_group_grass.selectAll()
        .data(function(d){return d})
        .enter()
        .append("line")
                    .style('z-index',-1)
                    .attr("x1",function(d){return d.spawnOrigin_x})
                    .attr("x2",function(d){return d.spawnOrigin_x})
                    .attr("y1",function(d){return d.spawnOrigin_y})
                    .attr("y2",function(d){return d.spawnOrigin_y - (d.size + 5)})
                    .attr("name",function(d){return d.name})
                    .classed("terrain", true)
                    .style("stroke",function(d){return d.borderhex})
                    .attr("stroke-width", 2)
 
