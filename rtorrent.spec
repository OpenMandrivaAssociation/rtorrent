%define	libtorrentver	0.16.10

Name:		rtorrent
Version:	0.16.10
Release:	1
Summary:	Curses based BitTorrent client
License:	GPLv2+
Group:		Networking/File transfer
URL:		https://rakshasa.github.io/rtorrent/
#Source0:	http://rtorrent.net/downloads/%name-%{version}.tar.gz
Source0:  https://github.com/rakshasa/rtorrent/releases/download/v%{version}/rtorrent-%{version}.tar.gz
#Patch0:		rtorrent-0.9.8_color.patch

BuildRequires: automake
BuildRequires: slibtool
BuildRequires: make
BuildRequires: pkgconfig(libtorrent) >= %{libtorrentver}
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(ncursesw)
# Replaced by faster tintyxml2
#BuildRequires: pkgconfig(xmlrpc)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(cppunit)
BuildRequires: autoconf autoconf-archive

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%autosetup -p1

%build
%configure AR=llvm-ar \
           RANLIB=llvm-ranlib \
          --enable-ipv6 \
          --with-xmlrpc-tinyxml2
%make_build

%install 
%make_install

%files
%doc README* AUTHORS doc/rtorrent.rc
%{_bindir}/rtorrent
%{_datadir}/rtorrent/lua/rtorrent.lua
