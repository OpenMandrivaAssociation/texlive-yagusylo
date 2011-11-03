# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/yagusylo
# catalog-date 2009-03-03 08:06:14 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-yagusylo
Version:	1.2
Release:	1
Summary:	A symbol loader
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yagusylo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The name is by way of being an acronym for "Yet Another Grand
Unified Symbols Loader"... The package allows the user to
access a symbol without loading the package that usually
provides it; this has the advantage of avoiding the name
clashes that so commonly trouble those who load symbol-
packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/yagusylo/yagusylo.cfg
%{_texmfdistdir}/tex/latex/yagusylo/yagusylo.sty
%doc %{_texmfdistdir}/doc/latex/yagusylo/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/yagusylo/README
%doc %{_texmfdistdir}/doc/latex/yagusylo/yagusylo-en.pdf
%doc %{_texmfdistdir}/doc/latex/yagusylo/yagusylo-fr.pdf
%doc %{_texmfdistdir}/doc/latex/yagusylo/yagusylo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/yagusylo/Makefile
%doc %{_texmfdistdir}/source/latex/yagusylo/yagusylo.dtx
%doc %{_texmfdistdir}/source/latex/yagusylo/yagusylo.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
