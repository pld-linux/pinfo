Summary:	Lynx-style info browser
Summary(es):	Visualizador de p·ginas info y man
Summary(pl):	PrzÍgl±darka info w stylu lynksa
Summary(pt_BR):	Visualizador de p·ginas info e man
Name:		pinfo	
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications/System
Group(cs):	Aplikace/SystÈm
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/SystËme
Group(it):	Applicazioni/Sistema
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∑•π•∆•‡
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	AplicaÁıes/Sistema
Group(pt_BR):	AplicaÁıes/Sistema
Group(ru):	“…Ãœ÷≈Œ…—/Û…”‘≈Õ¡
Group(sv):	Till‰mpningar/System
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source0:	http://zeus.polsl.gliwice.pl/~pborys/stable-version/%{name}-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Pinfo is a curses based lynx-style info browser.

%description -l es
Visualizador de p·ginas info y man.

%description -l pl
Pinfo jest przegl±dark± dokumentÛw info podobn± do lynksa.

%description -l pt_BR
Visualizador hipertexto de arquivos info e p·ginas de manual, com
interface semelhante ao lynx. Suporta pesquisa de expressıes
regulares.

%prep
%setup -q
%patch -p1

%build
aclocal -I macros
autoconf
automake -a -c -f
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
