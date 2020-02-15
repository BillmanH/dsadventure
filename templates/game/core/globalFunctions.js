//remove something from a dict
function popvalues(a, m) {
    delete a[m]
    return a
}

function limitDict(d) {
    var things_we_dont_print = [
                                'children',
                                'equipment',
                                'spawn_x',
                                'spawn_y',
                                'messages',
                                'y','x',
                                'current situation']
    for(i in things_we_dont_print){
        d = popvalues(d,things_we_dont_print[i])
    }
    return d
}

//for tooltips, convert a dict to HTML
function dictToHtml(d) {
    html = ""
    d = limitDict(d)
    for (var k in d) {
        html += k + ": " + d[k] + "<br>"
    }
    return html
}


//returns [-1,1]  for multiplying with other coordinates and determine direction.
function get_pos_neg(x, y) {
    nx = x / Math.abs(x)
    ny = y / Math.abs(y)
    return [nx, ny]
}

// random coordinates, for placing objects. 
function get_rnd_coord() {
    x = Math.floor(Math.random() * width) + 1;
    y = Math.floor(Math.random() * height) + 1;
    return [x, y]
}

// automatically rounds two decimal places
function randBetween(min, max) {
    var x = Math.random() * (max - min) + min;
    x = Math.round(x * 100) / 100
    return x
}

// rounds
function r(x) {
    x = Math.round(x * 100) / 100
    return x
}



//some additions to d3 that allow me to move them to the front and back.
d3.selection.prototype.moveToFront = function () {
    return this.each(function () {
        this.parentNode.appendChild(this);
    });
};

d3.selection.prototype.moveToBack = function () {
    return this.each(function () {
        var firstChild = this.parentNode.firstChild;
        if (firstChild) {
            this.parentNode.insertBefore(this, firstChild);
        }
    });
};

function coordshifter(move) {
    return randBetween(move * -1, move)
}

//trig functions for moving and locating objects
function get_distance_vector(Xa, Ya, Xb, Yb, speed) {
    var d = [Xb - Xa, Yb - Ya]
    var mag_d = ((d[0] ** 2) + (d[1] ** 2)) ** (1 / 2)
    var du = [d[0] / mag_d, d[1] / mag_d]
    var coord = [du[0] * speed, du[1] * speed]
    return coord
}

//calculate the distance to the character.
function get_dist_to_char(x, y) {
    var a = Math.abs(char_y - y)
    var b = Math.abs(char_x - x)
    var c = Math.sqrt(a * a + b * b);
    return c
}

//calculate the distance between too coordinates
function get_dist_a_b(x1, y1, x2, y2) {
    var a = Math.abs(y2 - y1)
    var b = Math.abs(x2 - x1)
    var c = Math.sqrt(a * a + b * b);
    return c
}

function move_towards_obj(Xa, Ya, Xb, Yb, speed) {
    // produces new coordinates that are in the direction of the character, using the speed
    // in this order (object that would like to move [x,y], then the object you would like to move towards [x,y]
    // where x,y are the current coordinates of the object that you would like to move.
    speed = parseInt(speed);
    //console.log('move-towards-object',Xa,Ya,Xb,Yb,speed)
    shift = get_distance_vector(Math.round(Xa),
        Math.round(Ya),
        Math.round(Xb),
        Math.round(Yb),
        speed)
    if (Number.isNaN(shift[0])) {
        return [Xa, Xb]
    } else {
        a = Xa + shift[0]
        b = Ya + shift[1]
        return [a, b]
    }
}
