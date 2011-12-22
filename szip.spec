%bcond_with	encoder		# build with encoder (may require license)
#
Summary:	SZIP - Science Data Lossless Compression library
Name:		szip
Version:	2.1
Release:	1
%if %{with encoder}
License:	free for non-commercial, scientific use only in HDF software
%else
License:	free for use in HDF software
%endif
Group:		System/Libraries
Source0:	ftp://ftp.hdfgroup.org/lib-external/szip/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-linking.patch
URL:		http://hdf.ncsa.uiuc.edu/doc_resource/SZIP/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
SZIP is an implementation of the extended-Rice lossless compression
algorithm. The Consultative Committee on Space Data Systems (CCSDS)
has adopted the extended-Rice algorithm for international standards
for space applications. SZIP is reported to provide fast and effective
compression, specifically for the EOS data generated by the NASA Earth
Observatory System (EOS). It was originally developed at University of
New Mexico (UNM) and integrated with HDF4 by UNM researchers and
developers.

%package devel
Summary:	Header files for SZIP library
Group:		Development/C	
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SZIP library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_encoder:--disable-encoding}
%{__make}

%install
%makeinstall_std
rm -rf %{buildroot}/%{_libdir}/libsz.a


%files
%doc COPYING RELEASE.txt
%attr(755,root,root) %{_libdir}/libsz.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libsz.so.2

%files devel
%attr(755,root,root) %{_libdir}/libsz.so
%{_includedir}/*.h
