# topsee_seetong_onvif_python_motion_detect

Tpsee Topsee Seetong IPC ONVIF python motion detect script

With this script you can subscribe to IPC motion detect events and then run whatever you want when event fires.

Edit credentials in the begining of the script. On some IPC models and (buggy) firmwares, script works only if you leave default factory username and password configured.

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

