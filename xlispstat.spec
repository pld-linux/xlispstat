Summary:	An implementation of the Lisp language with statistics extensions
Summary(de.UTF-8):	xlisp von David Betz mit Statistik-Erweiterungen
Summary(es.UTF-8):	Xlisp de David Betz con extensiones estadísticas
Summary(fr.UTF-8):	xlisp de David Betz avec des extensions statistiques
Summary(pl.UTF-8):	Implementacja języka Lisp z rozszerzeniami statystycznymi
Summary(pt_BR.UTF-8):	Xlisp de David Betz com extensões estatísticas
Summary(tr.UTF-8):	David Betz'in istatistik yetenekleri olana xlisp yorumlayıcısı
Name:		xlispstat
Version:	3.52.19
%define		tar_version	%(echo %{version} | tr . -)
Release:	1
License:	distributable
Group:		Applications/Engineering
Source0:	ftp://ftp.stat.umn.edu/pub/xlispstat/3-52/%{name}-%{tar_version}.tar.gz
# Source0-md5:	2cda23d9553b0f546e4e62558115ce95
URL:		http://lib.stat.cmu.edu/xlispstat/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlispstat package contains XLISP-PLUS, an implementation of the
Lisp programming language for the X Window System. XLISP-PLUS also
includes extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%description -l de.UTF-8
Eine Implementierung der Lisp-Programmiersprache für X-Window mit
Erweiterungen für fortgeschrittene statistische Berechnungen.

%description -l es.UTF-8
Una implementación al lenguaje de programación Lisp para X Window, con
extensiones para cálculos estadísticos avanzados.

%description -l fr.UTF-8
Implantation du langage Lisp pour X Window, avec des extensions pour
les calculs statistiques avancés.

%description -l pl.UTF-8
Pakiet xlispstat zawiera XLISP-PLUS - implementację języka
programowania Lisp dla X Window System. XLISP-PLUS zawiera także
rozszerzenia do prowadzenia zaawansowanych obliczeń statystycznych.

%description -l pt_BR.UTF-8
Uma implementação da linguagem de programação Lisp para X Window, com
extensões para cálculos estatísticos avançados.

%description -l tr.UTF-8
Lisp programlama dilinin X-Window altında çalışan ve ileri istatistik
hesaplama desteği bulunan bir gerçeklemesi.

%prep
%setup -q -n xlispstat-3-52-18

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} UCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELEASE doc/*
%attr(755,root,root) %{_bindir}/xlispstat
%dir %{_libdir}/xlispstat
%attr(755,root,root) %{_libdir}/xlispstat/xlisp
%{_libdir}/xlispstat/Autoload
%{_libdir}/xlispstat/Data
%{_libdir}/xlispstat/Examples
%{_libdir}/xlispstat/xlisp.hlp
%{_libdir}/xlispstat/xlisp.wks
