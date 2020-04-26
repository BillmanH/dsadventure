var relationships = charData
relationships['children'] = {{ relationships | safe }}
relationships['role'] = 'hero'
relationships['type'] = 'person'

// var relationships = {
//     'name': 'Character',
//     'type': 'person',
//     'role': 'hero',
//     'children': {{ relationships | safe }}}

var roleColors = {
    "commoner": "#0ee0f7",
    "hero": "#0dabbc",
    "speaker":"#e5b42d",
    "ruler":"#6037a3"
}

var typeColors = {
    "capitol": "#FFFFFF",
    "town": "#A8A8A8",
    "nation": "#00C0AF"
}

console.log(relationships);
var rootNode = d3.hierarchy(relationships)

var width = 1000,
    height = 1000,
    root;

relationship_canvas = d3.select('body').append('svg')
    .attr("width", width)
    .attr("height", height);

relationship_canvas.append('g')
    .classed('nodes',true)

var packLayout = d3.pack()
    .size([300, 300]);
  
rootNode.sum(function(d) {
    return 5;
  });

packLayout(rootNode);

d3.select('svg g')
    .selectAll('circle')
    .data(rootNode.descendants())
    .enter()
    .append('circle')
    .attr("id", function (d, i) { return "t" + String(i) })
    .style("opacity",20)
    .attr('fill', function (d) {
        if (d.data.type == 'person') { return roleColors[d.data.role.split(" ")[0].toLowerCase()] }
        else { return typeColors[d.data.type] }
    })
    .style("stroke","black")
    .attr('cx', function(d) { return d.x; })
    .attr('cy', function(d) { return d.y; })
    .attr('r', function(d) { return d.r; })
    .on("mouseover", function (d) {
        //console.log(d3.select(this).datum().data);
        return terrain_tooltip.style("visibility", "visible")
            .html(dictToHtml(d3.select(this).datum().data));
    })
    .on("mousemove", function (d) {
        return terrain_tooltip.style("top", (event.pageY - 10) + "px").style("left", (event.pageX + 10) + "px")
    })
    .on("mouseout", function () {
        return terrain_tooltip.style("visibility", "hidden");
    })

var nodes = d3.select('svg g')
    .selectAll('g')
    .data(rootNode.descendants())
    .enter()
    .append('g')
    .attr('transform', function(d) {return 'translate(' + [d.x, d.y] + ')'})

nodes
    .append('circle')
    .append('circle')
    .style("opacity",20)
    .attr('r', function(d) { return d.r; })

nodes
    .append('text')
    .attr('dx', -15)
    .attr('dy', 4)
    .style("font-size", "9px")
    .text(function(d) {
        return d.children === undefined ? d.data.name : '';
    })