// Tooltip, hover over character to see some stats

var char_tooltip = d3.select("body")
    .append("div")
    .attr("id", "char-info")
    .style("position", "absolute")
    .style("z-index", "10")
    .style("visibility", "hidden")
    .style("background-color", 'white')
    .html(charData["name"] + "<br>"
        + charData['title'] + "<br>"
        + charData['composure'] + "<br>"
        + ""); //add extra eliments to be displayed to the char tooltip

function updateToolTip(charData) {
    h = charData["name"] + "<br>"
        + charData['title'] + "<br>"
        + charData['composure'] + "<br>"
    return h
}

// if the character goes off to the east, then they show up on the west side of the next cell component.    
function alighnCharacter() {
    if ("arriveFrom" in charData) {
        if (charData["arriveFrom"] == "North") {
            char_x = width / 2
            char_y = height - 55
        }
        if (charData["arriveFrom"] == "South") {
            char_x = width / 2
            char_y = 55
        }
        if (charData["arriveFrom"] == "East") {
            char_x = 55
            char_y = height / 2
        }
        if (charData["arriveFrom"] == "West") {
            char_x = width - 55
            char_y = height / 2
        }
    }
}

alighnCharacter(); //if character came from somewhere, charData[arriveFrom] will reset the origin

// main charater object
var playerChar = canvas.append("circle")
    .attr("id", "character")
    .attr("cx", char_x)
    .attr("cy", char_y)
    .attr("r", charData["size"])
    .attr("composure", charData["composure"])
    .style("z-index", "9")
    .on("mouseover", function () {
        char_tooltip.html(dictToHtml(charData))
        char_tooltip.style("visibility", "visible");
    })
    .on("mousemove", function () {
        char_tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX + 10) + "px");
    })

    .on("mouseout", function () {
        char_tooltip.style("visibility", "hidden");
    })
    .on("click", function () {
    });

// What happens if the character dies
function charDeath() {
    playerChar.transition()
        .attr("fill", "red");
    charData["speed"] = 0
    d3.select("#text-window").html(charData["name"] + " has died!!")
    d3.select(".charDataHolder").attr("value", JSON.stringify(charData))
    d3.select("#chardeath").style("visibility", "visible")
    d3.select(".maptravelform").style("visibility", "hidden")
    d3.select("#chardeathbutton").html(charData["name"] + " has died...")
}

{% include "game/player/attack_char.js" %}

objectAlerts("#character", charData["current situation"])
