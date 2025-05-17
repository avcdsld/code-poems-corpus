using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
namespace BodyClock{
 class Program{
  static void Main(string[] args){
   BodyClock();
   Console.ReadLine();}
  public static void BodyClock(){
   int n, Day = 1, Year = 0;
   bool Life = true;
   n = 1;
   while (Life == true){
    Day += 1;
   if (Day / (365 * n) == 0){
    Year += 1;
    n += 1;
    Console. WriteLine("Happy Birthday your {0}", Year);}
   if (Year == 78){
    Life = false;}}}}}
