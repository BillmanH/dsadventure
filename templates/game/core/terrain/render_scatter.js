//console.log({{ t|safe }})

ti = {{ t.texture|safe }}
//take imput paramerter from t and create an array of data objets for D3.
function get_data(density){
    data = []
    cord = cord = get_rnd_coord()
    for (i=0;i< {{ t.detail.density}};i++) {
        ti.spawnOrigin_x = cord[0] + coordshifter(3)
        ti.spawnOrigin_y = cord[1] + coordshifter(3)
        data.push(JSON.parse(JSON.stringify(ti)))
    }
    return data
}

var group_data = []
    for (i=0;i< {{ t.detail.abundance}};i++){
        group_data.push(i)
    }

//uncomment to look at the data in the interpreter. 
//console.log("testing string")
//console.log(data)
var ter_group = canvas.selectAll("{{ t.texture.name|safe }}")
            .data(group_data)
            .enter()
            .append("g")
            
function add_circles(d,i){
    d3.select(this)
        .data(get_data())
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
 

}

ter_group.each(add_circles);

/*
        d3.select(this)
                .data(get_data())
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
 )
 */
console.log("x")
