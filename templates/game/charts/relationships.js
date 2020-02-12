var relationships = {'name':'Character','type':'person','children':{{ relationships | safe }}}

var width = 500,
        height = 500,
        root;

var vLayout = d3.forceSimulation()
            .force('link', d3.forceLink()
                            .id(function(d){return d.id;})
                            .distance(function(d){return 60}))
            .force('charge', d3.forceManyBody())
            .force('center', d3.forceCenter(width / 2, height / 2));

relationship_canvas = d3.select('body').append('svg')
    .attr("width", width)
    .attr("height", height);

relationship_canvas.append('g').classed('clusters',true)

d3.select('svg .clusters').append('g').classed('links',true)
d3.select('svg .clusters').append('g').classed('nodes',true)

var root = d3.hierarchy(relationships);
var vNodes = root.descendants();
var vLinks = root.links();

var roleColors ={
            "commoner": "#b2aa9d",
    }


node = d3.select('svg g.nodes')
  .selectAll('circle.node')
  .data(root.descendants())
  .enter()
  .append('circle')
  .classed('node', true)
  .attr('cx', function(d) {return d.x;})
  .attr('cy', function(d) {return d.y;})
  .attr('r', function(d) {if(d.data.type=='person'){return 10}else{return 30}})
  .style("stroke","black")
  .attr("id", function(d,i){return "t"+String(i)})
  .attr('fill',function(d){return roleColors[d.data.role]})
  .on("mouseover", function(d){
      //console.log(d3.select(this).datum().data);
      return terrain_tooltip.style("visibility", "visible")
      .html(dictToHtml(d3.select(this).datum().data));
  })
  .on("mousemove", function(d){
    return terrain_tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px")
  })
  .on("mouseout", function(){
    return terrain_tooltip.style("visibility", "hidden");
  })


link = d3.select('svg g.links')
  .selectAll('line.link')
  .data(root.links())
  .enter()
  .append('line')
  .classed('link', true)
  .attr('x1', function(d) {return d.source.x;})
  .attr('y1', function(d) {return d.source.y;})
  .attr('x2', function(d) {return d.target.x;})
  .attr('y2', function(d) {return d.target.y;})
  .style("stroke", "#ccc");

vLayout.nodes(vNodes).on('tick', tick);
vLayout.force('link').links(vLinks);

// now to move them. 
function tick() {
      link.attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node.attr("cx", function(d) { return d.x; })
          .attr("cy", function(d) { return d.y; });
}

function color(d) {
      return d._children ? "#3182bd" : d.children ? "#c6dbef" : "#fd8d3c";
}

function click(d) {
      if (!d3.event.defaultPrevented) {
              if (d.children) {
                        d._children = d.children;
                        d.children = null;
                      } else {
                                d.children = d._children;
                                d._children = null;
                              }
              update();
            }
}

function flatten(root) {
      var nodes = [], i = 0;

      function recurse(node) {
              if (node.children) node.children.forEach(recurse);
              if (!node.id) node.id = ++i;
              nodes.push(node);
            }

      recurse(root);
      return nodes;
}

