
d3.selectAll(".person,.alive")
    .each(function(d,i){
    if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=10){
        if(terrData['visited']==1){
        objectAlerts("#"+d3.select(this).attr("id"),"Hello " + charData["name"]);
        } else {
        objectAlerts("#"+d3.select(this).attr("id"),"Hello stranger.");
        }
    } 
    })


