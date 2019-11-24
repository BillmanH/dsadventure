get_message = function(d){
    name = d3.select(d).attr("id")
    message = d3.select(d).attr("messages")
    if(terrData['visited']==1){
       message = message.replace("stranger",charData["name"])
    }
    return name + ":</br> " + message.replace(",","</br>")
}

d3.selectAll(".person,.alive")
    .each(function(d,i){
    if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=10){
        //Person will display message if close enough to character. 
        objectAlerts("#"+d3.select(this).attr("id"),get_message(this));
        }
    })
