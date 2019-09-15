console.log({{ t|safe }})

ti = {{ t.texture|safe }}
//take imput paramerter from t and create an array of data objets for D3.
function get_data_{{ t.texture.name|safe }}(){
    scatter_spread = {{ t.texture.size }}
    data = []
    for(j=0;j<{{ t.detail.abundance }}; j++){
    children = []
    cord = cord = get_rnd_coord()
        for (i=0;i< {{ t.detail.density}};i++) {
            buildShift = get_pos_neg(randBetween(-1,1),randBetween(-1,1))
            ti.spawnOrigin_x = cord[0] + ((buildShift[0]*{{ t.texture.size }})/2)
            ti.spawnOrigin_y = cord[1] + ((buildShift[1]*{{ t.texture.size }})/2)
            children.push(JSON.parse(JSON.stringify(ti)))
            cord = [cord[0] + ((buildShift[0]*{{ t.texture.size }})),cord[1] + ((buildShift[1]*{{ t.texture.size }}))]
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
       
       
ter_group_{{ t.texture.name|safe }}.selectAll()
    .data(function(d){return d})
        .enter()
        .append("rect")
                    .style('z-index',-1)
                    .attr("x",function(d){return d.spawnOrigin_x})
                    .attr("y",function(d){return d.spawnOrigin_y})
                    .attr("width",function(d){return d.size})
                    .attr("height",function(d){return d.size})
                    .attr("affect",function(d){return d.affect})
                    .attr("affectText",function(d){return d.affectText})
                    .attr("affectAmt",function(d){return d.affectAmt})
                    .attr("name",function(d){return d.name})
                    .classed("terrain", true)
                    .classed("rect", true)
                    .attr("stroke","black")
                    .style("fill",function(d){return d.hexcolor})
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
