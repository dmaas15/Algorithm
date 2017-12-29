'x=MsgBox("Hello")
'MsgBox("Hello")

'x=InputBox("Do You Want to Continue with DNA Purification? (N/Y)")
'MsgBox(x)
'Evoware.SetStringVariable "DNA",x

Dim msgBoxResponse
msgBoxResponse=MsgBox("Do you want to run DNA Purification?", vbYesNoCancel)
Select Case msgBoxResponse
	Case vbYes: Evoware.SetStringVariable "DNA", "Y"
	Case vbNo: Evoware.SetStringVariable "DNA", "N"
	Case vbCancel: 
End Select