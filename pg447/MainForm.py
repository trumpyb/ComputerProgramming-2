import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._lblMessage = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._colorToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._redToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._greenToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._blueToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._blackToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._visibleToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# lblMessage
		# 
		self._lblMessage.Location = System.Drawing.Point(13, 410)
		self._lblMessage.Name = "lblMessage"
		self._lblMessage.Size = System.Drawing.Size(100, 23)
		self._lblMessage.TabIndex = 0
		self._lblMessage.Text = "Hello, world!"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._fileToolStripMenuItem,
			self._colorToolStripMenuItem,
			self._helpToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(884, 24)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# fileToolStripMenuItem
		# 
		self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._exitToolStripMenuItem]))
		self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
		self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 20)
		self._fileToolStripMenuItem.Text = "&File"
		# 
		# exitToolStripMenuItem
		# 
		self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
		self._exitToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._exitToolStripMenuItem.Text = "&Exit"
		# 
		# colorToolStripMenuItem
		# 
		self._colorToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._redToolStripMenuItem,
			self._greenToolStripMenuItem,
			self._blueToolStripMenuItem,
			self._blackToolStripMenuItem,
			self._visibleToolStripMenuItem]))
		self._colorToolStripMenuItem.Name = "colorToolStripMenuItem"
		self._colorToolStripMenuItem.Size = System.Drawing.Size(48, 20)
		self._colorToolStripMenuItem.Text = "&Color"
		# 
		# redToolStripMenuItem
		# 
		self._redToolStripMenuItem.Name = "redToolStripMenuItem"
		self._redToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._redToolStripMenuItem.Text = "&Red"
		# 
		# greenToolStripMenuItem
		# 
		self._greenToolStripMenuItem.Name = "greenToolStripMenuItem"
		self._greenToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._greenToolStripMenuItem.Text = "&Green"
		# 
		# blueToolStripMenuItem
		# 
		self._blueToolStripMenuItem.Name = "blueToolStripMenuItem"
		self._blueToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._blueToolStripMenuItem.Text = "&Blue"
		# 
		# blackToolStripMenuItem
		# 
		self._blackToolStripMenuItem.Name = "blackToolStripMenuItem"
		self._blackToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._blackToolStripMenuItem.Text = "Blac&k"
		# 
		# helpToolStripMenuItem
		# 
		self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._aboutToolStripMenuItem]))
		self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
		self._helpToolStripMenuItem.Size = System.Drawing.Size(44, 20)
		self._helpToolStripMenuItem.Text = "Help"
		# 
		# aboutToolStripMenuItem
		# 
		self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
		self._aboutToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._aboutToolStripMenuItem.Text = "About"
		# 
		# visibleToolStripMenuItem
		# 
		self._visibleToolStripMenuItem.Name = "visibleToolStripMenuItem"
		self._visibleToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._visibleToolStripMenuItem.Text = "Visible"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(884, 445)
		self.Controls.Add(self._lblMessage)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "pg447"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

