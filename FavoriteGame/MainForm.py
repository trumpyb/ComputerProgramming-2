import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._Show = System.Windows.Forms.Button()
		self._Clear = System.Windows.Forms.Button()
		self._exit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(307, 54)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		# 
		# Show
		# 
		self._Show.Location = System.Drawing.Point(61, 124)
		self._Show.Name = "Show"
		self._Show.Size = System.Drawing.Size(75, 23)
		self._Show.TabIndex = 1
		self._Show.Text = "Show"
		self._Show.UseVisualStyleBackColor = True
		self._Show.Click += self.ShowClick
		# 
		# Clear
		# 
		self._Clear.Location = System.Drawing.Point(237, 124)
		self._Clear.Name = "Clear"
		self._Clear.Size = System.Drawing.Size(75, 23)
		self._Clear.TabIndex = 2
		self._Clear.Text = "Clear"
		self._Clear.UseVisualStyleBackColor = True
		self._Clear.Click += self.ClearClick
		# 
		# exit
		# 
		self._exit.Location = System.Drawing.Point(449, 124)
		self._exit.Name = "exit"
		self._exit.Size = System.Drawing.Size(75, 23)
		self._exit.TabIndex = 3
		self._exit.Text = "Exit"
		self._exit.UseVisualStyleBackColor = True
		self._exit.Click += self.ExitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(890, 442)
		self.Controls.Add(self._exit)
		self.Controls.Add(self._Clear)
		self.Controls.Add(self._Show)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "FavoriteGame"
		self.ResumeLayout(False)


	def ShowClick(self, sender, e):
		self._label1.Text = "Chess"

	def ClearClick(self, sender, e):
		self._label1.Text = ""

	def ExitClick(self, sender, e):
		Application.Exit()