Summary:	An implementation of the Lisp language with statistics extensions
Summary(de):	xlisp von David Betz mit Statistik-Erweiterungen
Summary(es):	Xlisp de David Betz con extensiones estad�sticas
Summary(fr):	xlisp de David Betz avec des extensions statistiques
Summary(pl):	Implementacja j�zyka Lisp z rozszerzeniami statystycznymi
Summary(pt_BR):	Xlisp de David Betz com extens�es estat�sticas
Summary(tr):	David Betz'in istatistik yetenekleri olana xlisp yorumlay�c�s�
Name:		xlispstat
Version:	3.52.18
%define		tar_version	%(echo %{version} | sed 's,\\.,-,g')
Release:	5
License:	distributable
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In�ynierskie
Source0:	ftp://ftp.stat.umn.edu/pub/xlispstat/3-52/%{name}-%{tar_version}.tar.gz
URL:		http://lib.stat.cmu.edu/xlispstat
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlispstat package contains XLISP-PLUS, an implementation of the
Lisp programming language for the X Window System. XLISP-PLUS also
includes extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%description -l de
Eine Implementierung der Lisp-Programmiersprache f�r X-Windows mit
Erweiterungen f�r fortgeschrittene statistische Berechnungen.

%description -l es
Una implementaci�n al lenguaje de programaci�n Lisp para X Window, con
extensiones para c�lculos estad�sticos avanzados.

%description -l fr
Implantation du langage Lisp pour X Window, avec des extensions pour
les calculs statistiques avanc�s.

%description -l pl
Pakiet xlispstat zawiera XLISP-PLUS - implementacj� j�zyka
programowania Lisp dla X Window System. XLISP-PLUS zawiera tak�e
rozszerzenia do prowadzenia zaawansowanych oblicze� statystycznych.

%description -l pt_BR
Uma implementa��o da linguagem de programa��o Lisp para X Window, com
extens�es para c�lculos estat�sticos avan�ados.

%description -l tr
Lisp programlama dilinin X-Windows alt�nda �al��an ve ileri istatistik
hesaplama deste�i bulunan bir ger�eklemesi.

%prep
%setup -q -n xlispstat-3-52-18

%build
aclocal
autoconf
%configure
%{__make} UCFLAGS="%{rpmcflags} -mieee-fp"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf README RELEASE doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz RELEASE.gz doc/*
%dir %{_libdir}/xlispstat
%attr(755,root,root) %{_bindir}/xlispstat
%attr(755,root,root) %{_libdir}/xlispstat/xlisp
%{_libdir}/xlispstat/Autoload
%{_libdir}/xlispstat/Data
%{_libdir}/xlispstat/Examples
%{_libdir}/xlispstat/xlisp.hlp
%{_libdir}/xlispstat/xlisp.wks
