%define libtorrentver 0.11.7
%define release %mkrel 1
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}
Name: rtorrent
Version: 0.7.7
Release: %release
Epoch: 1
Summary: Curses based BitTorrent client
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL
Group: Networking/File transfer
URL: http://libtorrent.rakshasa.no/
Source0: http://libtorrent.rakshasa.no/downloads/%name-%{version}.tar.bz2 
Patch: rtorrent-0.7.7-new-sigc++.patch
Requires: libtorrent >= %libtorrentver
BuildRequires: libtorrent-devel >= %libtorrentver
BuildRequires: libcurl-devel >= 7.12.0
BuildRequires: libncursesw-devel
BuildRequires: docbook-utils
BuildRequires: docbook-dtd41-sgml
BuildRequires: automake1.8 libtool

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%setup -q
%patch -p1 -b .new-sigc++

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)
#gw add flags for the ncursesw headers
export CPPFLAGS=-I%_includedir/ncursesw
%configure2_5x
%make
cd doc
db2html faq.xml

%install 
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
%makeinstall_std
  
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc README AUTHORS TODO doc/faq doc/rtorrent.rc
%{_bindir}/rtorrent
%_mandir/man1/rtorrent.1*


