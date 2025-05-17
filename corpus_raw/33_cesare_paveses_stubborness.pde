String whatHappens;
BufferedReader today;
PImage littleSweetFruits;

void setup() {
    today = createReader
    ("the_world_but_what_i_m_waiting_for.txt");
    littleSweetFruits = loadImage
    ("i_dress_them_up_with_salt.jpg");
}

void draw() {
    try
    {whatHappens = today.readLine();
    /* just things */ }

    catch
    (IOException e)
    {/* so i don't want to see */
    whatHappens = null;}}
