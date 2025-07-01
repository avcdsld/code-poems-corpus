function(score, align, x, y) {

        // call the super constructor
        // (size does not matter here)
        this._super(me.Renderable, "init", [x, y, 10, 10]);

        // create a font
        this.font = new me.BitmapFont(me.loader.getBinary('PressStart2P'), me.loader.getImage('PressStart2P'), 1.5, align, "top");

        // ref to the score variable
        this.scoreRef = score;

        // make sure we use screen coordinates
        this.floating = true;
    }