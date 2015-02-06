Summary:	Auto code generation for converting OCaml values to/from type-safe bin protocol
Name:		ocaml-bin-prot
Version:	1.2.23
Release:	7
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://ocaml.info/home/ocaml_sources.html#bin-prot
Source0:	http://hg.ocaml.info/release/bin-prot/archive/bin-prot-release-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
Patch0:		ocaml-bin-prot-1.2.23-unused-var.patch
# curl http://hg.ocaml.info/release/bin-prot/archive/release-${version}.tar.bz2 > bin-prot-release-%{version}.tar.bz2
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ounit
BuildRequires:	ocaml-type-conv
BuildRequires:	pkgconfig(ncurses)

%description
This library contains functionality for reading and writing OCaml-values in
a type-safe binary protocol. These functions are extremely efficient and
provide users with a convenient and safe way of performing I/O on any
extensionally defined data type. This means that functions, objects, and
values whose type is bound through a polymorphic record field are not
supported, but everything else is.

As of now, there is no support for cyclic or shared values. Cyclic values
will lead to non-termination whereas shared values, besides requiring
significantly more space when encoded, may lead to a substantial increase in
memory footprint when they are read back in.

Currently only little endian (2) computer architectures are supported. Some
architectures may potentially also suffer from data alignment issues with this
library. Only Intel architectures are currently well-tested. Both 32bit and
64bit architectures are fully supported.

%files
%doc LICENSE LICENSE.Tywith
%dir %{_libdir}/ocaml/bin_prot
%{_libdir}/ocaml/bin_prot/META
%{_libdir}/ocaml/bin_prot/*.cma
%{_libdir}/ocaml/bin_prot/*.cmi
%{_libdir}/ocaml/bin_prot/*.cmo
%{_libdir}/ocaml/stublibs/*.so*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc LICENSE LICENSE.Tywith Changelog COPYRIGHT README.txt
%doc lib_test
%{_libdir}/ocaml/bin_prot/*.a
%{_libdir}/ocaml/bin_prot/*.cmxa
%{_libdir}/ocaml/bin_prot/*.mli
%{_libdir}/ocaml/bin_prot/*.ml

#----------------------------------------------------------------------------

%prep
%setup -q -n bin-prot-release-%{version}
%patch0 -p0

%build
make

# TODO: generate the doc in end-user file formats

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install



