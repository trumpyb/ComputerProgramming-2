import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._Show = System.Windows.Forms.Button()
		self._clear = System.Windows.Forms.Button()
		self._Exit = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# Show
		# 
		self._Show.Location = System.Drawing.Point(45, 45)
		self._Show.Name = "Show"
		self._Show.Size = System.Drawing.Size(75, 23)
		self._Show.TabIndex = 0
		self._Show.Text = "Show"
		self._Show.UseVisualStyleBackColor = True
		self._Show.Click += self.ShowClick
		# 
		# clear
		# 
		self._clear.Location = System.Drawing.Point(180, 45)
		self._clear.Name = "clear"
		self._clear.Size = System.Drawing.Size(75, 23)
		self._clear.TabIndex = 1
		self._clear.Text = "Clear"
		self._clear.UseVisualStyleBackColor = True
		self._clear.Click += self.ClearClick
		# 
		# Exit
		# 
		self._Exit.Location = System.Drawing.Point(301, 45)
		self._Exit.Name = "Exit"
		self._Exit.Size = System.Drawing.Size(75, 23)
		self._Exit.TabIndex = 2
		self._Exit.Text = "Exit"
		self._Exit.UseVisualStyleBackColor = True
		self._Exit.Click += self.ExitClick
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(155, 170)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(230, 111)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(661, 374)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._Exit)
		self.Controls.Add(self._clear)
		self.Controls.Add(self._Show)
		self.Name = "MainForm"
		self.Text = "names"
		self.ResumeLayout(False)


	def ShowClick(self, sender, e):
		self._label1.Text = "Ben"

	def ClearClick(self, sender, e):
		self._label1.Text = ""

	def ExitClick(self, sender, e):
		Application.Exit()