mapData['area']['Terrain Textures'] = terrData["Terrain Textures"]
//tool tip should work for all terrain objects
var terrain_tooltip = d3.select("body")
    .append("div")
    .attr("id", "terrain-info")                
    .style("position", "absolute")
    .style("z-index", "10")
    .style("visibility", "hidden")
    .html("<p>Default Text</p>");

// for each item in the list of terrain and details will fetch the template that renders that type of terrain
//
//
{% for i in n_ter_items %} 
    //terrData.terrain_details,terrData.terrain_textures 
    {% with  "game/core/terrain/"|add:i.texture.name|add:".js" as template %}
    {% include template with t=i %}
    {% endwith %}
{% endfor %}
