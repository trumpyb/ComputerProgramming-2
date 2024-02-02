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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._GripTape = System.Windows.Forms.CheckBox()
		self._Bearing = System.Windows.Forms.CheckBox()
		self._Riser = System.Windows.Forms.CheckBox()
		self._nuts = System.Windows.Forms.CheckBox()
		self._Assembly = System.Windows.Forms.CheckBox()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["The Master Thrasher $60",
			"The Dictator of Grind $45",
			"The Street King $50"]))
		self._comboBox1.Location = System.Drawing.Point(11, 36)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["7.75 axle $35",
			"8 axle $40",
			"8.5 axle $45"]))
		self._comboBox2.Location = System.Drawing.Point(138, 36)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 1
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["51 mm $20",
			"55 mm $22",
			"58 mm $24",
			"61 mm $28"]))
		self._comboBox3.Location = System.Drawing.Point(265, 37)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 2
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(11, 7)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(121, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Type of skateboard"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(139, 7)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(120, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Width of Axels"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(265, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(121, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Size of wheels"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(234, 78)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 23)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate Price"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(11, 282)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(271, 119)
		self._label5.TabIndex = 9
		# 
		# GripTape
		# 
		self._GripTape.Location = System.Drawing.Point(13, 64)
		self._GripTape.Name = "GripTape"
		self._GripTape.Size = System.Drawing.Size(104, 24)
		self._GripTape.TabIndex = 10
		self._GripTape.Text = "Grip tape $10"
		self._GripTape.UseVisualStyleBackColor = True
		# 
		# Bearing
		# 
		self._Bearing.Location = System.Drawing.Point(13, 94)
		self._Bearing.Name = "Bearing"
		self._Bearing.Size = System.Drawing.Size(104, 24)
		self._Bearing.TabIndex = 11
		self._Bearing.Text = "Bearings $30"
		self._Bearing.UseVisualStyleBackColor = True
		# 
		# Riser
		# 
		self._Riser.Location = System.Drawing.Point(13, 125)
		self._Riser.Name = "Riser"
		self._Riser.Size = System.Drawing.Size(104, 24)
		self._Riser.TabIndex = 12
		self._Riser.Text = "Riser pads $ 2"
		self._Riser.UseVisualStyleBackColor = True
		# 
		# nuts
		# 
		self._nuts.Location = System.Drawing.Point(13, 156)
		self._nuts.Name = "nuts"
		self._nuts.Size = System.Drawing.Size(166, 24)
		self._nuts.TabIndex = 13
		self._nuts.Text = "Nuts + bolts kit $ 3"
		self._nuts.UseVisualStyleBackColor = True
		# 
		# Assembly
		# 
		self._Assembly.Location = System.Drawing.Point(13, 186)
		self._Assembly.Name = "Assembly"
		self._Assembly.Size = System.Drawing.Size(134, 24)
		self._Assembly.TabIndex = 15
		self._Assembly.Text = "Assembly $10"
		self._Assembly.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(893, 452)
		self.Controls.Add(self._Assembly)
		self.Controls.Add(self._nuts)
		self.Controls.Add(self._Riser)
		self.Controls.Add(self._Bearing)
		self.Controls.Add(self._GripTape)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "pg485sk8board"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		num = 0
		
		TypeIndex = self._comboBox1.SelectedIndex
		WidthIndex = self._comboBox2.SelectedIndex
		ColorIndex = self._comboBox3.SelectedIndex
		
		num += [60,45,50][TypeIndex]
		num += [35,40,45][WidthIndex]
		num += [20,22,24,28][ColorIndex]
		
		if self._GripTape.Checked:
			num += 10
		if self._Bearing.Checked:
			num += 30
		if self._Riser.Checked:
			num += 2
		if self._nuts.Checked:
			num += 3
		if self._Assembly.Checked:
			num += 10
		
		self._label5.Text = "It will cost $"+str(num)
		

