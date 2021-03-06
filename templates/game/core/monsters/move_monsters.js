function move_monster() {
    d3.selectAll(".monster.alive")
        .each(function (d, i) {
            //check if the distance is less than perception
            if ((get_dist_to_char(d3.select(this).attr("cx"), d3.select(this).attr("cy")) <= d3.select(this).attr('perception'))
                ||
                (d3.select(this).classed("detectsPlayer"))) {
                if (d3.select(this).classed("detectsPlayer") == false) {
                    objectAlerts("#" + d3.select(this).attr("id"), d3.select(this).attr("name") + " Has spotted " + charData["name"]);
                    d3.select(this).classed("detectsPlayer", true);
                } nmc = move_towards_obj(Math.round(d3.select(this).attr("cx")),
                    Math.round(d3.select(this).attr("cy")),
                    char_x,
                    char_y,
                    d3.select(this).attr("move"));
                d3.select(this).transition()
                    .attr("cx", nmc[0])
                    .attr("cy", nmc[1])
                // check if less than radius of character
                if (get_dist_to_char(
                    d3.select(this).attr("cx"),
                    d3.select(this).attr("cy")
                ) <= ((charData["size"] * 2) + 3)) {
                    nmc = move_towards_obj(Math.round(d3.select(this).attr("cx")),
                        Math.round(d3.select(this).attr("cy")),
                        char_x,
                        char_y,
                        d3.select(this).attr("move") * -2);
                    nmc[0] = nmc[0]
                    nmc[1] = nmc[1]
                    d3.select(this).transition()
                        .attr("cx", nmc[0])
                        .attr("cy", nmc[1])
                    {% include "game/core/monsters/attack_monster.js" %}
                } else {
                    d3.select(this).transition()
                        .attr("cx", nmc[0])
                        .attr("cy", nmc[1])
                }
            } else {
                d3.select(this)
                    .transition()
                    .attr("cx", function (d, i) { return (parseInt(d3.select(this).attr("cx"))) + (coordshifter(3)) })
                    .attr("cy", function (d, i) { return (parseInt(d3.select(this).attr("cy"))) + (coordshifter(3)) })
            }
        })
};

