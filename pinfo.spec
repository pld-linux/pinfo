Summary:	Lynx-style info browser
Summary(pl):	Prz�gl�darka info w stylu lynx'a
Name:		pinfo	
Version:	0.6.3
Release:	1
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
License:	GPL
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source0:	http://zeus.polsl.gliwice.pl/~pborys/stable-version/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Pinfo is a curses based lynx-style info browser.

%description -l pl
Pinfo jest przegl�dark� dokument�w info podobn� do lynx'a.

%prep
%setup -q

%build
aclocal -I macros
autoconf
automake -a -c
%configure \
	--without-included-gettext
	
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog NEWS AUTHORS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pinfo
%config %verify(not md5 size mtime) %{_sysconfdir}/pinforc

%{_mandir}/man1/*
