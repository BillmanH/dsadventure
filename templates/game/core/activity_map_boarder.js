/*activity_map_boarder
This manages the user click function svgclick. The game is turn-based so the user's click is considered an action, and then all other objects react to that action.
*/
{% include "game/core/terrain/area_boarder.js" %}
    
function svgclick() {
/*
for click events on the main canvas, not on individual objects. 
Individual opbjects should have thier own click handler.
*/
        // Ignore the click event if it was suppressed
        if (d3.event.defaultPrevented) return;
            // Extract the click location\    
            var point = d3.mouse(this), p = { x: point[0], y: point[1] };
        // Calculate the hypothetical place where the character would be if they were to move. 
         //moveRate is based on the speed and is modified by atributes:
        {% include "game/core/charModifiers/move_modifiers.js" %}
        cmv = move_towards_obj(char_x,char_y,p.x,p.y,moveRate);
        var prev_x = char_x
        var prev_y = char_y
        char_x = cmv[0]
        char_y = cmv[1]
    
// if the character has moved close to the edges of the screen, light up the buttons to save and go to that area. 
    render_side_map(char_x,char_y);
//Each object that reacts to player movement must have an update statement here. 
    // check terrain
    var collision_check = check_terrain_collsion(prev_x,prev_y,char_x,char_y)

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
