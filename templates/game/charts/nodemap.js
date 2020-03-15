

var width = 1500, height = 1000



var simulation = d3.forceSimulation(relationships['nodes'])
  .force('charge', d3.forceManyBody().strength(-20))
  .force('center', d3.forceCenter(width / 2, height / 2))
  .force('link', d3.forceLink().links(relationships['links']).id(function(d,i) {
         return d.id
     }))
  .on('tick', ticked);


function updateLinks() {
  var u = d3.select('.links')
    .selectAll('line')
    .data(relationships['links'])

  u.enter()
    .append('line')
    .merge(u)
    .attr('x1', function(d) {
      return d.source.x
    })
    .attr('y1', function(d) {
      return d.source.y
    })
    .attr('x2', function(d) {
      return d.target.x
    })
    .attr('y2', function(d) {
      return d.target.y
    })

  u.exit().remove()
}

function updateNodes() {
  u = d3.select('.nodes')
    .selectAll('text')
    .data(relationships['nodes'])

  u.enter()
    .append('text')
    .text(function(d) {
      return d.id
    })
    .merge(u)
    .attr('x', function(d) {
      return d.x
    })
    .attr('y', function(d) {
      return d.y
    })
    .attr('dy', function(d) {
      return 5
    })

  u.exit().remove()
}

function ticked() {
  updateLinks()
  updateNodes()
}