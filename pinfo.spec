Summary:	Lynx-style info browser
Summary(pl):	Przêgl±darka info w stylu lynx'a
Name:		pinfo	
Version:	0.5.4
Release:	1
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Copyright:	GPL
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source:		http://zeus.polsl.gliwice.pl/~pborys/%{name}-%{version}.tar.gz
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Pinfo is a curses based lynx-style info browser.

%description -l pl
Pinfo jest przegl±dark± dokumentów info podobn± do lynx'a.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--without-included-gettext \
	--target=%{_target_platform} \
	--host=%{_host}
	
make 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man*/* \
	ChangeLog NEWS AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/pinfo
%config %verify(not md5 size mtime) /etc/pinforc

%lang(pl) /usr/share/locale/pl/LC_MESSAGES/*
%lang(cs) /usr/share/locale/cs/LC_MESSAGES/*
%lang(de) /usr/share/locale/de/LC_MESSAGES/*
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/*
/usr/share/man/man1/*

%changelog
* Mon May  3 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.5.2-1]
- added de and sv locale

* Fri Apr 16 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.4.9-1]
- added --with-readline to ./configure
- added pinforc and polish locale to %%files

* Sat Apr 10 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.4.8-1]
- added --sysconfdir=/etc to ./configure

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
