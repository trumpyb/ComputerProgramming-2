/*
 * Created by SharpDevelop.
 * User: trumpy.b
 * Date: 4/10/2024
 * Time: 2:32 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace prog54cConsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			double PI = 3.14159;
			Console.Write("Radius: ");
			double radius = double.Parse(Console.ReadLine());
			
			double area = PI * radius * radius;
			double perim = 2 * PI * radius;
			
			Console.WriteLine("Area: " + area);
			Console.WriteLine("Perimeter: " + perim);
			
			Console.ReadKey();
		}
	}
}