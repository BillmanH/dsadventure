{% include 'game/core/terrain/render_scatter.js' %}


ter_group_rock
.selectAll()
    .data(function(d){return d})
        .enter()
    .append('image')
        .attr('xlink:href', 'https://s3-us-west-2.amazonaws.com/www.williamjeffreyharding.com/images/rock.png')
        .attr('width', function(d){return d.size*2})
        .attr('height', function(d){return d.size*2})
        .style('z-index',function(d){return d.render_index} )
        .attr("x",function(d){return d.spawnOrigin_x-(d.size)})
        .attr("y",function(d){return d.spawnOrigin_y-(d.size)})
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

ter_group_rock.moveToBack()