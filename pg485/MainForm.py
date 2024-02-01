import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular shades Add $0",
			"Folding shades Add $10",
			"Roman shades Add $15"]))
		self._comboBox1.Location = System.Drawing.Point(119, 36)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 inches wide Add $0",
			"27 inches wide Add $2",
			"32 inches wide Add $4",
			"40 inches wide Add $6"]))
		self._comboBox2.Location = System.Drawing.Point(246, 36)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 1
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural Add $5",
			"Blue Add $0",
			"Teal Add $0",
			"Red Add $0",
			"Green Add $0"]))
		self._comboBox3.Location = System.Drawing.Point(373, 37)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 2
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 37)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 8)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(99, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "Number of shades"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(119, 7)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(121, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Type of shades"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(247, 7)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(120, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Width of shades"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(373, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(121, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Color of shades"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 112)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 23)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate Price"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 205)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(271, 119)
		self._label5.TabIndex = 9
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(893, 452)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "pg485"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		
		TypeIndex = self._comboBox1.SelectedIndex
		WidthIndex = self._comboBox2.SelectedIndex
		ColorIndex = self._comboBox3.SelectedIndex
		
		num *= 50
		
		num += [0,10,15][TypeIndex]
		num += [0,2,4,6][WidthIndex]
		num += [5,0,0,0,0][ColorIndex]
		
		self._label5.Text = "It will cost $"+str(num)
		