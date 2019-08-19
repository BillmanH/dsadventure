//console.log({{ t|safe }})

ti = {{ t.texture|safe }}
//take imput paramerter from t and create an array of data objets for D3.
data = []
for (i=0;i< {{ t.detail.abundance|safe }};i++) {
    cord = get_rnd_coord()
    ti.spawnOrigin_x = cord[0]
    ti.spawnOrigin_y = cord[1]
    data.push(JSON.parse(JSON.stringify(ti)))
}

//uncomment to look at the data in the interpreter. 
//console.log("testing string")
//console.log(data)

var elem = canvas.selectAll("{{ t.texture.name|safe }}")
            .data(data)
            .enter()
            .append("rect")
            .style('z-index',-1)
            .attr("x",function(d){return d.spawnOrigin_x})
            .attr("y",function(d){return d.spawnOrigin_y})
            .attr("width", function(d) {return d.size})
            .attr("height", function(d) {return d.size})
            .attr("affect",function(d){return d.affect})
            .attr("affectText",function(d){return d.affectText})
            .attr("affectAmt",function(d){return d.affectAmt})
            .attr("name",function(d){return d.name})
            .classed("terrain", true)
            .classed("rect", true)
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
                    });
            
