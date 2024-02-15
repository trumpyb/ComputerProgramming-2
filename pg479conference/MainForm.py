import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._txtName = System.Windows.Forms.TextBox()
		self._txtCompany = System.Windows.Forms.TextBox()
		self._txtAddress = System.Windows.Forms.TextBox()
		self._txtCity = System.Windows.Forms.TextBox()
		self._txtPhone = System.Windows.Forms.TextBox()
		self._txtEmail = System.Windows.Forms.TextBox()
		self._txtState = System.Windows.Forms.TextBox()
		self._txtZip = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._lblCost = System.Windows.Forms.Label()
		self._btnSelect = System.Windows.Forms.Button()
		self._btnReset = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._txtZip)
		self._groupBox1.Controls.Add(self._txtState)
		self._groupBox1.Controls.Add(self._txtEmail)
		self._groupBox1.Controls.Add(self._txtPhone)
		self._groupBox1.Controls.Add(self._txtCity)
		self._groupBox1.Controls.Add(self._txtAddress)
		self._groupBox1.Controls.Add(self._txtCompany)
		self._groupBox1.Controls.Add(self._txtName)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(520, 184)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Registrant"
		# 
		# txtName
		# 
		self._txtName.Location = System.Drawing.Point(113, 33)
		self._txtName.Name = "txtName"
		self._txtName.Size = System.Drawing.Size(100, 20)
		self._txtName.TabIndex = 0
		# 
		# txtCompany
		# 
		self._txtCompany.Location = System.Drawing.Point(113, 59)
		self._txtCompany.Name = "txtCompany"
		self._txtCompany.Size = System.Drawing.Size(100, 20)
		self._txtCompany.TabIndex = 1
		# 
		# txtAddress
		# 
		self._txtAddress.Location = System.Drawing.Point(113, 85)
		self._txtAddress.Name = "txtAddress"
		self._txtAddress.Size = System.Drawing.Size(100, 20)
		self._txtAddress.TabIndex = 2
		# 
		# txtCity
		# 
		self._txtCity.Location = System.Drawing.Point(113, 111)
		self._txtCity.Name = "txtCity"
		self._txtCity.Size = System.Drawing.Size(100, 20)
		self._txtCity.TabIndex = 3
		# 
		# txtPhone
		# 
		self._txtPhone.Location = System.Drawing.Point(361, 33)
		self._txtPhone.Name = "txtPhone"
		self._txtPhone.Size = System.Drawing.Size(100, 20)
		self._txtPhone.TabIndex = 4
		# 
		# txtEmail
		# 
		self._txtEmail.Location = System.Drawing.Point(361, 60)
		self._txtEmail.Name = "txtEmail"
		self._txtEmail.Size = System.Drawing.Size(100, 20)
		self._txtEmail.TabIndex = 5
		# 
		# txtState
		# 
		self._txtState.Location = System.Drawing.Point(255, 137)
		self._txtState.Name = "txtState"
		self._txtState.Size = System.Drawing.Size(100, 20)
		self._txtState.TabIndex = 6
		# 
		# txtZip
		# 
		self._txtZip.Location = System.Drawing.Point(398, 137)
		self._txtZip.Name = "txtZip"
		self._txtZip.Size = System.Drawing.Size(100, 20)
		self._txtZip.TabIndex = 7
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 8
		self._label1.Text = "Name"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 9
		self._label2.Text = "Company"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 82)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 10
		self._label3.Text = "Address"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(7, 111)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 11
		self._label4.Text = "City"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(255, 30)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 12
		self._label5.Text = "Phone"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(255, 63)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 13
		self._label6.Text = "Email"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(255, 98)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 14
		self._label7.Text = "State"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(398, 98)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 15
		self._label8.Text = "Zip"
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(13, 204)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 1
		self._label9.Text = "Total Cost"
		# 
		# lblCost
		# 
		self._lblCost.Location = System.Drawing.Point(120, 203)
		self._lblCost.Name = "lblCost"
		self._lblCost.Size = System.Drawing.Size(100, 23)
		self._lblCost.TabIndex = 2
		# 
		# btnSelect
		# 
		self._btnSelect.Location = System.Drawing.Point(20, 256)
		self._btnSelect.Name = "btnSelect"
		self._btnSelect.Size = System.Drawing.Size(93, 57)
		self._btnSelect.TabIndex = 3
		self._btnSelect.Text = "&Select Conference Options"
		self._btnSelect.UseVisualStyleBackColor = True
		# 
		# btnReset
		# 
		self._btnReset.Location = System.Drawing.Point(214, 256)
		self._btnReset.Name = "btnReset"
		self._btnReset.Size = System.Drawing.Size(100, 57)
		self._btnReset.TabIndex = 4
		self._btnReset.Text = "&Reset"
		self._btnReset.UseVisualStyleBackColor = True
		self._btnReset.Click += self.BtnResetClick
		# 
		# btnExit
		# 
		self._btnExit.Location = System.Drawing.Point(423, 257)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(88, 56)
		self._btnExit.TabIndex = 5
		self._btnExit.Text = "&Exit"
		self._btnExit.UseVisualStyleBackColor = True
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(554, 440)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnReset)
		self.Controls.Add(self._btnSelect)
		self.Controls.Add(self._lblCost)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg479conference"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	

	def BtnExitClick(self, sender, e):
		Application.Exit()

	def BtnResetClick(self, sender, e):
		self._txtName.Text = ""
		self._txtCompany.Text = ""
		self._txtAddress.Text = ""
		self._txtCity.Text = ""
		self._txtPhone.Text = ""
		self._txtEmail.Text = ""
		self._txtState.Text = ""
		self._txtZip.Text = ""