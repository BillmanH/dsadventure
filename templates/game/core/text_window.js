/*
    Adding text when needed. This global function takes a d3 object, appends some text and that text dissapears when the function is complete. 
    It runs asynchronosly, so you can have multiple objects sending messages simultaniously. 

    Additional text 'textWindow' is at the bottom of the screen and is piped in from the server. You should be able to get it in 'textWindow' from     from the server'
    */

textWindow = d3.select("body")
    .append("div")
    .attr("id","text-window")
    .html(charData["name"] + " is standing in " + mapData["terrain"] +".</br>"+ charData['message'])

//noteDirection is a global that controlls the rolloff of the text (the direction)
noteDirection = 1

// change the direction of the objectAlert's message
function switchDirection(t){
    if(t==1){return [1,1]}
    else if (t==2){return [1,-1]}
    else if (t==3){return [-1,-1]}
    else if (t==4){return [-1,1]}
}


//objectAlerts takes an object (like the char) and sends out a quick text
//message for 
function objectAlerts(subject,message,color="#000000"){
    noteDirection++;
    if(noteDirection>4){noteDirection=1};
    direct = switchDirection(noteDirection);
    subj = d3.select(subject);
    x = subj.attr("cx");
    y = subj.attr("cy");
    nx = (parseInt(x)+(randBetween(50,150)*direct[0])).toString()
    ny = (parseInt(y)+(randBetween(50,150)*direct[1])).toString()
    var objectAlert = d3.select("body")
        .append("div")
        .style("z-index", "10")
        .style("position", "absolute")
        .attr("class","objectalert")
        .style("top", y +"px").style("left",x +"px")
        .html("<p style='color:"+color+"'>"+message+"</p>")
        .transition()
        .duration(2500)
        .style("top", ny +"px").style("left",nx +"px")
    objectAlert.transition()
        .duration(1500)
        .style("opacity", 0)
        .remove()    
}

