import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._txtInput = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._lblOutput = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# txtInput
		# 
		self._txtInput.Location = System.Drawing.Point(119, 88)
		self._txtInput.Name = "txtInput"
		self._txtInput.Size = System.Drawing.Size(640, 20)
		self._txtInput.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 127)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Duplicates: "
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 183)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 183)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(174, 183)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Exter Text:"
		# 
		# lblOutput
		# 
		self._lblOutput.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._lblOutput.Location = System.Drawing.Point(120, 127)
		self._lblOutput.Name = "lblOutput"
		self._lblOutput.Size = System.Drawing.Size(639, 43)
		self._lblOutput.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonFace
		self.ClientSize = System.Drawing.Size(895, 431)
		self.Controls.Add(self._lblOutput)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._txtInput)
		self.Name = "MainForm"
		self.Text = "strint1"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		self._lblOutput.Text = ""
		string = self._txtInput.Text.lower()
		
		duplicates = []
		
		for x in string:
			if string.count(x)>1 and x not in duplicates:
				duplicates.append(x)
				
		for x in duplicates:
			self._lblOutput.Text += x + " "

	def Button2Click(self, sender, e):
		self._lblOutput.Text = ""
		self._txtInput.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()