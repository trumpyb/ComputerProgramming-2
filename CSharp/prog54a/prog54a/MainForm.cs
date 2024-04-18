/*
 * Created by SharpDevelop.
 * User: trumpy.b
 * Date: 4/15/2024
 * Time: 1:56 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace prog54a
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
	
		
		
		
		void Button1Click(object sender, EventArgs e)
		{
			int miles = 0;
			int gallons = 0;
			double mpg = 0;
			
			if (comboBox1.Text == "1970 VW Bug") {
				miles = 286;
				gallons = 9;
			}else if (comboBox1.Text == "1979 Firebird"){
				miles = 412;
				gallons = 40;
			}else if (comboBox1.Text == "1980 Subaru"){
				miles = 361;
				gallons = 18;
			}else if (comboBox1.Text == "1975 Cutlass"){
				miles = 161;
				gallons = 11;
			}
			else{
				MessageBox.Show("Invalid Selection");
				return;
			}
			
			mpg = miles / (double)gallons;
			mpg = Math.Round(mpg, 1);
			
			label5.Text = miles.ToString();
			label6.Text = gallons.ToString();
			label7.Text = mpg.ToString();
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			label5.Text = "";
			label6.Text = "";
			label7.Text = "";	
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
		
		void Label5Click(object sender, EventArgs e){}
		
		void Label6Click(object sender, EventArgs e){}
		
		
		void Label1Click(object sender, EventArgs e)
		{
			
		}
	}
}
