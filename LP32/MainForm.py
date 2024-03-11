import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

from Class1 import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._txtDiameter = System.Windows.Forms.TextBox()
		self._lblOutput = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Pizza Diameter"
		# 
		# txtDiameter
		# 
		self._txtDiameter.Location = System.Drawing.Point(120, 13)
		self._txtDiameter.Name = "txtDiameter"
		self._txtDiameter.Size = System.Drawing.Size(100, 20)
		self._txtDiameter.TabIndex = 1
		# 
		# lblOutput
		# 
		self._lblOutput.Location = System.Drawing.Point(13, 71)
		self._lblOutput.Name = "lblOutput"
		self._lblOutput.Size = System.Drawing.Size(207, 139)
		self._lblOutput.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(94, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(176, 225)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(742, 418)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._lblOutput)
		self.Controls.Add(self._txtDiameter)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "LP32"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._txtDiameter.Text = ""
		self._lblOutput.Text = ""

	def Button1Click(self, sender, e):
		diameter = int(self._txtDiameter.Text)
		price = Class1(diameter)
		self._lblOutput.Text = "$"+str(price.calcPrice())