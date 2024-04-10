/*
 * Created by SharpDevelop.
 * User: trumpy.b
 * Date: 4/10/2024
 * Time: 2:21 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace prog54bConsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Num 1: ");
			int num1 = int.Parse(Console.ReadLine());
			Console.Write("Num 2: ");
			int num2 = int.Parse(Console.ReadLine());
			Console.Write("Num 3: ");
			int num3 = int.Parse(Console.ReadLine());
			Console.Write("Num 4: ");
			int num4 = int.Parse(Console.ReadLine());
			
			int sum = num1 + num2 + num3 + num4;
			double avg = (double)sum / 4;
			
			Console.WriteLine("Sum: " + sum);
			Console.WriteLine("Average: " + Math.Round(avg,2));
			
			Console.ReadKey();
		}
	}
}