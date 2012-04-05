%define	libtorrentver	0.13.0
%define	release	%mkrel	1

Name:		rtorrent
Version:	0.9.1
Release:	%release
Epoch:		1
Summary:	Curses based BitTorrent client
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://libtorrent.rakshasa.no/
Source0:	http://libtorrent.rakshasa.no/downloads/%name-%{version}.tar.gz
Requires:	libtorrent >= %libtorrentver
BuildRequires:	libtorrent-devel >= %libtorrentver
BuildRequires:	libcurl-devel >= 7.12.0
BuildRequires:	ncursesw-devel
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	xmlrpc-c-devel
BuildRequires:  cppunit-devel

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%setup -q

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)

#gw add flags for the ncursesw headers
export CPPFLAGS=-I%_includedir/ncursesw

#add hack to fix build on BS, for some reason build fails with iurt on x86_64 without this,
#local build on BS works without this hack, though (wally 03/2010)
export LIBS="-lxmlrpc -lxmlrpc_util -lpthread"


%configure2_5x --with-xmlrpc-c
%make
cd doc
db2html faq.xml

%install 
rm -rf $RPM_BUILD_ROOT;
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc README AUTHORS doc/faq doc/rtorrent.rc
%{_bindir}/rtorrent
#gw it was outdated:
#%_mandir/man1/rtorrent.1*
