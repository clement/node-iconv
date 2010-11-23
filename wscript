import Options
from os import unlink, symlink, popen
from os.path import exists 

srcdir = "."
blddir = "build"
VERSION = "0.3.0"

def set_options(opt):
    opt.tool_options("compiler_cxx")

def configure(conf):
    conf.check_tool("compiler_cxx")
    conf.check_tool("node_addon")

    conf.check_cxx(lib='iconv',
                   uselib_store='ICONV',
                   mandatory=True)
    conf.env.USELIB = [ 'ICONV' ]

def build(bld):
    obj = bld.new_task_gen("cxx", "shlib", "node_addon")
    obj.cxxflags = ["-Wall"]
    obj.target = "iconv"
    obj.source = "src/iconv.cc"
    obj.defines = bld.env.DEFINES
    obj.uselib = bld.env.USELIB
