#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-base64url
Version  : 1.4
Release  : 9
URL      : https://cran.r-project.org/src/contrib/base64url_1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/base64url_1.4.tar.gz
Summary  : Fast and URL-Safe Base64 Encoder and Decoder
Group    : Development/Tools
License  : GPL-3.0
Requires: R-base64url-lib = %{version}-%{release}
Requires: R-backports
BuildRequires : R-backports
BuildRequires : R-base64enc
BuildRequires : R-checkmate
BuildRequires : R-openssl
BuildRequires : buildreq-R

%description
"-", the 63rd character ("/") is replaced with "_". Furthermore, the encoder
    does not fill the string with trailing "=". The resulting encoded strings
    comply to the regular expression pattern "[A-Za-z0-9_-]" and thus are
    safe to use in URLs or for file names.
    The package also comes with a simple base32 encoder/decoder suited for
    case insensitive file systems.

%package lib
Summary: lib components for the R-base64url package.
Group: Libraries

%description lib
lib components for the R-base64url package.


%prep
%setup -q -c -n base64url
cd %{_builddir}/base64url

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640972670

%install
export SOURCE_DATE_EPOCH=1640972670
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64url
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64url
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library base64url
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc base64url || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/base64url/DESCRIPTION
/usr/lib64/R/library/base64url/INDEX
/usr/lib64/R/library/base64url/Meta/Rd.rds
/usr/lib64/R/library/base64url/Meta/features.rds
/usr/lib64/R/library/base64url/Meta/hsearch.rds
/usr/lib64/R/library/base64url/Meta/links.rds
/usr/lib64/R/library/base64url/Meta/nsInfo.rds
/usr/lib64/R/library/base64url/Meta/package.rds
/usr/lib64/R/library/base64url/Meta/vignette.rds
/usr/lib64/R/library/base64url/NAMESPACE
/usr/lib64/R/library/base64url/NEWS.md
/usr/lib64/R/library/base64url/R/base64url
/usr/lib64/R/library/base64url/R/base64url.rdb
/usr/lib64/R/library/base64url/R/base64url.rdx
/usr/lib64/R/library/base64url/doc/Benchmarks.R
/usr/lib64/R/library/base64url/doc/Benchmarks.Rmd
/usr/lib64/R/library/base64url/doc/Benchmarks.html
/usr/lib64/R/library/base64url/doc/index.html
/usr/lib64/R/library/base64url/help/AnIndex
/usr/lib64/R/library/base64url/help/aliases.rds
/usr/lib64/R/library/base64url/help/base64url.rdb
/usr/lib64/R/library/base64url/help/base64url.rdx
/usr/lib64/R/library/base64url/help/paths.rds
/usr/lib64/R/library/base64url/html/00Index.html
/usr/lib64/R/library/base64url/html/R.css
/usr/lib64/R/library/base64url/tests/testthat.R
/usr/lib64/R/library/base64url/tests/testthat/helper.R
/usr/lib64/R/library/base64url/tests/testthat/test_base32.R
/usr/lib64/R/library/base64url/tests/testthat/test_base64.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/base64url/libs/base64url.so
/usr/lib64/R/library/base64url/libs/base64url.so.avx2
/usr/lib64/R/library/base64url/libs/base64url.so.avx512
