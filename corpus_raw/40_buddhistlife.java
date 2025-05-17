public class BuddhistLife {

    boolean alive = true;
    boolean enlightened = false;

    public BuddhistLife() {
        while (alive) {
            fortune();
        }
        dispose();
    }

    private void fortune() {
        if (((int)(Math.random()*365)) == 108){
            alive = false;
        }
        if (((int)(Math.random()*3650)) == 108){
            enlightened = true;
        }
    }

    private void dispose() {
        if (!enlightened) {
            new BuddhistLife();
        }
    }

    public static void main(String[] args) {
        new BuddhistLife();
    }
}
