program OhMini8Ball;
var Quest:String;
P: array[0..2] of String= ('Yes', 'No', 'Maybe'); begin Randomize;
WriteLn('What profound answer you ask of me?'); ReadLn(Quest);
if Quest<>'' then begin
WriteLn('From wonders and '+
'mysteries this is given thee');
WriteLn('The Wisdom of the Mini 8-Ball'+
' has for you to see:');
WriteLn(P[Random(3)]);
WriteLn('Come again to seek'+
' only what I may give for free.');
end else WriteLn('Only an empty answer'+
' from a question where the words are free.');end.
