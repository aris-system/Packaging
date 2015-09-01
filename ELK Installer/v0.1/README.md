These two packages install and configure ELK stack on RHEL6.
ELK stands for Elasticsearch, Logstash and Kibana. Projects brought to you by Elastic, that help you to search, analyze, and visualize your data, allowing you to get actionable insight in real time. Included versions are:
ElasticSearch: 1.7.x
Logstash: 1.5.x
Kibana: 4.1.1

The package "aris-elk-installer-prerequisites-0.1-1.el6.x86_64.rpm" adds three official repositories for Elasticsearch, Logstash and EPEL, which are required for ELK installer package called "aris-elk-installer-0.1-1.el6.x86_64.rpm".
The package "aris-elk-installer-0.1-1.el6.x86_64.rpm" installs all ELK stack applications on your machine and configures logstash to listen on port 5050 for lumberjack input. It also restricts kibana access through local Nginx Proxy. So make sure you dont have a web server listening on ports 80 and 443 before installing the package.

Run the following command in order to set the admin password for the web UI.
"htpasswd -c /etc/nginx/conf.d/kibana.htpasswd admin"
kibana UI will be accessible through https://<your-ip>.

Also there is a known issue with this installer which comes from the bug in Logstash and Elasticsearch packages in official repositories. If you install then remove and then install the packages again, you may experience problems with starting Logstash and Elasticsearch and you may have to delete the leftover files manually. We hope this bug will be fixed soon by Elastic.

to install packages with their dependencies run:

yum localinstall aris-elk-installer-prerequisites-0.1-1.el6.x86_64.rpm
yum localinstall aris-elk-installer-0.1-1.el6.x86_64.rpm

Kianoosh Kashefi

Arissystem
