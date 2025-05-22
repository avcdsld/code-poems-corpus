SELECT [Love].Name,

IIf([Brains]>[Beauty],"Theatre","Booty-Call")
   AS [Type_Of_Date],

IIf([Love].[True] Like "True", "False",
   IIf([Heartbreaker] Like "True","Bad idea",
   "Sure, why not?"))
   AS [Good_For_A_Fling],

IIf([Height_In_Ft]>5.5,"Y","N")
   AS [Tall_Enough],

IIf([Trust] Like "No","No way",IIf([Love].[True] Like "False","Nah","Absolutely!"))
   AS [Marriage_Material]

FROM ([Love] INNER JOIN Body ON [Love].Name = 
Body.Name)
   INNER JOIN Mind ON Body.Name = Mind.Name;
