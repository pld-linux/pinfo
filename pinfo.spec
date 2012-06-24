Summary:	Lynx-style info browser
Summary(pl):	Prz�gl�darka info w stylu lynx'a
Name:		pinfo
Version:	0.3.1
Release:	1
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Copyright:	GPL
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source:		http://zeus.polsl.gliwice.pl/~pborys/%{name}-%{version}.tar.gz
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Pinfo is a curses based lynx-style info browser.

%description -l pl
Pinfo jest przegl�dark� dokument�w info podobn� do lynx'a.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{man/man1,bin}

install -s pinfo $RPM_BUILD_ROOT/usr/bin
install	 pinfo.1 $RPM_BUILD_ROOT/usr/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/pinfo
/usr/man/man1

%changelog
* Mon Mar 23 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [0.3.1-1]
- upgraded to 0.3.1

* Sun Mar 21 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [0.2.4-1]
- upgraded to 0.2.4

* Fri Mar 19 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [0.2.3-1]
- initial RPM release
