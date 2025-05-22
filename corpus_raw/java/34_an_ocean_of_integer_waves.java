public class IntWaves
{
public static void main(String[] a)
throws Throwable
{
  int h=25;
  while(true)
  {
    java.io.PrintStream p = System.out;
    int cnt=new java.util.Random().nextInt(h);
    int i=0,j=0;
    for(;i<=cnt;i++)
    {
      for(j=0;j<i;j++){p.print(i);}
      p.println();
      Thread.sleep(h);
    }
    for (i=cnt;i>=0;i--)
    {
      for(j=0;j<i;j++){p.print(i);}
      p.println();
      Thread.sleep(h);
    }
  }
}
}
