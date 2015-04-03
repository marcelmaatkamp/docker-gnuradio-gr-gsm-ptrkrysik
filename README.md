# docker-gnuradio-gr-gsm-ptrkrysik

Start the image with extra privileges to access the rtlsdr dongle and expose a ssh-port: 
```
 $ docker run -ti -p 2224:22 --privileged marcelmaatkamp/gnuradio-gr-gsm-ptrkrys:latest
 
 root@gnuradio-gr-gsm-ptrkrys# /usr/sbin/sshd
```

SSH into the box with X-forwarding enabled:
```
  ssh -X -p 2224 root@dockerhost
  
  root@gnuradio-gr-gsm-ptrkrys# locale-gen en_US en_US.UTF-8
  root@gnuradio-gr-gsm-ptrkrys# airprobe_rtlsdr.py
```
