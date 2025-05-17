int comma(int hyphen, int greater)
{
    if (greater > hyphen)
    {
        return comma(greater - hyphen, hyphen);
    }
    else if (hyphen > greater)
    {
        return comma(hyphen - greater, greater);
    }
    else
    {
        return greater, hyphen;
    }
}
