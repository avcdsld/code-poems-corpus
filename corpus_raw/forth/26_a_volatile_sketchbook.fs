\ A Volatile Sketchbook
\ for the vaporware artist

variable page 0 cells allot
0 constant pencil
1 constant charcoal

: draw  1 + + dup 1 + swap 2drop ;
: turn  2 page +! ;

: sketch
        for
                page @ dup
                charcoal draw
                pencil draw
                turn
        next ;

: book  255 sketch ;

book
