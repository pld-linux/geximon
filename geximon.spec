Summary:	GTK+ Exim Monitor
Summary(pl):	Monitor Exima oparty na GTK+
Name:		geximon
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://pov.lt/geximon/%{name}-%{version}.tar.gz
# Source0-md5:	29c65614249e7d0e4dd376cfa085a0d5
URL:		http://pov.lt/geximon/
BuildRequires:	python-devel
Requires:	python-pygtk-gtk >= 1.99.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ Exim Monitor - GTK+-based clone of eximon, the exim server monitor.

%description -l pl
GTK+ Exim Monitor - oparty na GTK+ monitor Exima bêd±cy klonem eximona.

%prep
%setup -q

%build
./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/geximon,%{_desktopdir}}

./setup.py install \
	--prefix=$RPM_BUILD_ROOT/usr

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
%{_mandir}/man8/geximon.8*
%{_datadir}/omf/%{name}
%{_pixmapsdir}/*
%{py_sitescriptdir}/%{name}
