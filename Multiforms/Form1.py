
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.myparent = parent
		self.message = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 39)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(248, 210)
		self._button1.TabIndex = 1
		self._button1.Text = "Show home form"
		self._button1.UseVisualStyleBackColor = True
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.FormClosing += self.Form1FormClosing
		self.Load += self.Form1Load
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.myparent.Show()

	def Form1Load(self, sender, e):
		self._label1.text = self.message

	def Form1FormClosing(self, sender, e):
		self.myparent.Show()