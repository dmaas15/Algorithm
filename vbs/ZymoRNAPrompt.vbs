'x=MsgBox("Hello")
'MsgBox("Hello")
'x=InputBox("Do You Want to Continue with RNA Purification? (N/Y)")
'MsgBox(x)
'Evoware.SetStringVariable "RNA",x

Dim msgBoxResponse
msgBoxResponse=MsgBox("Do you want to run RNA Purification?", vbYesNoCancel)
Select Case msgBoxResponse
	Case vbYes: Evoware.SetStringVariable "RNA", "Y"
	Case vbNo: Evoware.SetStringVariable "RNA", "N"
	Case vbCancel: 
End Select