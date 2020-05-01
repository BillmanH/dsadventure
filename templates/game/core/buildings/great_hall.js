var great_hall = canvas
    .append("g")
    .classed("building", true)
    .classed("great_hall", true)

great_hall
    .append("rect")
    .style('z-index', -1)
    .attr("x", (width / 2) + (60 * terrData['town']["buildings"].indexOf("great_hall")))
    .attr("y", (height / 2) + (60 * terrData['town']["buildings"].indexOf("great_hall")))
    .attr("width", 60)
    .attr("height", 60)
    .attr("affect", "bump")
    .attr("affectText", "** hit the great hall")
    .attr("name", "great_hall")
    .classed("terrain", true)
    .classed("rect", true)
    .attr("stroke", "black")
    .style("fill", "#a5a5a5")



var hall_image = great_hall.append('image')
    .attr('xlink:href', 'https://s3-us-west-2.amazonaws.com/www.williamjeffreyharding.com/images/img_66610.png')
    .attr('width', 60)
    .attr('height', 60)
    .attr("x", (width / 2) + (60 * terrData['town']["buildings"].indexOf("great_hall")))
    .attr("y", (height / 2) + (60 * terrData['town']["buildings"].indexOf("great_hall")))
    .on("mouseover", function (d) {
        return terrain_tooltip.style("visibility", "visible")
            .html("The great hall of " + terrData['town']['name']);
    })
    .on("mousemove", function (d) {
        return terrain_tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX + 10) + "px")
            .html("The great hall of " + terrData['town']['name']);
    })
    .on("mouseout", function () {
        return terrain_tooltip.style("visibility", "hidden");
    })