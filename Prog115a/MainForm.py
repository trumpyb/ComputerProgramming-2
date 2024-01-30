import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._Calc = System.Windows.Forms.Button()
		self._clr = System.Windows.Forms.Button()
		self._ext = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(44, 27)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 342)
		self._listBox1.TabIndex = 0
		# 
		# Calc
		# 
		self._Calc.Location = System.Drawing.Point(170, 27)
		self._Calc.Name = "Calc"
		self._Calc.Size = System.Drawing.Size(75, 23)
		self._Calc.TabIndex = 1
		self._Calc.Text = "Calculate"
		self._Calc.UseVisualStyleBackColor = True
		self._Calc.Click += self.CalcClick
		# 
		# clr
		# 
		self._clr.Location = System.Drawing.Point(170, 180)
		self._clr.Name = "clr"
		self._clr.Size = System.Drawing.Size(75, 23)
		self._clr.TabIndex = 2
		self._clr.Text = "Clear"
		self._clr.UseVisualStyleBackColor = True
		self._clr.Click += self.ClrClick
		# 
		# ext
		# 
		self._ext.Location = System.Drawing.Point(170, 346)
		self._ext.Name = "ext"
		self._ext.Size = System.Drawing.Size(75, 23)
		self._ext.TabIndex = 3
		self._ext.Text = "Exit"
		self._ext.UseVisualStyleBackColor = True
		self._ext.Click += self.ExtClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(888, 442)
		self.Controls.Add(self._ext)
		self.Controls.Add(self._clr)
		self.Controls.Add(self._Calc)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog115a"
		self.ResumeLayout(False)


	def CalcClick(self, sender, e):
		self._listBox1.Items.Clear()
		
		lcv = 2
		
		while lcv <= 36:
			self._listBox1.Items.Add(str(lcv))
			lcv += 2
			
			

	def ClrClick(self, sender, e):
		self._listBox1.Items.Clear()
		

	def ExtClick(self, sender, e):
		Application.Exit()