Summary: NethServer net-snmp service
Name: nethserver-net-snmp
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: nethserver-base
Requires: net-snmp
AutoReq: no


%description
NethServer configuration for net-snmp daemon.


%preun

%post

%prep
%setup

%build
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT   > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}-%{version}-%{release}-filelist 
%defattr(-,root,root)

%changelog
* Thu Apr 09 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- SNMP support - Feature #2945 [NethServer]

