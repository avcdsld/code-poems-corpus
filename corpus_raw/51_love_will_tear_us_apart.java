public class LoveWillTearUsApart {

    public static void love(String y, String m, String l){
      if (y!=m) {
        l.split("&");
      }
      love(y, m, l);
    }

    public static void main(String[] args) {
       LoveWillTearUsApart.love("my_road", "your_road", "you&me");
    }
}
