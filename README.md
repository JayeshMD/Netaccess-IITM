# Netaccess

This package automates the netacess process used in IIT Madras. 

# Dependancies

This need \emph{selenium}

| Package name | Vesrion|
|--------------|---------
| selenium     | 4.35.0|

You can install it using following command.

```
pip install selenium
```

# How to use

Download the code.

```
git clone https://github.com/JayeshMD/Netaccess-IITM.git
```

## Step 1: Setting up python
Open **netaccess.py** and modify the first line to path of python3.

```
#!path_to_python_bin/python3
```

This is the location of python which you installed selenium. See following example.

```
#!/usr/bin/python3
```

For linux or Mac systems you can open terminal and type, 
```
where python3
```
to obtain path of python.

## Step 2: Provide user user name and password

Open **netaccess.py** and provide your user name and password.

```
userName = "type your user name"
password = "password"
```

## Step 3: Setup to repeat approval process

For linux and Mac systems open terminal and type,
```
crontab -e
```

(if asked choose your favorite editor).
Add following line with 

```
0 */12 * * * (cd path_to_netaccss_folder && ./netaccess.py > log_netacc && echo $(date) > log_time)
```

Now onwards the appoval will happen every 12 hours (12 am & 12 pm).




