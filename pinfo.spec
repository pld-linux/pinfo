Summary:	Lynx-style info browser
Summary(es):	Visualizador de p�ginas info y man
Summary(pl):	Przegl�darka info w stylu lynksa
Summary(pt_BR):	Visualizador de p�ginas info e man
Summary(ru):	��������� ��������� info- � man-���������� � ����� lynx
Summary(uk):	�������� ��������� info- �� man-�������Ԧ� � ���̦ lynx
Name:		pinfo
Version:	0.6.9
Release:	1
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

%description -l es
Visualizador de p�ginas info y man.

%description -l pl
Pinfo jest przegl�dark� dokument�w info podobn� do lynksa.

%description -l pt_BR
Visualizador hipertexto de arquivos info e p�ginas de manual, com
interface semelhante ao lynx. Suporta pesquisa de express�es
regulares.

%description -l ru
Pinfo - ��� ��������� ��������� info-������ � man-�������. ��
��������� ������������ ����� �� ��������� Lynx. �������������� �����
�� ���������� ����������.

%description -l uk
Pinfo - �� �������� ��������� info-���̦� �� man-���Ҧ���. ��
��������� ��Ħ���� �� ���������� Lynx. ������դ���� ����� ��
���������� �������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
