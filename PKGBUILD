# Maintainer: ulolol
# Based on the original AUR package by Charles Milette <charles.milette@gmail.com>
# Modified to include pokemon random feature

_gitname=Pokemon-Terminal
pkgname=pokemon-terminal-git
pkgver=1.3.0
pkgrel=1
pkgdesc="Pokemon terminal themes with random selection support"
arch=('any')
url="https://github.com/ulolol/$_gitname"
license=('GPL3')
depends=('python>=3.6' 'python-psutil')
optdepends=('gnome-shell: support changing GNOME wallpaper'
            'feh: support changing Openbox and i3 wallpaper'
            'terminology: support changing Terminology background'
            'tilix: support changing Tilix background'
            'python-pyyaml: support changing Contour Terminal background')
makedepends=('python-setuptools' 'python')
source=("git+https://github.com/ulolol/$_gitname.git")
md5sums=('SKIP')

package() {
  cd "$srcdir/$_gitname"
  python setup.py install --root="$pkgdir/" --optimize=1
}
