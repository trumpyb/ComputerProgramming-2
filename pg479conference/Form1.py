
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._cbxRegister = System.Windows.Forms.CheckBox()
		self._cbxKeynote = System.Windows.Forms.CheckBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._mbxWorkshop = System.Windows.Forms.ComboBox()
		self._btnReset = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._cbxKeynote)
		self._groupBox1.Controls.Add(self._cbxRegister)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(244, 128)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# cbxRegister
		# 
		self._cbxRegister.Location = System.Drawing.Point(7, 20)
		self._cbxRegister.Name = "cbxRegister"
		self._cbxRegister.Size = System.Drawing.Size(172, 24)
		self._cbxRegister.TabIndex = 0
		self._cbxRegister.Text = "Conference registration: $895"
		self._cbxRegister.UseVisualStyleBackColor = True
		# 
		# cbxKeynote
		# 
		self._cbxKeynote.Location = System.Drawing.Point(7, 51)
		self._cbxKeynote.Name = "cbxKeynote"
		self._cbxKeynote.Size = System.Drawing.Size(225, 24)
		self._cbxKeynote.TabIndex = 1
		self._cbxKeynote.Text = "Opening Night Dinner and Keynote: $30"
		self._cbxKeynote.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._mbxWorkshop)
		self._groupBox2.Location = System.Drawing.Point(262, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(144, 128)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Preconference Workshop"
		# 
		# mbxWorkshop
		# 
		self._mbxWorkshop.FormattingEnabled = True
		self._mbxWorkshop.Items.AddRange(System.Array[System.Object](
			["Intro to E-Commerce",
			"The Future of the Web",
			"Advanced Visual Basic",
			"Network Security"]))
		self._mbxWorkshop.Location = System.Drawing.Point(7, 20)
		self._mbxWorkshop.Name = "mbxWorkshop"
		self._mbxWorkshop.Size = System.Drawing.Size(121, 21)
		self._mbxWorkshop.TabIndex = 0
		self._mbxWorkshop.Text = "Select One"
		# 
		# btnReset
		# 
		self._btnReset.Location = System.Drawing.Point(13, 147)
		self._btnReset.Name = "btnReset"
		self._btnReset.Size = System.Drawing.Size(115, 41)
		self._btnReset.TabIndex = 2
		self._btnReset.Text = "Reset"
		self._btnReset.UseVisualStyleBackColor = True
		self._btnReset.Click += self.BtnResetClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(134, 147)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(122, 41)
		self._btnClose.TabIndex = 3
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(414, 200)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnReset)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnResetClick(self, sender, e):
		self._cbxRegister.Checked = False
		self._cbxKeynote.Checked = False

	def BtnCloseClick(self, sender, e):
		sum = 0
		if cbxRegister.isChecked():
			sum += 895
		if cbxKeynote.isChecked():
			sum += 30
			
		prices = [295, 295, 395, 395]
		
		index = mbxWorkshop.selectedIndex()
		
		sum += prices[index]
		
		from MainForm import *
		Main = MainForm(self, sum)
		self.Hide()