##Save docker image to a zip archive
```docker save -o ubuntu.zip ubuntu:18.04```  
##Install 7zip
```apt install p7zip-full```
##Extract files from ubuntu.zip
```7z x ubuntu.zip -o./Ubuntu_extract_files/```
