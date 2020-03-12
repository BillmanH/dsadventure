/*
text window : All of the text panels for messages, updates and special function buttons that you need to do actions in the world.  

*/

textWindow = d3.select("body")
    .append("div")
    .attr("id", "text-window")
    .html(charData["current situation"] + ".</br>"
        + charData['message'])

{% if mapData.NArea.terrain != 'void'%}
    textWindow.append("div").attr("id", "northText").html("")
{% endif %}

{% if mapData.SArea.terrain != 'void'%}
    textWindow.append("div").attr("id", "southText").html("")
{% endif %}

{% if mapData.WArea.terrain != 'void'%}
    textWindow.append("div").attr("id", "westText").html("")
{% endif %}

{% if mapData.EArea.terrain != 'void'%}
    textWindow.append("div").attr("id", "eastText").html("")
{% endif %}


textWindow.append("div").attr("id", "eventLog").html("")


var n_messages = 0

//objectAlerts takes an object (like the char) and sends out a quick text
//accepts an object 'this' or playerChar or a class or id
function objectAlerts(subject, message, color = "#000000", bg = "white", decay = 1000) {
    subj = d3.select(subject);
    x = subj.attr("cx");
    y = subj.attr("cy");
    //nx = (parseInt(x)+(randBetween(50,150)*direct[0])).toString()
    //ny = (parseInt(y)+(randBetween(50,150)*direct[1])).toString()
    nx = width.toString()
    ny = parseInt(n_messages * 100).toString()
    n_messages += 1
    var objectAlert = d3.select("body")
        .append("div")
        .style("z-index", "8")
        .style("position", "absolute")
        .attr("class", "objectalert")
        .style("background-color", bg)
        .style("top", y + "px").style("left", x + "px")
        .html("<p style='color:" + color + "'>" + message + "</p>")
        .transition()
        .ease(d3.easeExpOut)
        .duration(1500)
        .style("top", ny + "px").style("left", nx + "px");
    objectAlert.transition()
            .duration(decay)
            .style("opacity", 0)
            .remove()
            .on("end", function() { n_messages -= 1 });
}