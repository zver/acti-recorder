Name: acti-recorder
Version: 0.1
Release: 1

Summary: Recording video from acti cameras
License: GPLv3
Group: Monitoring

Url: https://github.com/zver/acti-recorder
BuildArch: noarch

Requires: bc

Source: %name-%version.tar
Source1: README


%description
Simple script for record video from ACTI camera.
acti-recorder start recording when motion was detected.

%prep
%setup

%build

%install
ls -la 
install -pD %SOURCE1 %{buildroot}usr/share/doc/%name-%version/README
%makeinstall_std


%files
%_bindir/*
%_sysconfdir/*.conf

%changelog
* Sat Dec 18 2010 Denis Klimov <zver@altlinux.org> 0.1-1
- Initial package for ALT Linux

