#https://github.com/silvije2/topsee_seetong_onvif_python_motion_detect/

from onvif import ONVIFCamera
import time
import daemon
import os

if __name__ == '__main__':
 #if you want to run script as a daemon uncomment following line
 #with daemon.DaemonContext():
    #edit credentials in following line
    mycam = ONVIFCamera('192.168.0.123', 80, 'admin', '123456')  # , no_cache=True)
    resp = mycam.devicemgmt.GetHostname()
    print('Hostname:\t' + str(resp.Name))

    resp = mycam.devicemgmt.GetDeviceInformation()
    print('Manufacturer:\t' + str(resp.Manufacturer))
    print('Model:\t\t' + str(resp.Model))
    print('Firmware:\t' + str(resp.FirmwareVersion).strip())
    print('Serial:\t\t' + str(resp.SerialNumber))
    print('Hardware ID:\t' + str(resp.HardwareId))

    resp = mycam.devicemgmt.GetNetworkInterfaces()
    print('IPv4 address:\t' + str(resp[0].IPv4.Config.Manual[0].Address))
    print('MAC address:\t' + str(resp[0].Info.HwAddress))

    media_service = mycam.create_media_service()
    profiles = media_service.GetProfiles()
    token = profiles[0]._token
    obj = media_service.create_type('GetStreamUri')
    obj.ProfileToken = token
    obj.StreamSetup.Stream = 'RTP-Unicast'
    obj.StreamSetup.Transport.Protocol = 'TCP'
    streamuri = media_service.GetStreamUri(obj)
    print('Main stream:\t' + str(streamuri.Uri))
    obj2 = media_service.create_type('GetSnapshotUri')
    obj2.ProfileToken = token
    snapuri = media_service.GetSnapshotUri(obj2)
    print('Snapshot URI:\t' + str(snapuri.Uri))

    token = profiles[1]._token
    obj.ProfileToken = token
    obj2.ProfileToken = token
    streamuri = media_service.GetStreamUri(obj)
    print('Sub stream:\t' + str(streamuri.Uri))
    snapuri = media_service.GetSnapshotUri(obj2)
    print('Snapshot URI:\t' + str(snapuri.Uri))

    print('\nTrying to subscribe to motion events...')
    params = mycam.events.create_type('CreatePullPointSubscription')
    params.Filter = "tns1:RuleEngine/CellMotionDetector"
    params.InitialTerminationTime = "PT10Y"
    pullpoint = mycam.events.CreatePullPointSubscription(params)
    print('Subscription reference:\t' + pullpoint.SubscriptionReference.Address)
    print('Current time:\t\t' + str(pullpoint.CurrentTime))
    print('Termination time:\t' + str(pullpoint.TerminationTime))

    pullpoint_service = mycam.create_pullpoint_service()
    req = pullpoint_service.create_type('PullMessages')
    req.MessageLimit = 1
    req.Timeout = 'PT5S'
    pullmess = pullpoint_service.PullMessages(req)
    print(pullmess)

    while True:
     time.sleep(4)
     pullmess = pullpoint_service.PullMessages(req)
     try:
      mcheck = pullmess.NotificationMessage[0].Message.Message.Data.SimpleItem._Value
      if mcheck:
       #here you put whatever command you want to run on motion event
       os.system("echo 'We have a motion' >> /var/log/motion_detect.log &")
       print(pullmess.CurrentTime, end=' ')
       print('Motion detected!')
     except AttributeError:
      pass
