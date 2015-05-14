Summary: NethServer net-snmp service
Name: nethserver-net-snmp
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}
BuildArch: noarch

BuildRequires: nethserver-devtools
Requires: nethserver-base
Requires: net-snmp

%description
NethServer configuration for net-snmp daemon.

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist 
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Apr 09 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- SNMP support - Feature #2945 [NethServer]

