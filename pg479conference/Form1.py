
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(244, 128)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(7, 20)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(172, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Conference registration: $895"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(7, 51)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(225, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Opening Night Dinner and Keynote: $30"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._comboBox1)
		self._groupBox2.Location = System.Drawing.Point(262, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(144, 128)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Preconference Workshop"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Intro to E-Commerce",
			"The Future of the Web",
			"Advanced Visual Basic",
			"Network Security"]))
		self._comboBox1.Location = System.Drawing.Point(7, 20)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		self._comboBox1.Text = "Select One"
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(414, 153)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)

