console.log("attack event")
objectAlerts("#"+d3.select(this).attr("id"),
    d3.select(this).attr("name")+" "+d3.select(this).attr("attack_type"),
    color="#FF0000")
