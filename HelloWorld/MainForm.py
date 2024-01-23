import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._show = System.Windows.Forms.Button()
		self._clear = System.Windows.Forms.Button()
		self._exit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label1.Location = System.Drawing.Point(167, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(450, 106)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# show
		# 
		self._show.Location = System.Drawing.Point(167, 188)
		self._show.Name = "show"
		self._show.Size = System.Drawing.Size(149, 73)
		self._show.TabIndex = 1
		self._show.Text = "Show"
		self._show.UseVisualStyleBackColor = True
		self._show.Click += self.Button1Click
		# 
		# clear
		# 
		self._clear.Location = System.Drawing.Point(322, 188)
		self._clear.Name = "clear"
		self._clear.Size = System.Drawing.Size(137, 73)
		self._clear.TabIndex = 2
		self._clear.Text = "Clear"
		self._clear.UseVisualStyleBackColor = True
		self._clear.Click += self.ClearClick
		# 
		# exit
		# 
		self._exit.Location = System.Drawing.Point(465, 188)
		self._exit.Name = "exit"
		self._exit.Size = System.Drawing.Size(152, 73)
		self._exit.TabIndex = 3
		self._exit.Text = "Exit"
		self._exit.UseVisualStyleBackColor = True
		self._exit.Click += self.ExitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(872, 426)
		self.Controls.Add(self._exit)
		self.Controls.Add(self._clear)
		self.Controls.Add(self._show)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "HelloWorld"
		self.ResumeLayout(False)
		
		

	def Button1Click(self, sender, e):
		self._label1.Text = "Hello, world!"

	def ClearClick(self, sender, e):
		self._label1.Text = ""

	def ExitClick(self, sender, e):
		Application.Exit()

	def Label1Click(self, sender, e):
		pass