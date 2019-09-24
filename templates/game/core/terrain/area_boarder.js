var boarderText = "to the *nextArea* you can see *description*;" +
                "<form class='maptravelform' action='coreview' method='post' id='*nextForm*Form'>" +
                "<input class='charDataHolder' type='hidden' name='charData' value="+JSON.stringify(charData)+">"+
                '{% csrf_token %}'+
                "<button type='submit' value='submit'>Save and progress to this region</button>" +
                "</form>"
//constraints and transition to new area
function render_side_map (char_x,char_y){
    if (char_y < 50) {//north                
        charData['location'] = String(mapData['NArea']['x'])+":"+String(mapData['NArea']['y'])
        charData["arriveFrom"] = "North";        
        d3.select("#northText")
            .html(boarderText
                .replace("*nextArea*",charData["arriveFrom"].toLowerCase())
                .replace("*description*",mapData["NArea"]["terrain"])
                .replace("*nextForm*",charData["arriveFrom"].toLowerCase())
                )
        d3.select(".charDataHolder").attr("value",JSON.stringify(charData)) 
    }
    if (char_y > 50) {
        d3.select("#northText").html("")
        charData['location'] = currentLocation
    }
    if (char_y > height-50) {//south
                 charData['location'] = String(mapData['SArea']['x'])+":"+String(mapData['SArea']['y'])        
        charData["arriveFrom"] = "South";
        d3.select("#southText")
        .html(boarderText
            .replace("*nextArea*",charData["arriveFrom"].toLowerCase())
            .replace("*description*",mapData["SArea"]["terrain"])
            .replace("*nextForm*",charData["arriveFrom"].toLowerCase())
            )
    d3.select(".charDataHolder").attr("value",JSON.stringify(charData)) 
    }
    if (char_y < height - 50) {
        d3.select("#southText").html("")
        charData['location'] = currentLocation
    }
    if (char_x > width - 50) {//east
                        charData['location'] = String(mapData['EArea']['x'])+":"+String(mapData['EArea']['y'])                
        charData["arriveFrom"] = "East";
        d3.select("#eastText")
            .html(boarderText
                .replace("*nextArea*",charData["arriveFrom"].toLowerCase())
                .replace("*description*",mapData["EArea"]["terrain"])
                .replace("*nextForm*",charData["arriveFrom"].toLowerCase())
                )
    d3.select(".charDataHolder").attr("value",JSON.stringify(charData)) 
    }
    if (char_x < width - 50) {
            d3.select("#eastText").html("")
        charData['location'] = currentLocation
    }    
    if (char_x < 50) {//west
                        charData['location'] = String(mapData['WArea']['x'])+":"+String(mapData['WArea']['y'])        
        charData["arriveFrom"] = "West";
        d3.select("#westText")
            .html(boarderText
                .replace("*nextArea*",charData["arriveFrom"].toLowerCase())
                .replace("*description*",mapData["WArea"]["terrain"])
                .replace("*nextForm*",charData["arriveFrom"].toLowerCase())
                )
        d3.select(".charDataHolder").attr("value",JSON.stringify(charData)) 
    }
    if (char_x > 50) {
        d3.select("#westText").html("")
        charData['location'] = currentLocation
    }

   }
