from .build import build_arch, get_triplet, extract_archive
import pathlib


triplet = get_triplet(build_arch())

archive = pathlib.Path(__file__).parent / "_toolchain" / f"{triplet}.tar.xz"
toolchain = pathlib.Path(__file__).parent / "_toolchain" / triplet



def environ():
    if toolchain.exists():
        print("Toolchain directory exists")
    else:
        print("extract archive")
        extract_archive(toolchain, str(archive))
    return {
        "TOOLCHAIN_PATH": f"{toolchain}",
        "CC": f"{toolchain / 'bin' / '{triplet}-gcc'}",
        "CXX": f"{toolchain / 'bin' / '{triplet}-g++'}",
        "CFLAGS": f"-I{toolchain}/{triplet}/sysroot/usr/include",
        "CPPFLAGS": f"-I{toolchain}/{triplet}/sysroot/usr/include",
        "CMAKE_FLAGS": f"-I{toolchain}/{triplet}/sysroot/usr/include",
        "LDFLAGS": f"-L{toolchain}/{triplet}/sysroot/lib"
    }
