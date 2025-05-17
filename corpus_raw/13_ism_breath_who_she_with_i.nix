cat roomofonesown.txt | sed 's/a[A-Z]/[a-z]/g' |
grep -oE "\b[a-z]+ism\b" | sort | uniq -c | sort
   1 despotism
   1 feminism
   1 prganism
   1 scepticism
   1 symbolism
  13 criticism

cat roomofonesown.txt | grep -oE "\b[a-z]+ 
breath\b"
drew breath
her breath
his breath
hot breath
my breath
our breath
