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
    collision_check = check_terrain_collsion(prev_x,prev_y,char_x,char_y)
        //terrain interactions happen before the character object is relocated
        // regular movement happens if the check turns out that no colision has happened.
        if(collision_check){
            cmv = move_towards_obj(prev_x,prev_y,p.x,p.y,moveRate/2);
        playerChar.transition().attr("cx", cmv[0]).attr("cy", cmv[1]);
        playerChar.transition().attr("cx", prev_x).attr("cy", prev_y);

            char_x = prev_x
            char_y = prev_y
        } else {
        playerChar.transition().attr("cx", char_x).attr("cy", char_y);
        
           {% if terrData.town %}
                {% include "game/core/people/talk_townsfolk.js" %}
                move_townsfolk()
           {% endif %}
           {% if terrData.monsters %}
                {% include "game/core/monsters/move_monsters.js" %}
                move_monster()
            {% endif %}
        }
       playerChar.moveToFront()
       char_tooltip.html(updateToolTip(charData));
//the .js templates are only brought in if the 'monsters' section of the mapData contains monsters. 
{% if "monsters" in mapData %}
    {% include "game/monsters/core_monster.js" %}    
{% endif %}
}
canvas.on("click", svgclick);
</script>
