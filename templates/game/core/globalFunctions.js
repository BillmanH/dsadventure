// random coordinates, for placing objects. 
function get_rnd_coord(){  
        x = Math.floor(Math.random() * width) + 1;
        y = Math.floor(Math.random() * height) + 1;
        return [x,y]
}
function randBetween(min, max) {
  return Math.random() * (max - min) + min;
}

//some additions to d3 that allow me to move them to the front and back.
d3.selection.prototype.moveToFront = function() {
    return this.each(function(){
        this.parentNode.appendChild(this);
    });
};

d3.selection.prototype.moveToBack = function() {
    return this.each(function() {
        var firstChild = this.parentNode.firstChild;
            if (firstChild) {
                this.parentNode.insertBefore(this, firstChild);
            }
    });
};

//trig functions for moving and locating objects
function get_distance_vector(Xa,Ya,Xb,Yb,speed){
    var d = [Xb-Xa,Yb-Ya]
    var mag_d = ((d[0]**2)+(d[1]**2))**(1/2)
    var du = [d[0]/mag_d,d[1]/mag_d]
    var coord = [du[0]*speed,du[1]*speed]
    return coord
}
