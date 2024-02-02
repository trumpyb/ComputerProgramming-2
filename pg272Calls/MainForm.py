import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._Daytime = System.Windows.Forms.RadioButton()
		self._Evening = System.Windows.Forms.RadioButton()
		self._OffHours = System.Windows.Forms.RadioButton()
		self._Time = System.Windows.Forms.TextBox()
		self._btnCalc = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._OffHours)
		self._groupBox1.Controls.Add(self._Evening)
		self._groupBox1.Controls.Add(self._Daytime)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(119, 121)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# Daytime
		# 
		self._Daytime.Location = System.Drawing.Point(7, 20)
		self._Daytime.Name = "Daytime"
		self._Daytime.Size = System.Drawing.Size(104, 24)
		self._Daytime.TabIndex = 0
		self._Daytime.TabStop = True
		self._Daytime.Text = "Daytime"
		self._Daytime.UseVisualStyleBackColor = True
		# 
		# Evening
		# 
		self._Evening.Location = System.Drawing.Point(7, 51)
		self._Evening.Name = "Evening"
		self._Evening.Size = System.Drawing.Size(104, 24)
		self._Evening.TabIndex = 1
		self._Evening.TabStop = True
		self._Evening.Text = "Evening"
		self._Evening.UseVisualStyleBackColor = True
		# 
		# OffHours
		# 
		self._OffHours.Location = System.Drawing.Point(7, 82)
		self._OffHours.Name = "OffHours"
		self._OffHours.Size = System.Drawing.Size(104, 24)
		self._OffHours.TabIndex = 2
		self._OffHours.TabStop = True
		self._OffHours.Text = "Off Hours"
		self._OffHours.UseVisualStyleBackColor = True
		# 
		# Time
		# 
		self._Time.Location = System.Drawing.Point(13, 141)
		self._Time.Name = "Time"
		self._Time.Size = System.Drawing.Size(119, 20)
		self._Time.TabIndex = 1
		# 
		# btnCalc
		# 
		self._btnCalc.Location = System.Drawing.Point(13, 168)
		self._btnCalc.Name = "btnCalc"
		self._btnCalc.Size = System.Drawing.Size(119, 23)
		self._btnCalc.TabIndex = 2
		self._btnCalc.Text = "Calculate"
		self._btnCalc.UseVisualStyleBackColor = True
		self._btnCalc.Click += self.BtnCalcClick
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(155, 168)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(857, 424)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._btnCalc)
		self.Controls.Add(self._Time)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg272Calls"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnCalcClick(self, sender, e):
		num = int(self._Time.Text)
		
		multiple = 0
		
		if self._Daytime.Checked:
			multiple = .07
		if self._Evening.Checked:
			multiple = .12
		if self._OffHours.Checked:
			multiple = .05
			
		self._label1.Text = "The cost of your phone call is $"+str(round(multiple*num,2))
		
