# aci-cobra
https://github.com/datacenter/arya
https://10.37.1.11/cobra/_downloads/

jamie@HPEB:~/Documents$ mkdir aci-cobra
jamie@HPEB:~/Documents$ cd aci-cobra/
jamie@HPEB:~/Documents/aci-cobra$ virtualenv -p python3 venv
Running virtualenv with interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/jamie/Documents/aci-cobra/venv/bin/python3
Also creating executable in /home/jamie/Documents/aci-cobra/venv/bin/python
Installing setuptools, pip, wheel...
done.


(venv) jamie@HPEB:~/Documents/aci-cobra$ easy_install -Z ~/Downloads/acicobra-3.2_5e-py2.7.egg 
Processing acicobra-3.2_5e-py2.7.egg
.
Installed /home/jamie/Documents/aci-cobra/venv/lib/python2.7/site-packages/certifi-2019.3.9-py2.7.egg
Finished processing dependencies for acicobra===3.2-5e

(venv) jamie@HPEB:~/Documents/aci-cobra$ easy_install -Z ~/Downloads/acimodel-3.2_5e-py2.7.egg 
Processing acimodel-3.2_5e-py2.7.egg
.
Installed /home/jamie/Documents/aci-cobra/venv/lib/python2.7/site-packages/acimodel-3.2_5e-py2.7.egg
Processing dependencies for acimodel===3.2-5e
Finished processing dependencies for acimodel===3.2-5e


(venv) jamie@HPEB:~/Documents/aci-cobra$ git init
Initialized empty Git repository in /home/jamie/Documents/aci-cobra/.git/
(venv) jamie@HPEB:~/Documents/aci-cobra$ nano .gitignore
(venv) jamie@HPEB:~/Documents/aci-cobra$ cat .gitignore 
venv/
