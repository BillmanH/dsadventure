var Sprite = {
    init: function(width=null,height=null){
        if(width!=null&height!=null){
            this.coord = this.getRandomChoord(width,height)
        }
    }

    getRandomChoord : function (width,height){  
        x = Math.floor(Math.random() * width) + 1;
        y = Math.floor(Math.random() * height) + 1;
        return [x,y]
    },

    randBetween function (min, max) {
        return Math.random() * (max - min) + min;
    }
}
