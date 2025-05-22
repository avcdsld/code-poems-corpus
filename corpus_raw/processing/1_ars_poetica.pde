String silence="                  ";
String idea="This is'nt p0etry.";
String draft;
String[]poem=new String[idea.length()];
void setup(){
 draft=idea;
 Write();
 ReThink();
}
void draw(){
ReWrite();
}
void Write(){
println (draft);
}
void ReThink(){
for(int decomp=0;decomp<draft.length();decomp++)
{poem[decomp]=draft.substring(decomp,decomp+1);}
}
void ReWrite(){
 byte seek=byte(random(0, poem.length));
 poem[seek]=" ";
 String poetry=join(poem,"");
 println(poetry);
 if(poetry.equals(silence)){
 println("."); noLoop();}
}
