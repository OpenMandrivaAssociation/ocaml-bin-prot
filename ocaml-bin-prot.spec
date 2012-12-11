Name:           ocaml-bin-prot
Version:        1.2.23
Release:        5
Summary:        Auto code generation for converting OCaml values to/from type-safe bin protocol
License:        LGPL
Group:          Development/Other
URL:            http://ocaml.info/home/ocaml_sources.html#bin-prot
Source0:        http://hg.ocaml.info/release/bin-prot/archive/bin-prot-release-%{version}.tar.bz2
Patch0:         ocaml-bin-prot-1.2.23-unused-var.patch
# curl http://hg.ocaml.info/release/bin-prot/archive/release-${version}.tar.bz2 > bin-prot-release-%{version}.tar.bz2
BuildRequires:  ocaml
BuildRequires:  camlp4
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-type-conv
BuildRequires:  ncurses-devel

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

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n bin-prot-release-%{version}
%patch0 -p0

%build
make

# TODO: generate the doc in end-user file formats

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE LICENSE.Tywith
%dir %{_libdir}/ocaml/bin_prot
%{_libdir}/ocaml/bin_prot/META
%{_libdir}/ocaml/bin_prot/*.cma
%{_libdir}/ocaml/bin_prot/*.cmi
%{_libdir}/ocaml/bin_prot/*.cmo
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc LICENSE LICENSE.Tywith Changelog COPYRIGHT README.txt
%doc lib_test
%{_libdir}/ocaml/bin_prot/*.a
%{_libdir}/ocaml/bin_prot/*.cmxa
%{_libdir}/ocaml/bin_prot/*.mli
%{_libdir}/ocaml/bin_prot/*.ml



%changelog
* Wed Apr 07 2010 Florent Monnier <blue_prawn@mandriva.org> 1.2.23-1mdv2010.1
+ Revision: 532841
- updated to version 1.2.23

* Fri Mar 26 2010 Florent Monnier <blue_prawn@mandriva.org> 1.2.21-1mdv2010.1
+ Revision: 527573
- updated to version 1.2.21

* Fri Sep 25 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.20-1mdv2010.0
+ Revision: 449230
- new version 1.2.20

* Tue Jul 28 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.18-1mdv2010.0
+ Revision: 401361
- updated version

* Sun Jan 18 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.9-1mdv2009.1
+ Revision: 330985
- added some BuildRequires
- import ocaml-bin-prot


