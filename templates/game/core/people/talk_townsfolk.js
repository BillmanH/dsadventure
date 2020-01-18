get_message = function(d){
    name = d3.select(d).attr("id")
    messages = d3.select(d).attr("messages").split(",")
    message = messages[Math.floor(Math.random()*messages.length)];
    console.log(message)
    if(terrData['visited']==1){
       message = message.replace("stranger",charData["name"])
    }
    return name + ":</br> " + message.replace(",","</br>")
}

d3.selectAll(".person,.alive")
    .each(function(d,i){
    if(get_dist_to_char(d3.select(this).attr("cx"),d3.select(this).attr("cy"))<=10){
        //Person will display message if close enough to character. 
        objectAlerts("#"+d3.select(this).attr("id"),get_message(this),decay=100000);
        }
    })
