<SCRIPT>
judgment= function (you){

 qtn='How many things do you '

 you.guess=prompt(qtn+'guess?',0)
 you.know =prompt(qtn+'know?' ,0)

 induction='fai';deduction='suc'
 arrogance='lu' ;humility ='ce'
 prejudice='re' ;tolerance='ss'

 ignorance=induction+arrogance+prejudice
 wisdom   =deduction+humility +tolerance
 prudence =you.know-you.guess

 this.method=(prudence<1)?ignorance:wisdom

};

m=new judgment({}).method
document.write('This judgment tends to '+m)

</SCRIPT>
