var charColor = "#0000ff"


function get_weapon_in_range(range) {
    w = charData['equipment']['weapons']
    var bestWeapon = { 'name': 'none' }
    for (var i in w) {
        if (w[i].range >= range) {
            return w[i]
        }
    }
    return bestWeapon
}

function assign_damage_to_target(target, damage) {
    if (damage > 0) { damage = damage * -1 } //damage should always be negative so that it subtracts from the target's health.
    d3.select("#" + target.id).data()[0].health = d3.select("#" + target.id).data()[0].health + damage;
    if (d3.select("#" + target.id).data()[0].health <= 0) {
        {% include "game/core/monsters/death_monster.js" %}
    }
}

function meleAttack(target, weapon) {
    d3.select("#" + target.id).classed("detectsPlayer", true)
    damage = 1
    damage = randBetween(1, weapon.damage) + weapon.damage_mod
    assign_damage_to_target(target, damage)
    objectAlerts('#character',
        damage.toString() + ": " + charData['name'] + ' attacks ' + d3.select("#" + target.id).attr("name") + ' with ' + weapon.name,
        color = charColor)
}

function rangeAttack(target, weapon) {
    d3.select(target).classed("detectsPlayer", true)
    //console.log("ranged Attack",weapon)
    damage = randBetween(1, weapon.damage) + weapon.damage_mod
    assign_damage_to_target(target, damage)

    objectAlerts('#character',
        damage.toString() + ": " + charData['name'] + ' attacks ' + d3.select("#" + target.id).attr("name") + ' with ' + weapon.name,
        color = charColor)
    var dart = canvas
        .append("circle")
        .style("z-index", "8")
        .classed("missile", true)
        .attr("cx", d3.select("#character").attr("cx"))
        .attr("cy", d3.select("#character").attr("cy"))
        .attr("r", 2)
        .attr("fill", "black")
        .transition()
        .duration(1000)
        .attr("cx", d3.select(target).attr("cx"))
        .attr("cy", d3.select(target).attr("cy"))
    dart.transition()
        .duration(500)
        .style("opacity", 0)
        .remove()
    console.log(dart)
}

function charattack(target) {
    var charColor = "#0000ff"  //color of the message that the character recieves
    range = get_dist_to_char(d3.select("#" + target.id).attr("cx"), d3.select("#" + target.id).attr("cy"))
    // checktoSee if a character has equipped items that do damage
    weapon = get_weapon_in_range(range)
    if (weapon.name != 'none') {
        if (range <= 20) {
            meleAttack(target, weapon)
        } else {
            rangeAttack(target, weapon)
        }
    } else {
        objectAlerts('#character', "You have no weapon at that range: " + r(range))
    }
}
