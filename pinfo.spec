Summary:	Lynx-style info and man browser
Summary(pl):	Przêgl±darka info i manuali w stylu lynx'a
Name:		pinfo
Version:	0.3.7
Release:	2
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Copyright:	GPL
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source:		http://zeus.polsl.gliwice.pl/~pborys/%{name}-%{version}.tar.gz
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Pinfo is a curses based lynx-style info and man browser.

%description -l pl
Pinfo jest przegl±dark± dokumentów info i stron man podobn± do lynx'a.

%prep
%setup -q

%build
make SPEEDOPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{man/man1,bin}

install -s pinfo $RPM_BUILD_ROOT/usr/bin
install	 pinfo.1 $RPM_BUILD_ROOT/usr/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*
gzip -9nf ACKNOWLEDGEMENTS CHANGELOG TODO TECHSTUFF README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ACKNOWLEDGEMENTS,CHANGELOG,TODO,TECHSTUFF,README}.gz
%attr(755,root,root) /usr/bin/pinfo
/usr/man/man1

%changelog
* Sun Mar 28 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.3.7-2]
- upgraded to 0.3.7
- added (gzipped) documentation

* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.5-1]
- fixed passing $RPM_OPT_FLAGS.

* Mon Mar 23 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.3.1-1]
- upgraded to 0.3.1

* Sun Mar 21 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.2.4-1]
- upgraded to 0.2.4

* Fri Mar 19 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.2.3-1]
- initial RPM release
