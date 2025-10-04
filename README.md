# Netaccess-IITM

This package automates the netacess process used in IIT Madras. 

# Dependancies

This need *selenium*

| Package name | Vesrion|
|--------------|---------|
| Google Chrome| Latest veriosn| 
| selenium     | 4.35.0 |

Code is tested with above packages but will (mostly) work with older versions.

# How to use

Download the code.

```
cd ~/.
git clone https://github.com/JayeshMD/Netaccess-IITM.git
```

## Step 1: Setting up python
Enter into Netaccess-IITM folder and create virtual environment.

```
cd ~/Netaccess-IITM 
python3 -m venv venv_netaccess
```

activate virtual environment.

```
source ~/Netaccess-IITM/venv_netaccess/bin/activate
```
You can install *selenium* using following command.

```
pip install selenium
```

For linux or Mac systems you can open terminal and type, 
```
which python3
```
to obtain path of python.

## Step 2: Default python path for netaccess

Open **netaccess.py** and modify the first line to path of python3.

```
#!path_to_python_bin/python3
```

This is the location of python which you installed selenium. See following example.

```
#!~/Netaccess-IITM/venv_netaccess/bin/python3
```

## Step 3: Provide *username* and *password*

Run **netaccess.py** and provide username and password.

```
~/Netaccess-IITM/netaccess.py 
```

## Step 4: Setup to repeat approval process

For linux and Mac systems open terminal and type,
```
crontab -e
```

(if asked choose your favorite editor).
Add following line with 

```
0 */12 * * * (cd ~/Netaccess-IITM && ./netaccess.py > log_netacc && echo $(date) > log_time)
```

Now onwards the appoval will happen every 12 hours (12 am & 12 pm).

To do the this setup at other location modity the paths accordingly.




