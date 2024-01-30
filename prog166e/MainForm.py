import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._calc = System.Windows.Forms.Button()
		self._clr = System.Windows.Forms.Button()
		self._ext = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# calc
		# 
		self._calc.Location = System.Drawing.Point(170, 12)
		self._calc.Name = "calc"
		self._calc.Size = System.Drawing.Size(75, 23)
		self._calc.TabIndex = 1
		self._calc.Text = "Calculate"
		self._calc.UseVisualStyleBackColor = True
		self._calc.Click += self.CalcClick
		# 
		# clr
		# 
		self._clr.Location = System.Drawing.Point(170, 186)
		self._clr.Name = "clr"
		self._clr.Size = System.Drawing.Size(75, 23)
		self._clr.TabIndex = 2
		self._clr.Text = "Clear"
		self._clr.UseVisualStyleBackColor = True
		self._clr.Click += self.ClrClick
		# 
		# ext
		# 
		self._ext.Location = System.Drawing.Point(170, 380)
		self._ext.Name = "ext"
		self._ext.Size = System.Drawing.Size(75, 23)
		self._ext.TabIndex = 3
		self._ext.Text = "Exit"
		self._ext.UseVisualStyleBackColor = True
		self._ext.Click += self.ExtClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(892, 415)
		self.Controls.Add(self._ext)
		self.Controls.Add(self._clr)
		self.Controls.Add(self._calc)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog166e"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def CalcClick(self, sender, e):
		self._listBox.Items.Clear()
		num = 1
		den = 2
		
		while den<=15:
			while num < den:
				frac = float(num)/den
				fstr = str(num)+"/"+str(den)
				
				self._listBox1.Items.Add(fstr + " = "+str(round(frac,5)))
				
				num += 1
			num = 1
			dem += 1

	def ClrClick(self, sender, e):
		self._listBox.Items.Clear()

	def ExtClick(self, sender, e):
		Application.Exit()