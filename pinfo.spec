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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/pinfo
%config %verify(not md5 size mtime) /etc/pinforc

/usr/share/man/man1/*
