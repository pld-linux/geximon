Summary:	GTK Exim Monitor
Name:		geximon
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://pov.lt/geximon/%{name}-%{version}.tar.gz
# Source0-md5:	29c65614249e7d0e4dd376cfa085a0d5
URL:	http://pov.lt/geximon
Requires:	python-pygtk
Requires:	python-pygtk-gtk >= 1.99.16
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Exim Monitor

%prep
%setup -q

%build
./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/geximon,%{_desktopdir}}

./setup.py install --prefix=$RPM_BUILD_ROOT/usr

%py_comp $RPM_BUILD_ROOT%{_datadir}/geximon
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/geximon

find  $RPM_BUILD_ROOT%{_datadir}/geximon -name "*.py" -exec rm -f {} \;

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/geximon

%{_mandir}/man8/geximon.8.gz
%{_datadir}/omf/%{name}
%{_pixmapsdir}/*
%{_datadir}/python2.3/site-packages/%{name}
