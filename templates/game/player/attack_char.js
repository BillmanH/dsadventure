var charColor = "#0000ff"

function assign_damage_to_target(target,damage){
    console.log("assign_damage_to_target",target.id)
    if(damage>0){damage=damage*-1} //damage should always be negative so that it subtracts from the target's health.
        d3.select("#"+target.id).data()[0].health=d3.select("#"+target.id).data()[0].health+damage;
    if (d3.select("#"+target.id).data()[0].health<=0){
        {% include "game/core/monsters/death_monster.js" %}
    }
}

function meleAttack(target,weapon){
    damage = 1
    assign_damage_to_target(target,damage)
    objectAlerts('#character',
        damage.toString()+": " + charData['name']+' attacks '+ target.name +' with '+ weapon,
        color=charColor)
}

function rangeAttack(target,weapon){
    damage = 1
    assign_damage_to_target(target,damage)

     objectAlerts('#character',
        damage.toString()+": " + charData['name']+' attacks '+ target.name +' with '+ weapon,
        color=charColor)
}

function charattack(target){
    console.log("charattack: ",target.id)
    var charColor = "#0000ff"  //color of the message that the character recieves
    range = get_dist_to_char(target)
    console.log(range)
    // checktoSee if a character has equipped items that do damage
    if((range <= 10)&(true)){
      meleAttack(target) 
    } else if ((range => 10)&(true)){
       rangeAttack(target)
    } else {
        //no attack
    }
}
