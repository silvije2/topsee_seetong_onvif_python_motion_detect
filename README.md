***WARNING***
Please do NOT expose any IP Camera or it's web interface on public IP address! Most of them are vulnerable to unauthorized public access through onvif!
To confirm this use ONVIF Device Manager

	https://sourceforge.net/projects/onvifdm/

Tpsee Topsee Seetong SkyVision Tianshitong 天视通 ***ARE*** vulnerable without any doubt!

To find how many 天视通 cameras are publicly exposed in 2020 you can use link below:

	https://www.zoomeye.org/searchResult?q=IPCConfig.exe%3Fversion%20%2Bafter:%222020-01-01%22%20%2Bbefore:%222021-01-01%22&t=all

***WARNING*** If using Topsee/Seetong PC client or mobile apps, keep in mind that communication is unencrypted, and your usernames, passwords and e-mail address are visible on the network



# topsee_seetong_onvif_python_motion_detect

Tpsee Topsee Seetong Tianshitong SkyVision 天视通 IPC ONVIF python motion detect script

With this script you can subscribe to IPC motion detect events and then run whatever you want when event fires.

Edit credentials in the begining of the script. On some IPC models and (buggy) firmwares, script works only if you leave default factory username and password configured. On some models script works fine with older firmwares and stop working after firmware upgrade. Seems Onvif support is not well maintained. Contacting Topsee poor "Technical after services" people with this problem didn't help at all.

Script also shows various IPC information like model, firmware version, serial number and so on...

## Prerequisites

You need to install python3-pip, onvif-py3 and suds-passworddigest-py3

## Installing

Run following commands:

```
apt-get install python3-pip
pip3 install onvif-py3
pip3 install git+https://github.com/miuhaki/suds-passworddigest-py3.git
```

## Running

To run a script type following command:

```
python3 motion_detect.py
```

## Authors

* **Silvije2** [Github](https://github.com/silvije2/)

## License

GPL-3.0-or-later

