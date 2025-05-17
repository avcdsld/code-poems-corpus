enum Color {
    white,
    black,
    dirty
};

class Lamb {
    public:
    Color fleece;

    Lamb();
};

Lamb:: Lamb(): fleece(white)
{
}

class Shepherd {
    Lamb lamb;
};

int main(int argc, char* argv[])
{
    Shepherd mary;

    goto school;

    return (0);

school:
    return (5);
}
