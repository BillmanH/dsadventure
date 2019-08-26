//returns [-1,1]  for multiplying with other coordinates and determine direction.
function get_pos_neg(x,y){
    nx = x/Math.abs(x)
    ny = y/Math.abs(y)
    return [nx,ny]
}

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

function coordshifter(move){
    return randBetween(move*-1, move)
}

//trig functions for moving and locating objects
function get_distance_vector(Xa,Ya,Xb,Yb,speed){
    var d = [Xb-Xa,Yb-Ya]
    var mag_d = ((d[0]**2)+(d[1]**2))**(1/2)
    var du = [d[0]/mag_d,d[1]/mag_d]
    var coord = [du[0]*speed,du[1]*speed]
    return coord
}

function move_towards_obj(Xa,Ya,Xb,Yb,speed){
    // produces new coordinates that are in the direction of the character, using the speed
    // in this order (object that would like to move [x,y], then the object you would like to move towards [x,y]
    // where x,y are the current coordinates of the object that you would like to move.
    speed=parseInt(speed);
    //console.log('move-towards-object',Xa,Ya,Xb,Yb,speed)
    shift = get_distance_vector(Math.round(Xa),
                Math.round(Ya),
                Math.round(Xb),
                Math.round(Yb),
                speed)
    a = Xa+shift[0]
    b = Ya+shift[1]
    return [a,b]
}
