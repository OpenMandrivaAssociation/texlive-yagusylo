# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/yagusylo
# catalog-date 2012-07-21 17:20:52 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-yagusylo
Version:	1.2
Release:	3
Summary:	A symbol loader
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yagusylo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yagusylo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The name is by way of being an acronym for "Yet Another Grand
Unified Symbols Loader"... The package allows the user to
access a symbol without loading the package that usually
provides it; this has the advantage of avoiding the name
clashes that so commonly trouble those who load symbol-
packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
