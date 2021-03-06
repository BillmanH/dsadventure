console.log({{ t|safe }})

ti = {{ t.texture|safe }}
//take imput paramerter from t and create an array of data objets for D3.
function get_data_{{ t.texture.name|safe }}(){
    scatter_spread = {{ t.texture.spread_radius|safe }}
    data = []
    tabundance =  {{ t.detail.abundance }}
    if(ti.abundance_affected_by == 'elevation'){tabundance+=terrData.elevation}
    if(ti.abundance_affected_by == 'rainfall'){tabundance+=terrData.rainfall}
    for(j=0;j< tabundance ; j++){
    children = []
    cord = get_rnd_coord()
    direction = get_pos_neg(randBetween(-1,1)
                            ,randBetween(-1,1))
    tdensity = {{ t.detail.density }}
    if(ti.density_affected_by == 'elevation'){tdensity+=terrData.elevation}
    if(ti.density_affected_by == 'rainfall'){tdensity+=terrData.rainfall}
        for (i=0;i< tdensity ;i++) {
            ti.spawnOrigin_x = cord[0] + (randBetween(0,scatter_spread)*direction[0])
            ti.spawnOrigin_y = cord[1] + (randBetween(0,scatter_spread)*direction[1])
            cord[0] = ti.spawnOrigin_x
            cord[1] = ti.spawnOrigin_y
            children.push(JSON.parse(JSON.stringify(ti)))
        }
        data.push(children)
    }
    return data
}

var ter_group_{{ t.texture.name|safe }} = canvas.selectAll("{{ t.texture.name|safe }}")
            .data(get_data_{{ t.texture.name|safe }}())
            .enter()
            .append("g")
            .classed("terrain",true)
            .classed("{{ t.texture.name|safe }}",true)
            .style('z-index',"{{ t.texture.render_index|safe }}")

ter_group_{{ t.texture.name|safe }}.selectAll()
    .data(function(d){return d})
        .enter()
        .append("circle")
        .style('z-index',function(d){return d.render_index} )
                    .attr("cx",function(d){return d.spawnOrigin_x})
                    .attr("cy",function(d){return d.spawnOrigin_y})
                    .attr("affect",function(d){return d.affect})
                    .attr("affectText",function(d){return d.affectText})
                    .attr("affectAmt",function(d){return d.affectAmt})
                    .attr("name",function(d){return d.name})
                    .classed("terrain", true)
                    .classed("circle", true)
                    .attr("r",function(d){return d.size})
                    .style("fill",function(d){return d.hexcolor})
                    .style("stroke",function(d){return d.borderhex})
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
