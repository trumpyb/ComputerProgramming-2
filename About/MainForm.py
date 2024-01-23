import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._Show = System.Windows.Forms.Button()
		self._Clear = System.Windows.Forms.Button()
		self._Exit = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# Show
		# 
		self._Show.Location = System.Drawing.Point(13, 13)
		self._Show.Name = "Show"
		self._Show.Size = System.Drawing.Size(75, 23)
		self._Show.TabIndex = 0
		self._Show.Text = "Show"
		self._Show.UseVisualStyleBackColor = True
		self._Show.Click += self.ShowClick
		# 
		# Clear
		# 
		self._Clear.Location = System.Drawing.Point(109, 13)
		self._Clear.Name = "Clear"
		self._Clear.Size = System.Drawing.Size(75, 23)
		self._Clear.TabIndex = 1
		self._Clear.Text = "Clear"
		self._Clear.UseVisualStyleBackColor = True
		self._Clear.Click += self.ClearClick
		# 
		# Exit
		# 
		self._Exit.Location = System.Drawing.Point(191, 13)
		self._Exit.Name = "Exit"
		self._Exit.Size = System.Drawing.Size(75, 23)
		self._Exit.TabIndex = 2
		self._Exit.Text = "Exit"
		self._Exit.UseVisualStyleBackColor = True
		self._Exit.Click += self.ExitClick
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 39)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(253, 213)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._Exit)
		self.Controls.Add(self._Clear)
		self.Controls.Add(self._Show)
		self.Name = "MainForm"
		self.Text = "About"
		self.ResumeLayout(False)


	def ShowClick(self, sender, e):
		self._label1.Text = "My name is Benjamin Trumpy. I have learned Python, C++, TI Extended BASIC, Java, and HTML. I remember HTML, C++, Python and TI Extended BASIC"

	def ClearClick(self, sender, e):
		self._label1.Text = ""

	def ExitClick(self, sender, e):
		Application.Exit()