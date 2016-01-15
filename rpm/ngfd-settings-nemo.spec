Name:       ngfd-settings-nemo

Summary:    NGFD configuration for Nemo
Version:    0.0.2
Release:    1
Group:      System/Library
License:    LGPL 2.1
BuildArch:  noarch
URL:        https://github.com/nemomobile-ux/ngfd-settings-nemo
Source0:    %{name}-%{version}.tar.gz
Requires:   ngfd
Conflicts:  ngfd-settings-basic
Provides:   ngfd-settings

%description
NGFD configuration for Nemo

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_datadir}/ngfd/
install -d %{buildroot}/%{_datadir}/ngfd/events.d/
install -d %{buildroot}/%{_datadir}/ngfd/plugins.d/
install -m 644 data/ngfd.ini %{buildroot}/%{_datadir}/ngfd/
install -m 644 data/events.d/* %{buildroot}/%{_datadir}/ngfd/events.d/
install -m 644 data/plugins.d/* %{buildroot}/%{_datadir}/ngfd/plugins.d/

%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/ngfd/
