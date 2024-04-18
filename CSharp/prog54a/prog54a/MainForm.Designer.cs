/*
 * Created by SharpDevelop.
 * User: trumpy.b
 * Date: 4/15/2024
 * Time: 1:56 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
namespace prog54a
{
	partial class MainForm
	{
		/// <summary>
		/// Designer variable used to keep track of non-visual components.
		/// </summary>
		private System.ComponentModel.IContainer components = null;
		
		/// <summary>
		/// Disposes resources used by the form.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing) {
				if (components != null) {
					components.Dispose();
				}
			}
			base.Dispose(disposing);
		}
		
		/// <summary>
		/// This method is required for Windows Forms designer support.
		/// Do not change the method contents inside the source code editor. The Forms designer might
		/// not be able to load this method if it was changed manually.
		/// </summary>
		private void InitializeComponent()
		{
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.label5 = new System.Windows.Forms.Label();
			this.label6 = new System.Windows.Forms.Label();
			this.label7 = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			this.button2 = new System.Windows.Forms.Button();
			this.button3 = new System.Windows.Forms.Button();
			this.comboBox1 = new System.Windows.Forms.ComboBox();
			this.SuspendLayout();
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label1.Location = new System.Drawing.Point(13, 13);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(82, 56);
			this.label1.TabIndex = 0;
			this.label1.Text = "Car";
			this.label1.Click += new System.EventHandler(this.Label1Click);
			// 
			// label2
			// 
			this.label2.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label2.Location = new System.Drawing.Point(13, 73);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(82, 78);
			this.label2.TabIndex = 1;
			this.label2.Text = "Miles";
			// 
			// label3
			// 
			this.label3.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label3.Location = new System.Drawing.Point(13, 170);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(82, 81);
			this.label3.TabIndex = 2;
			this.label3.Text = "Gallons";
			// 
			// label4
			// 
			this.label4.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label4.Location = new System.Drawing.Point(13, 266);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(82, 78);
			this.label4.TabIndex = 3;
			this.label4.Text = "Miles Per Gallon";
			// 
			// label5
			// 
			this.label5.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label5.Location = new System.Drawing.Point(101, 73);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(616, 78);
			this.label5.TabIndex = 4;
			this.label5.Click += new System.EventHandler(this.Label5Click);
			// 
			// label6
			// 
			this.label6.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label6.Location = new System.Drawing.Point(101, 170);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(616, 81);
			this.label6.TabIndex = 5;
			this.label6.Click += new System.EventHandler(this.Label6Click);
			// 
			// label7
			// 
			this.label7.BackColor = System.Drawing.SystemColors.InactiveCaption;
			this.label7.Location = new System.Drawing.Point(101, 266);
			this.label7.Name = "label7";
			this.label7.Size = new System.Drawing.Size(616, 78);
			this.label7.TabIndex = 6;
			// 
			// button1
			// 
			this.button1.Location = new System.Drawing.Point(13, 373);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(75, 23);
			this.button1.TabIndex = 7;
			this.button1.Text = "Calculate";
			this.button1.UseVisualStyleBackColor = true;
			this.button1.Click += new System.EventHandler(this.Button1Click);
			// 
			// button2
			// 
			this.button2.Location = new System.Drawing.Point(237, 373);
			this.button2.Name = "button2";
			this.button2.Size = new System.Drawing.Size(75, 23);
			this.button2.TabIndex = 8;
			this.button2.Text = "Clear";
			this.button2.UseVisualStyleBackColor = true;
			this.button2.Click += new System.EventHandler(this.Button2Click);
			// 
			// button3
			// 
			this.button3.Location = new System.Drawing.Point(471, 373);
			this.button3.Name = "button3";
			this.button3.Size = new System.Drawing.Size(75, 23);
			this.button3.TabIndex = 9;
			this.button3.Text = "Exit";
			this.button3.UseVisualStyleBackColor = true;
			this.button3.Click += new System.EventHandler(this.Button3Click);
			// 
			// comboBox1
			// 
			this.comboBox1.FormattingEnabled = true;
			this.comboBox1.Items.AddRange(new object[] {
									"1970 VW Bug",
									"1979 Firebird",
									"1980 Subaru",
									"1975 Cutlass"});
			this.comboBox1.Location = new System.Drawing.Point(102, 13);
			this.comboBox1.Name = "comboBox1";
			this.comboBox1.Size = new System.Drawing.Size(615, 21);
			this.comboBox1.TabIndex = 10;
			this.comboBox1.Text = "Choose Your Car";
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(729, 445);
			this.Controls.Add(this.comboBox1);
			this.Controls.Add(this.button3);
			this.Controls.Add(this.button2);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.label7);
			this.Controls.Add(this.label6);
			this.Controls.Add(this.label5);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Name = "MainForm";
			this.Text = "prog54a";
			this.ResumeLayout(false);
		}
		private System.Windows.Forms.ComboBox comboBox1;
		private System.Windows.Forms.Button button3;
		private System.Windows.Forms.Button button2;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Label label7;
		private System.Windows.Forms.Label label6;
		private System.Windows.Forms.Label label5;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label1;
	}
}
