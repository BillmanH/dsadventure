var worlds_visited = {{ worlds_visited | safe }}
// charData is all of the info relevant to the character
var charData = {{charData | safe}};
var currentLocation = charData['location']
// mapData contains everything for this area and the neighboring four
var mapData = {{mapData | safe}};
// terrData is everything relevant to rendering this area
var terrData = {{terrData | safe}}
