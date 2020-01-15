/*
    Adding text when needed. This global function takes a d3 object, appends some text and that text dissapears when the function is complete. 
    It runs asynchronosly, so you can have multiple objects sending messages simultaniously. 

    */

textWindow = d3.select("body")
    .append("div")
    .attr("id", "text-window")
    .html(charData["current situation"] + ".</br>"
        + charData['message'])

if (mapData['NArea']['terrain'] != 'void') { textWindow.append("div").attr("id", "northText").html("") }
if (mapData['EArea']['terrain'] != 'void') { textWindow.append("div").attr("id", "eastText").html("") }
if (mapData['SArea']['terrain'] != 'void') { textWindow.append("div").attr("id", "southText").html("") }
if (mapData['WArea']['terrain'] != 'void') { textWindow.append("div").attr("id", "westText").html("") }
textWindow.append("div").attr("id", "eventLog").html("")

n_messages = 0

//objectAlerts takes an object (like the char) and sends out a quick text
//accepts an object 'this' or playerChar or a class or id
function objectAlerts(subject, message, color = "#000000", bg = "white") {
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
        .style("top", ny + "px").style("left", nx + "px")
    if (message.length < 30) {
        objectAlert.transition()
            .duration(1000)
            .style("opacity", 0)
            .remove()
            .on("end", function () { n_messages -= 1 });
    }
}

