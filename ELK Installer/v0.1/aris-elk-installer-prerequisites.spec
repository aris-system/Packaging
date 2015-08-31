%define debug_package %{nil}
Name:aris-elk-installer-prerequisites
Version:0.1
Release:1%{?dist}
Summary:Aris ELK Stack Installer Prerequisites
License:GPL
URL:www.arissystem.com
BuildArch:x86_64
Requires:epel-release
Source: aris-elk-installer-prerequisites.tar.gz
Autoreq: 0

%description
This package installs prerequisite repositories for ELK installation including repositories.
EPEL Repo.
Elastic Search Repo.
Logstash Repo.

%prep
%setup -q -n %{name}

%build

%install

mkdir -p %buildroot/etc/yum.repos.d/

cp elasticsearch.repo %buildroot/etc/yum.repos.d/
cp logstash.repo %buildroot/etc/yum.repos.d/

%clean

%files
/etc/yum.repos.d/elasticsearch.repo
/etc/yum.repos.d/logstash.repo
%changelog

%pre

%post
%postun
