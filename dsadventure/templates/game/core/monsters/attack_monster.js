
damage = Math.round(randBetween(1, d3.select(this).attr("damage"))*10)/10
charData['composure'] -= damage

objectAlerts("#"+d3.select(this).attr("id"),
    d3.select(this).attr("name")+" "+d3.select(this).attr("attack_type")+" "+damage.toString(),
    color="#FF0000")

if(charData['composure']<0){charDeath()}

