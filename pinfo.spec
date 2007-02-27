Summary:	Lynx-style info browser
Summary(es.UTF-8):	Visualizador de páginas info y man
Summary(pl.UTF-8):	Przeglądarka info w stylu lynksa
Summary(pt_BR.UTF-8):	Visualizador de páginas info e man
Summary(ru.UTF-8):	Программа просмотра info- и man-документов в стиле lynx
Summary(uk.UTF-8):	Програма перегляду info- та man-документів у стилі lynx
Name:		pinfo
Version:	0.6.9
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	https://alioth.debian.org/download.php/1498/%{name}-%{version}.tar.bz2
# Source0-md5:	e0c788467945f5f97fbacad55863e5b8
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-ncurses.patch
URL:		http://pinfo.alioth.debian.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.0
BuildRequires:	texinfo
Requires:	man-config
Requires:	setup >= 2.4.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pinfo is a curses based lynx-style info browser.

%description -l es.UTF-8
Visualizador de páginas info y man.

%description -l pl.UTF-8
Pinfo jest przeglądarką dokumentów info podobną do lynksa.

%description -l pt_BR.UTF-8
Visualizador hipertexto de arquivos info e páginas de manual, com
interface semelhante ao lynx. Suporta pesquisa de expressões
regulares.

%description -l ru.UTF-8
Pinfo - это программа просмотра info-файлов и man-страниц. Ее
интерфейс пользователя похож на интерфейс Lynx. Поддерживается поиск
по регулярным выражениям.

%description -l uk.UTF-8
Pinfo - це програма перегляду info-файлів та man-сторінок. Її
інтерфейс подібний до інтерфейсу Lynx. Підтримується пошук по
регулярним виразам.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f doc/pinfo.info po/stamp-po

%build
CPPFLAGS="-I%{_includedir}/ncurses"
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/shrc.d/%{name}.sh
install %{SOURCE2} $RPM_BUILD_ROOT/etc/shrc.d/%{name}.csh

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
/etc/shrc.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pinforc
%{_mandir}/man1/*
%{_infodir}/pinfo*
