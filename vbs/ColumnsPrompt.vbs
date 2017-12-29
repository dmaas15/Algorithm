'x=MsgBox("Hello")
'MsgBox("Hello")

'x=InputBox("Do You Want to Continue with DNA Purification? (N/Y)")
'MsgBox(x)
'Evoware.SetStringVariable "DNA",x

Dim msgBoxResponse
'msgBoxResponse=MsgBox("Do you want to run DNA Purification?", vbYesNoCancel)
'Select Case msgBoxResponse
'	Case vbYes: Evoware.SetStringVariable "DNA", "Y"
'	Case vbNo: Evoware.SetStringVariable "DNA", "N"
'	Case vbCancel: 
'End Select

'TipBox Array for tipsthat are put in back carrier
Dim tipBox(11)
tipBox(0)=0
tipBox(1)=4
tipBox(2)=5
tipBox(3)=8
tipBox(4)=9
tipBox(5)=12
tipBox(6)=13
tipBox(7)=16
tipBox(8)=17
tipBox(9)=20
tipBox(10)=21
tipBox(11)=24
'tipBox(12)=24

tipBoxIndex=0
colTipBox=12

numCol=InputBox("Enter number of Sample Columns: (1,2,3,4,6,or 12):","Input Required","0")
Select Case numCol
	Case "1", "2", "3","4","6","12":
		msgBoxResponse=MsgBox("You enter "&numCol&" Columns", vbYesNoCancel)
	Case Else:
		msgBoxResponse=MsgBox("You entered an invalid number of Columns!", vbAbort)
End Select


For iTransfer = 1 to 23
	column=colTipBox-(numCol*iTransfer)
	
	If tipBoxIndex>11 Then
		msgBoxResponse=msgBox("Please Refresh Tip Boxes!",vbOK)
		tipBoxIndex=0
	End If
	
	msgBoxResponse=msgBox("Transfer: "&iTransfer&" TB: "&tipBox(tipBoxIndex)&" Col: "&column,vbOK)
	
	If column=0 Then
		colTipBox=colTipBox+12
		tipBoxIndex=tipBoxIndex+1
	End If
	

Next