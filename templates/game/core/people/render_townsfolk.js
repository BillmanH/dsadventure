console.log({{ t|safe }})

ti = {{ t.texture|safe }}
//take imput paramerter from t and create an array of data objets for D3.
function get_data_{{ t.texture.name|safe }}(){
    scatter_spread = 3
    data = []
    for(j=0;j<{{ t.detail.abundance }}; j++){
    children = []
    cord = cord = get_rnd_coord()
        for (i=0;i< {{ t.detail.density}};i++) {
            ti.spawnOrigin_x = cord[0] + coordshifter(scatter_spread)
            ti.spawnOrigin_y = cord[1] + coordshifter(scatter_spread)
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
       
       
ter_group_{{ t.texture.name|safe }}.selectAll()
    .data(function(d){return d})
        .enter()
        .append("circle")
                    .style('z-index',-1)
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
