function smoothLine(fromX,fromY,toX,toY) {
  var radius=10,p,_translate;
  var signX=fromX>toX?-1:1,signY=fromY>toY?-1:1;
  if (Math.abs(fromY-toY)<radius*1.5 /*|| Math.abs(fromX-toX)<radius*2*/) {
    p=['M',fromX,fromY,
       'C',fromX+Math.min(Math.abs(toX-fromX)/2,radius)*signX,fromY,
       toX-(toX-fromX)/2,toY,
       toX,toY];
    _translate=function (x,y) {
      var p=this.path;
      p[1]+=x;p[2]+=y;
      p[4]+=x;p[5]+=y;
      p[6]+=x;p[7]+=y;
      p[8]+=x;p[9]+=y;
    };
  } else {
    p=[
      'M',fromX,fromY,
      'Q',fromX+radius*signX,fromY,fromX+radius*signX,fromY+radius*signY,
      'V',Math.abs(fromY-toY)<radius*2 ? fromY+radius*signY : (toY-radius*signY),
      'Q',fromX+radius*signX,toY,fromX+radius*signX*2,toY,
      'H',toX
    ];
    _translate=function (x,y) {
      var p=this.path;
      p[1]+=x;p[2]+=y;
      p[4]+=x;p[5]+=y;p[6]+=x;p[7]+=y;
      p[9]+=y;
      p[11]+=x;p[12]+=y;p[13]+=x;p[14]+=y;
      p[16]+=x;
    };
  }
  return {
    type:'path',
    path:p,
    'stroke-linecap':'butt',
    'stroke-linejoin':'round',
    'stroke':'#333',
    'stroke-width':2,
    _translate:_translate
  };
}