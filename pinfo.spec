Summary:	Lynx-style info browser
Summary(es.UTF-8):	Visualizador de páginas info y man
Summary(pl.UTF-8):	Przeglądarka info w stylu lynksa
Summary(pt_BR.UTF-8):	Visualizador de páginas info e man
Summary(ru.UTF-8):	Программа просмотра info- и man-документов в стиле lynx
Summary(uk.UTF-8):	Програма перегляду info- та man-документів у стилі lynx
Name:		pinfo
Version:	0.6.13
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/baszoetekouw/pinfo/releases
Source0:	https://github.com/baszoetekouw/pinfo/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b2671c8f6ef0aa5d7c6460c3111e2f50
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-info.patch
Patch4:		%{name}-gettext.patch
Patch5:		%{name}-color.patch
Patch6:		%{name}-no-common.patch
URL:		https://github.com/baszoetekouw/pinfo
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.0
BuildRequires:	texinfo
Requires:	setup >= 2.4.6-2
Suggests:	man
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
%patch5 -p1
%patch6 -p1

%build
CPPFLAGS="-I%{_includedir}/ncursesw"
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/shrc.d/%{name}.sh
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/shrc.d/%{name}.csh

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/pinfo
%config(noreplace) %verify(not md5 mtime size) /etc/shrc.d/pinfo.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pinforc
%{_mandir}/man1/pinfo.1*
%{_infodir}/pinfo.info*
