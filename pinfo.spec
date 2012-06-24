Summary:	Lynx-style info browser
Summary(es):	Visualizador de p�ginas info y man
Summary(pl):	Prz�gl�darka info w stylu lynksa
Summary(pt_BR):	Visualizador de p�ginas info e man
Summary(ru):	��������� ��������� info- � man-���������� � ����� lynx
Summary(uk):	�������� ��������� info- �� man-�������Ԧ� � ���̦ lynx
Name:		pinfo
Version:	0.6.8
Release:	3
License:	GPL
Group:		Applications/System
Vendor:		Przemek Borys <pborys@dione.ids.pl>
Source0:	http://dione.ids.pl/~pborys/software/pinfo/%{name}-%{version}.tar.gz
# Source0-md5:	55feb4ebaa709b52bd00a15ed0fb52fb
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-po.patch
Patch3:		%{name}-mkstemp.patch
Patch4:		%{name}-home_etc.patch
URL:		http://dione.ids.pl/~pborys/software/pinfo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
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
%patch4 -p1

%build
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
%attr(755,root,root) /etc/shrc.d/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pinforc
%{_mandir}/man1/*
%{_infodir}/pinfo*
