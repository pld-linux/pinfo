Summary:	Lynx-style info browser
Summary(es):	Visualizador de páginas info y man
Summary(pl):	Przêgl±darka info w stylu lynksa
Summary(pt_BR):	Visualizador de páginas info e man
Name:		pinfo
Version:	0.6.6p1
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source0:	http://zeus.polsl.gliwice.pl/~pborys/stable-version/%{name}-%{version}.tar.gz
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-info.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
Requires:	man-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Pinfo is a curses based lynx-style info browser.

%description -l es
Visualizador de páginas info y man.

%description -l pl
Pinfo jest przegl±dark± dokumentów info podobn± do lynksa.

%description -l pt_BR
Visualizador hipertexto de arquivos info e páginas de manual, com
interface semelhante ao lynx. Suporta pesquisa de expressões
regulares.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.sh
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.csh

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS AUTHORS README
%attr(755,root,root) %{_bindir}/pinfo
%attr(755,root,root) %{_sysconfdir}/profile.d/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pinforc
%{_mandir}/man1/*
%{_infodir}/*
