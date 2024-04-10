/*
 * Created by SharpDevelop.
 * User: trumpy.b
 * Date: 4/10/2024
 * Time: 2:04 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Prog52aconsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter Length: ");
			int len = int.Parse(Console.ReadLine());
			Console.Write("Enter Width: ");
			int wid = int.Parse(Console.ReadLine());
			
			int area = len * wid;
			int perim = 2 * len + 2 * wid;
			
			Console.WriteLine("Area: " + area);
			Console.WriteLine("Perimeter: " + perim);
			
			Console.ReadKey();
		}
	}
}