%define debug_package %{nil}
Name:aris-elk-installer
Version:0.1
Release:1%{?dist}
Summary:Aris ELK Stack Installer
License:GPL
URL:www.arissystem.com
BuildArch:x86_64
Requires:aris-elk-installer-prerequisites elasticsearch logstash nginx java-1.8.0-openjdk openssl httpd-tools
Source: aris-elk-installer.tar.gz
Autoreq: 0

%description
This package installs and configures ELK Stack (Elastic-Logstash-Kibana) and also protects Kibana UI with password using Nginx Proxy.
Elastic Search: 1.7.x
Logstash: 1.5.x
Kibana: 4.1.1
Run the following command in order to set the admin password for the web UI.
"htpasswd -c /etc/nginx/conf.d/kibana.htpasswd admin"
%prep
%setup -q -n %{name}

%build

%install

mkdir -p %buildroot/opt/kibana4
mkdir -p %buildroot/etc/nginx/conf.d/
mkdir -p %buildroot/etc/logstash/conf.d/
mkdir -p %buildroot/etc/init.d/

cp -R kibana-4.1.1-linux-x64/* %buildroot/opt/kibana4/
cp logstash_syslogs.conf %buildroot/etc/logstash/conf.d/logstash_syslogs.conf
cp kibana4 %buildroot/etc/init.d/
cp kibana4.conf  %buildroot/etc/nginx/conf.d/

%clean

%files
/opt/kibana4/*
%config /etc/logstash/conf.d/logstash_syslogs.conf
%config /etc/nginx/conf.d/kibana4.conf
%attr(755, root, root) /etc/init.d/kibana4

%changelog

%pre

%post

sed -i 's/#pid_file/pid_file/g' /opt/kibana4/config/kibana.yml

cd /etc/pki/tls

openssl req -x509 -nodes -newkey rsa:2048 -days 365 -keyout private/logstash-forwarder.key -out certs/logstash-forwarder.crt -subj /CN=$(hostname)

service elasticsearch start
service logstash start
service kibana4 start
service nginx start
chkconfig --add elasticsearch
chkconfig --add logstash
chkconfig --add kibana4
chkconfig --add nginx

%preun
service elasticsearch stop
service logstash stop
service kibana4 stop
service nginx stop
chkconfig --del elasticsearch
chkconfig --del logstash
chkconfig --del kibana4
chkconfig --del nginx

