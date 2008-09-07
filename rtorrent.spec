%define libtorrentver 0.12.2
%define release %mkrel 3

Name: rtorrent
Version: 0.8.2
Release: %release
Epoch: 1
Summary: Curses based BitTorrent client
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPLv2+
Group: Networking/File transfer
URL: http://libtorrent.rakshasa.no/
Source0: http://libtorrent.rakshasa.no/downloads/%name-%{version}.tar.gz
#gw patches from Gentoo
Patch: libtorrent-0.12.2-fix_start_stop_filter.patch
Patch1: rtorrent-0.8.2-gcc4.3.patch
Patch2: rtorrent-0.8.2-fix_conn_type_seed.patch
Patch3: rtorrent-0.8.2-fix_load_cache.patch
Patch4: rtorrent-0.8.2-fix_utf8_filenames.patch
Requires: libtorrent >= %libtorrentver
BuildRequires: libtorrent-devel >= %libtorrentver
BuildRequires: libcurl-devel >= 7.12.0
BuildRequires: libncursesw-devel
BuildRequires: docbook-utils
BuildRequires: docbook-dtd41-sgml
BuildRequires: automake libtool
BuildRequires: xmlrpc-c-devel

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%setup -q
%patch -p1
%patch1 -p1 -b .gcc4.3
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)
#gw add flags for the ncursesw headers
export CPPFLAGS=-I%_includedir/ncursesw
# don't use --as-needed - it make build fail on x86_64
%define ldflags -Wl,--no-undefined
%configure2_5x --with-xmlrpc-c
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
