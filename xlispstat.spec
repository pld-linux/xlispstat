Summary: An implementation of the Lisp language with statistics extensions.
Name: xlispstat
Version: 3.52.9
Release: 2
Copyright: Distributable
Group: Applications/Engineering
Source: ftp://umnstat.stat.umn.edu:/pub/xlispstat/3-52/xlispstat-3-52-9.tar.gz
URL: http://lib.stat.cmu.edu/xlispstat
BuildRoot: /var/tmp/xlispstat-root

%description
The xlispstat package contains XLISP-PLUS, an implementation of the Lisp
programming language for the X Window System.  XLISP-PLUS also includes
extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%prep
%setup -q -n xlispstat-3-52-9

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/lib/xlispstat/xlisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README RELEASE doc
/usr/bin/xlispstat
/usr/lib/xlispstat
