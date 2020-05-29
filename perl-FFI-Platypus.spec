#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	FFI
%define		pnam	Platypus
Summary:	FFI::Platypus - Write Perl bindings to non-Perl libraries with FFI. No XS required.
Name:		perl-FFI-Platypus
Version:	1.28
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FFI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe23d49d5822adf1355a6b32157728a7
URL:		http://search.cpan.org/dist/FFI-Platypus/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-FFI-CheckLib
BuildRequires:	perl-IPC-Cmd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platypus is a library for creating interfaces to machine code
libraries written in languages like C, C++, Go, Fortran, Rust, Pascal.
Essentially anything that gets compiled into machine code. This
implementation uses libffi to accomplish this task. libffi is battle
tested by a number of other scripting and virtual machine languages,
such as Python and Ruby to serve a similar role. There are a number of
reasons why you might want to write an extension with Platypus instead
of XS:

* FFI::Platypus does not require messing with the guts of Perl
* FFI::Platypus is portable
* FFI::Platypus could be a bridge to Perl 6
* FFI::Platypus can be reimplemented
* FFI::Platypus is pure perl (sorta)
* FFI::Platypus is not C or C++ centric
* FFI::Platypus does not require a parser

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorarch}/FFI/Build.pm
%dir %{perl_vendorarch}/FFI/Build
%dir %{perl_vendorarch}/FFI/Build/File
%{perl_vendorarch}/FFI/Build/File/Base.pm
%{perl_vendorarch}/FFI/Build/File/C.pm
%{perl_vendorarch}/FFI/Build/File/CXX.pm
%{perl_vendorarch}/FFI/Build/File/Library.pm
%{perl_vendorarch}/FFI/Build/File/Object.pm
%{perl_vendorarch}/FFI/Build/MM.pm
%{perl_vendorarch}/FFI/Build/Platform.pm
%{perl_vendorarch}/FFI/Platypus.pm
%dir %{perl_vendorarch}/FFI/Platypus
%{perl_vendorarch}/FFI/Platypus/API.pm
%{perl_vendorarch}/FFI/Platypus/Buffer.pm
%{perl_vendorarch}/FFI/Platypus/Bundle.pm
%{perl_vendorarch}/FFI/Platypus/Closure.pm
%{perl_vendorarch}/FFI/Platypus/Constant.pm
%{perl_vendorarch}/FFI/Platypus/DL.pm
%{perl_vendorarch}/FFI/Platypus/Declare.pm
%{perl_vendorarch}/FFI/Platypus/Function.pm
%{perl_vendorarch}/FFI/Platypus/Internal.pm
%{perl_vendorarch}/FFI/Platypus/Lang.pm
%dir %{perl_vendorarch}/FFI/Platypus/Lang
%{perl_vendorarch}/FFI/Platypus/Lang/ASM.pm
%{perl_vendorarch}/FFI/Platypus/Lang/C.pm
%{perl_vendorarch}/FFI/Platypus/Lang/Win32.pm
%{perl_vendorarch}/FFI/Platypus/Legacy.pm
%{perl_vendorarch}/FFI/Platypus/Memory.pm
%{perl_vendorarch}/FFI/Platypus/Record.pm
%dir %{perl_vendorarch}/FFI/Platypus/Record
%{perl_vendorarch}/FFI/Platypus/Record/Meta.pm
%{perl_vendorarch}/FFI/Platypus/Record/TieArray.pm
%{perl_vendorarch}/FFI/Platypus/ShareConfig.pm
%{perl_vendorarch}/FFI/Platypus/Type.pm
%dir %{perl_vendorarch}/FFI/Platypus/Type
%{perl_vendorarch}/FFI/Platypus/Type/PointerSizeBuffer.pm
%{perl_vendorarch}/FFI/Platypus/Type/StringArray.pm
%{perl_vendorarch}/FFI/Platypus/Type/StringPointer.pm
%{perl_vendorarch}/FFI/Platypus/TypeParser.pm
%dir %{perl_vendorarch}/FFI/Platypus/TypeParser
%{perl_vendorarch}/FFI/Platypus/TypeParser/Version0.pm
%{perl_vendorarch}/FFI/Platypus/TypeParser/Version1.pm
%{perl_vendorarch}/FFI/Probe.pm
%dir %{perl_vendorarch}/FFI/Probe
%{perl_vendorarch}/FFI/Probe/Runner.pm
%dir %{perl_vendorarch}/FFI/Probe/Runner
%{perl_vendorarch}/FFI/Probe/Runner/Builder.pm
%{perl_vendorarch}/FFI/Probe/Runner/Result.pm
%{perl_vendorarch}/FFI/Temp.pm
%{perl_vendorarch}/FFI/typemap
%dir %{perl_vendorarch}/auto/FFI/Platypus
%attr(755,root,root) %{perl_vendorarch}/auto/FFI/Platypus/Platypus.so
%{perl_vendorarch}/auto/FFI/Platypus/Constant
%{perl_vendorarch}/auto/FFI/Platypus/Memory
%{perl_vendorarch}/auto/FFI/Platypus/Record
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/config.pl
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus/include
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/include/ffi_platypus_bundle.h
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/include/ffi_platypus_config.h
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus/lib
%attr(755,root,root) %{perl_vendorarch}/auto/share/dist/FFI-Platypus/lib/libplfill.so
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe/bin
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe/bin/dlrun
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe/probe.pl
%dir %{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe/src
%{perl_vendorarch}/auto/share/dist/FFI-Platypus/probe/src/dlrun.c
%{_mandir}/man3/FFI::Build*.3pm*
%{_mandir}/man3/FFI::Platypus*.3pm*
%{_mandir}/man3/FFI::Probe*.3pm*
%{_mandir}/man3/FFI::Temp*.3pm*
