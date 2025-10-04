# Netaccess-IITM

This package automates the netacess process used at IIT Madras. 

# Dependancies

This need *selenium*

| Package name | Vesrion|
|--------------|---------|
| Google Chrome| Latest veriosn| 
| selenium     | 4.35.0 |

The code is tested with the above packages, but will (mostly) work with older versions as well.

# How to use

Download the code.

```
cd ~/.
git clone https://github.com/JayeshMD/Netaccess-IITM.git
```

## Step 1: Setting up Python
Enter the Netaccess-IITM folder and create a virtual environment.

```
cd ~/Netaccess-IITM 
python3 -m venv venv_netaccess
```

Activate the virtual environment.

```
source ~/Netaccess-IITM/venv_netaccess/bin/activate
```
You can install **selenium** using the following command.

```
pip install selenium
```

## Step 2: Default Python path for netaccess 

For Linux or Mac systems, to obtain the path of Python you can open a terminal and run, 
```
which python3
```
Modify first line of the *netaccess.py* to add python interpreter path.

```
#!path_to_python3
```
For example,

```
#!/home/user/Netaccess-IITM/venv_netaccess/bin/python3
```
**Imporatnat: Add correct path. Above path is just an example.**

## Step 3: Provide *username* and *password*

Run **netaccess.py** and provide username and password.

```
~/Netaccess-IITM/netaccess.py 
```

## Step 4: Set up to repeat the approval process

For Linux and Mac systems, open a terminal and type,
```
crontab -e
```

(If asked, choose your favorite editor.)
Add the following line with 

```
0 */12 * * * (cd ~/Netaccess-IITM && ./netaccess.py > log_netacc && echo $(date) > log_time)
```

Henceforth, approvals will occur every 12 hours (12 am & 12 pm).

To do this setup at another location, modify the paths accordingly.




