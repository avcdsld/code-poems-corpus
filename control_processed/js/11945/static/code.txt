function(node,x,y,size,color,context) {
    context.fillStyle = 'yellow';
    context.beginPath();
    context.arc(x,y,size,1.25*Math.PI,0,false);
    context.arc(x,y,size,0,0.75*Math.PI,false);
    context.lineTo(x,y);
    context.closePath();
    context.fill();

    context.fillStyle = 'white';
    context.strokeStyle = 'black';
    context.beginPath();
    context.arc(x+size/3,y-size/3,size/4,0,2*Math.PI,false);
    context.closePath();
    context.fill();
    context.stroke();

    context.fillStyle = 'black';
    context.beginPath();
    context.arc(x+4*size/9,y-size/3,size/8,0,2*Math.PI,false);
    context.closePath();
    context.fill();
  }