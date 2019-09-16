function check_terrain_collsion(prev_x,prev_y,char_x,char_y){
    check = false
    t = d3.selectAll(".terrain")
    t.each(function(d, i) {
        if (d3.select(this).classed("circle")){
            var x1=this.cx.baseVal.value
            var y1=this.cy.baseVal.value
            var r=this.r.baseVal.value
        } else if (d3.select(this).classed("rect")){
            var x1=(this.x.baseVal.value)+(this.width.baseVal.value/2)
            var y1=(this.y.baseVal.value)+(this.height.baseVal.value/2)
            var r= (this.height.baseVal.value+this.width.baseVal.value)/2
        }
    //speed up compute time by limiting checks on only the objects that are close. 
    dist_to_ch = get_dist_to_char(x1,y1)
    threshold = charData["speed"]+charData["size"]+r
        if (dist_to_ch<=threshold){
            //you could place a "proximity event" here if you had one
            //console.log(this)
            console.log("[" + x1 + "," + y1 + "]" + " an " + " is close")
            // next check for the actual collsion event
            touch_threshold = get_dist_a_b(char_x,char_y,x1,y1)
            if (touch_threshold<(charData["size"]+r)){
                //all collision activity events here:
                console.log("touche")
                switch (d3.select(this).attr("affect")) {
                case "none":
                    break;
                case "slow":
                    charData["attributes"]["slowed"] = d3.select(this).attr("affectAmt")
                    objectAlerts("#character",d3.select(this).attr("affectText").replace("***",charData["name"]))
                    break;
                case "bump":
                    vol = d3.select(this).attr("affectAmt")
                    objectAlerts("#character",d3.select(this).attr("affectText").replace("***",charData["name"]))
                    break;
                default:
                    break;
            }
                
                check = true
            } 
        } 
    })
return check
}

