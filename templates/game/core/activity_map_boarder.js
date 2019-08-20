/*activity_map_boarder
This manages the user click function svgclick. The game is turn-based so the user's click is considered an action, and then all other objects react to that action.
*/
function svgclick() {
/*
for click events on the main canvas, not on individual objects. 
Individual opbjects should have thier own click handler.
*/
        // Ignore the click event if it was suppressed
        if (d3.event.defaultPrevented) return;
            // Extract the click location\    
            var point = d3.mouse(this), p = { x: point[0], y: point[1] };
         //moveRate is based on the speed and is modified by atributes:
        {% include "game/core/charModifiers/move_modifiers.js" %}
        cmv = move_towards_obj(char_x,char_y,p.x,p.y,moveRate);
        var prev_x = char_x
        var prev_y = char_y
        char_x = cmv[0]
        char_y = cmv[1]
        var boarderText = "to the *nextArea* you can see *description*;" +
                                "<form class='maptravelform' action='/gamecontinue' method='post' id='*nextForm*Form'>" +
                                "<input class='charDataHolder' type='hidden' name='charData' value='placeholder'>"+
                                "<button type='submit' value='submit'>Save and progress to this region</button>" +
                                "</form>"
//constraints and transition to new area
            if (char_y < 50) {//north                
                charData['location'] = String(mapData['NArea']['x'])+":"+String(mapData['NArea']['y'])
                charData["arriveFrom"] = "North";        
                d3.select("#northText")
                    .html(boarderText
                        .replace("*nextArea*",charData["arriveFrom"].toLowerCase())
                        .replace("*description*",mapData["NArea"]["Description"])
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
                        .replace("*description*",mapData["SArea"]["Description"])
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
                        .replace("*description*",mapData["EArea"]["Description"])
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
                        .replace("*description*",mapData["WArea"]["Description"])
                        .replace("*nextForm*",charData["arriveFrom"].toLowerCase())
                    )
            d3.select(".charDataHolder").attr("value",JSON.stringify(charData)) 
                }
            if (char_x > 50) {
                d3.select("#westText").html("")
            charData['location'] = currentLocation
            }
/*
Each object that reacts to player movement must have an update statement here. This also means that this <script> must come at the end, after all of the other 
objects are present
*/
        //terrain interactions happen before the character movement is relocated
        var drc = terrain_interactions(prev_x,prev_y)//terrain_interactions takes the cacluated position change and checks for modifications due to objects
        char_x = drc[0]
        char_y = drc[1]
        playerChar.transition().attr("cx", char_x).attr("cy", char_y);
        playerChar.moveToFront()//ensure that character is always on top and not topped by other characters. 
                char_tooltip.html(updateToolTip(charData));
//the .js templates are only brought in if the 'monsters' section of the mapData contains monsters. 
{% if "monsters" in mapData %}
    {% include "game/monsters/core_monster.js" %}    
{% endif %}
}
canvas.on("click", svgclick);
</script>
